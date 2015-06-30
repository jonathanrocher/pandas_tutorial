# Copyright 2015 Enthought, Inc. All Rights Reserved
"""
Modeling Climate Data in Pandas
-------------------------------

Topics: Pandas, HDF5, FTP file retrieval.

Introduction
~~~~~~~~~~~~

The National Climatic Data Center (NCDC) provides FTP access to extensive
historic and current climate data, collected from weather stations across the
globe.  In this extended exercise, we will download 'Global Surface Summary of
the Day' (GSOD) data from the NCDC servers and use Pandas to analyse and plot
selected data.

The data that we will analyse are organized by year, and stored under the URL:

    ftp://ftp.ncdc.noaa.gov/pub/data/gsod

The file

    ftp://ftp.ncdc.noaa.gov/pub/data/gsod/readme.txt

describes the data format; a copy of this file is stored in the exercise
folder under the name 'gsod_readme.txt'.


1. Retrieve GSOD datafiles for 2008 for the following 3 cities.

    Austin, US
    Cambridge, UK
    Paris, FR

   Store the files locally.  The full URLs for the 3 data files are:

      Austin:     ftp://ftp.ncdc.noaa.gov/pub/data/gsod/2008/999999-23907-2008.op.gz
      Cambridge:  ftp://ftp.ncdc.noaa.gov/pub/data/gsod/2008/035715-99999-2008.op.gz
      Paris:      ftp://ftp.ncdc.noaa.gov/pub/data/gsod/2008/071560-99999-2008.op.gz

   Hint: Use the urlretrieve function from the standard library urllib module
   for this.  You can also use ftplib, if you prefer.

   (Note: in case of difficulties accessing the server, the relevant files are
    also stored in the 'data' subfolder of the exercise folder.)

2. For each of the three cities above:

     (a) Read the datafile into a Pandas DataFrame object with suitable column
         headings.

     (b) Replace missing values (as described in the readme file) for the
         numeric columns with NaNs.

     (c) Use the Year, Month and Day information in the input to construct and
         assign a suitable index for the DataFrame.

     (d) (Optional) Replace the 'FRSHTT' indicators column with six separate
         boolean columns giving fog, rain, snow, hail, thunder and tornado
         indicators.

   Hints: pandas.read_fwf reads data in fixed-format columns.  You may also
   find the gzip standard library module useful for dealing with the compressed
   .gz files.

   Bonus: Extract field heading, column heading and missing data information
   programmatically from the gsod_readme.txt file, rather than copying and
   pasting.

3. The Austin data for the start of the year are missing.  Retrieve alternative
   Austin data for 2008 from the URL:

      Austin (2): ftp://ftp.ncdc.noaa.gov/pub/data/gsod/2008/722544-13958-2008.op.gz

   Now:

     (a) Create a scatter plot comparing the two sets of Austin data.  (You'll
         first need to adjust the two datasets to a common set of indices.)

     (b) Compute a correlation coefficient for the two Austin datasets.

     (c) Finally, fill in the missing days in the original Austin dataset using
         the data from the second Austin dataset.

4. Create a single pandas Panel containing all three datasets.

5. From the panel you created in part 4, extract a DataFrame giving just
   the mean temperatures for each location.  Use this to plot all three
   temperatures on the same graph.

6. Compute and report mean temperatures for the whole year for each location.

7. Compute and plot rolling means with a 14-day window for each of the
   locations.

8. Compute monthly total rainfalls for each location, dropping any locations
   for which no rainfall data are available.  Create a bar plot showing these
   totals.


BONUS:

1. Write a 'CachingClimateDataStore' class that allows easy retrieval of the
   GSOD data, and stores the corresponding pandas dataframe locally in an HDF5
   file.

   For example, your class might be used something like this:

      >>> store = CachingClimateDataStore()
      >>> # Next line goes to the FTP server, fetches the file, turns
      >>> # it into a dataframe and stores it locally.
      >>> paris_climate = store['071560-99999-2008']
      >>> # A second retrieval operation goes straight to the local .h5 file.
      >>> paris_climate = store['071560-99999-2008']

   (Hints: (1) look at the pandas.HDFStore class.  (2) you can override item
   access via the __getitem__ special method.)

2. (Half day to full day team project, open-ended!)  Use Traits and Chaco (or a
   UI toolkit of your choice) to write an application that allows the user to:

     - retrieve data for cities on request

     - display plots showing a summary of the data for any particular year and
       location

     - compare two locations (or two years for the same location), showing
       scatter plots, combined graphs, and correlation coefficients.

See :ref:`pandas-climate-data-solution`.

"""

