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
   file called 'gsod_climate_data.h5'.

   For example, your class might be used something like this:

      >>> store = CachingClimateDataStore()
      >>> # Next line goes to the FTP server, fetches the file, turns
      >>> # it into a dataframe and stores it locally in the HDF5 file.
      >>> paris_climate = store['071560-99999-2008']
      >>> # A second retrieval operation retrieves data directly from the HDF5
      >>> # file.
      >>> paris_climate = store['071560-99999-2008']

   (Hints: (1) look at the pandas.HDFStore class.  (2) you can override item
   access via the __getitem__ special method.)

2. (Half-day to full-day team project, open-ended!)  Use Traits and Chaco (or a
   UI toolkit of your choice) to write an application that allows the user to:

     - Retrieve data for cities on request, and store the data locally in an
       HDF5 file.

     - Display plots showing a summary of the data for any particular year and
       location.

     - Compare two locations (or two years for the same location), showing
       scatter plots, combined graphs, and correlation coefficients.

See :ref:`pandas-climate-data-solution`.

"""