# Standard library imports.
import contextlib
import cStringIO
import datetime
import ftplib
import gzip

# 3rd party library imports.
from matplotlib import pyplot
import numpy
import pandas
import tables


def read_column_descriptions():
    """
    Retrieve field names and positions from the 'gsod_readme.txt' file.

    """
    with open('gsod_readme.txt') as f:
        readme = f.read()

    # Extract portion of the readme that describes the fields.
    readme = readme[readme.index('FIELD'):]
    readme = readme[:readme.index('*****')]

    # Find column indices for this portion of the README.
    position = readme.index('POSITION')
    field_type = readme.index('TYPE')
    description = readme.index('DESCRIPTION')

    # Extract lines; throw away the header.
    readme_lines = readme.splitlines()[1:]

    # Extract chunks: each chunk is a list of rows giving
    # information about one field of the climate data file.
    rows = [
        i for i, line in enumerate(readme_lines)
        if line[:position].strip()
    ]
    chunks = [
        readme_lines[start_row:end_row]
        for start_row, end_row in zip(rows, rows[1:] + [len(readme_lines)])
    ]

    # Extract field names.
    fields = [chunk[0][:position].strip() for chunk in chunks]
    # Field names in the readme.txt are not unique: names 'Count' and 'Flag'
    # occur multiple times.  We prefix each occurrence of 'Count' or 'Flag'
    # with the field name from the preceding column.
    fields = [
        fields[i - 1] + field if field in ['Count', 'Flag'] else field
        for i, field in enumerate(fields)
    ]

    # Extract field positions.
    positions = []
    for chunk in chunks:
        start, end = chunk[0][position:field_type].split('-')
        # Columns in readme.txt are 1-based with an *inclusive* end column.
        # Adjust for 0-based values with an *exclusive* end column.
        positions.append((int(start) - 1, int(end)))

    # Extract descriptions, then information about missing values.
    missing = {}
    descriptions = [
        ''.join([line[description:] + '\n' for line in chunk])
        for chunk in chunks
    ]
    for field, description in zip(fields, descriptions):
        words = description.split()
        if 'Missing' in words:
            index = words.index('Missing')
            assert words[index + 1] == '='
            missing[field] = float(words[index + 2])

    return fields, positions, missing


def read_raw_data(file):
    """
    Read raw climate data from the given open file or file-like object,
    returning a pandas DataFrame object.

    """
    fields, positions, missing = read_column_descriptions()

    # We convert the MAXFlag and MINFlag columns to booleans directly on
    # reading.
    field_converters = {
        'MAXFlag': lambda s: s == '*',
        'MINFlag': lambda s: s == '*',
    }

    # Use read_fwf for reading fixed-width columns.
    climate_data = pandas.read_fwf(
        file,
        colspecs=positions,
        names=fields,
        skiprows=1,
        converters=field_converters,
    )

    # Remove 'YEAR' and 'MODA' columns, and use them to set the index.
    year = climate_data.pop('YEAR')
    month_and_day = climate_data.pop('MODA')
    month = month_and_day // 100
    day = month_and_day % 100
    climate_data.index = map(datetime.datetime, year, month, day)

    # Replace missing values in numeric columns.
    for field, missing_value in missing.items():
        series = climate_data[field]
        series[series == missing_value] = numpy.NaN

    # Replace the indicators 'FRSHTT' column with 6 separate boolean columns.
    indicators = climate_data.pop('FRSHTT')
    climate_data['FOG'] = indicators // 10 ** 5 == 1
    climate_data['RAIN'] = indicators // 10 ** 4 % 10 == 1
    climate_data['SNOW'] = indicators // 10 ** 3 % 10 == 1
    climate_data['HAIL'] = indicators // 10 ** 2 % 10 == 1
    climate_data['THUNDER'] = indicators // 10 % 10 == 1
    climate_data['TORNADO'] = indicators % 10 == 1
    return climate_data


class RemoteClimateDataStore(object):
    """
    Dict-like class allowing read-only access to climate data FTP site,
    returning pandas DataFrames.

    """
    def __init__(self, site='ftp.ncdc.noaa.gov', directory='pub/data/gsod'):
        self.site = site
        self.directory = directory

    def __getitem__(self, location):
        year = location.split('-')[-1]
        dirname = '{}/{}'.format(self.directory, year)
        filename = '{}.op.gz'.format(location)

        # Retrieving an FTP file the hard way.  See also urllib.urlretrieve.
        connection = ftplib.FTP(self.site)
        with contextlib.closing(connection):
            connection.login()
            connection.cwd(dirname)
            compressed_output = cStringIO.StringIO()
            connection.retrbinary(
                'retr {}'.format(filename),
                compressed_output.write,
            )
            compressed_output.seek(0)
            with gzip.GzipFile(fileobj=compressed_output) as z:
                return read_raw_data(z)


class CachingClimateDataStore(object):
    """
    Dict-like class representing store for raw dataframes corresponding
    to climate data files.

    """
    def __init__(self, local_store=None, remote_store=None):
        if local_store is None:
            local_store = pandas.HDFStore('gsod_climate_data.h5')
        if remote_store is None:
            remote_store = RemoteClimateDataStore()
        self.local_store = local_store
        self.remote_store = remote_store

    def __getitem__(self, location):
        try:
            df = self.local_store[location]
        # Pandas 0.8 gives a NodeError;  0.10 gives a KeyError.  Catch both
        # to be on the safe side.
        except (tables.NodeError, KeyError):
            df = self.remote_store[location]
            self.local_store[location] = df
        return df


def main():
    # 1. Retrieve climate data files for 2008 for Austin, Cambridge and Paris.
    # 2. For each city, read the data into a Pandas DataFrame object.

    store = CachingClimateDataStore()
    austin_climate = store['999999-23907-2008']
    cambridge_climate = store['035715-99999-2008']
    paris_climate = store['071560-99999-2008']
    alternative_austin_climate = store['722544-13958-2008']

    # Plotting the two Austin temperature data on the same plot.
    austin_climate['TEMP'].plot()
    alternative_austin_climate['TEMP'].plot()
    pyplot.show()

    # Creating a scatter plot for the two datasets.  Requires matching
    # the indices first, using the 'align' method.
    austin1, austin2 = austin_climate['TEMP'].align(
        alternative_austin_climate['TEMP'],
        join='inner',
    )
    pyplot.figure()
    pyplot.scatter(austin1, austin2)
    pyplot.show()

    # Computing the correlation.
    print "Correlation coefficient between the two Austin temperature sets: ",
    print austin_climate['TEMP'].corr(alternative_austin_climate['TEMP'])

    # Joining the Austin data into a single dataframe.
    austin_climate = austin_climate.combine_first(alternative_austin_climate)

    # 3. Create a single pandas Panel containing all three datasets.
    climate_panel = pandas.Panel(
        dict(
            Cambridge=cambridge_climate,
            Austin=austin_climate,
            Paris=paris_climate,
        )
    )

    # Extract a DataFrame giving temperatures only for the three locations.
    temp_df = climate_panel.minor_xs('TEMP')

    # ... and use this to plot all three temperatures on the same graph.
    temp_df.plot()
    pyplot.show()

    # Find mean temperatures for the year in Cambridge, Austin and Paris.
    print "Mean temperatures"
    print temp_df.mean()

    # Compute and plot rolling means with a 14-day window for the temperature.
    rolling_means = pandas.rolling_mean(temp_df, window=10)
    rolling_means.plot()
    pyplot.show()

    # Compute monthly total rainfalls in Austin and Paris.
    rainfall = climate_panel.minor_xs('PRCP')
    monthly_rainfall = rainfall.groupby(lambda dt: dt.month).agg(numpy.sum)
    # Drop columns containing no values.
    monthly_rainfall = monthly_rainfall.dropna(axis=1, how='all')

    # Plot bar plot.
    monthly_rainfall.plot(kind='bar')
    pyplot.show()


if __name__ == '__main__':
    main()
