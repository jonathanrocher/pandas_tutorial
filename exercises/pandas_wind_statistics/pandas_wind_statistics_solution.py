# Copyright 2015 Enthought, Inc. All Rights Reserved
"""
Wind Statistics
----------------

This exercise is an alternative version of the Numpy exercise but this time we
will be using pandas for all tasks. The data have been modified to contain some
missing values, identified by NaN.  Using pandas should make this exercise
easier, in particular for the bonus question.


Of course, you should be able to perform all of these operations without using
a for loop or other looping construct.


Topics: Pandas, time-series

1. The data in 'wind.data' has the following format::

        Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
        61  1  1 15.04 14.96 13.17  9.29   NaN  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'read_table' function from pandas to read the data into
   a DataFrame.

2. Replace the first 3 columns by a proper datetime index.

3. Compute how many values are missing for each location over the entire
   record.  They should be ignored in all calculations below. Compute how many
   non-missing values there are in total.

4. Calculate the mean windspeeds of the windspeeds over all the locations and
   all the times (a single number for the entire dataset).

5. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)

6. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)

7. Find the average windspeed in January for each location.  Treat
   January 1961 and January 1962 both as January.

8. Downsample the record to a yearly, monthly and weekly frequency
   for each location.

9. Plot the time series and a box plot of the monthly data for each location.

Bonus
~~~~~

10. Calculate the mean windspeed for each month in the dataset.  Treat
    January 1961 and January 1962 as *different* months.

11. Calculate the min, max and mean windspeeds and standard deviations of the
    windspeeds across all locations for each week (assume that the first week
    starts on January 1 1961) for the first 52 weeks.

Notes
~~~~~

This solution has been tested with Pandas version 0.14.1.

The original data from which these were derived were analyzed in detail in the
following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.

"""
from matplotlib import pyplot as plt
from pandas import read_table, set_option, Period

# Part 1 & 2 - read the file and make dates

def custom_date_parser(year_str, month_str, day_str):
    """ Return a pandas 'Period' representing the day

    A Period represents the whole day, while a datetime or a timestamp
    represents a particular moment in time.  Period is better for this data,
    particularly when we resample.

    """
    full_date_str = '19{0}-{1}-{2}'.format(year_str, month_str, day_str)
    return Period(full_date_str, freq='D')

wind_data = read_table('wind.data', sep='\s+', index_col=0,
                       parse_dates=[[0, 1, 2]], date_parser=custom_date_parser)

# Non-missing values at each location
print "3. Number of non-missing values for each location:"
print wind_data.count()
non_null_count = wind_data.count().sum()
print "There are {0} non-missing values in the entire dataset".format(
    non_null_count)
print

print '4. Mean over all values'
total = wind_data.sum().sum()
print '  mean:', total/non_null_count
print

print '5. Statistics over all days at each location'
print '  min:', wind_data.min()
print '  max:', wind_data.max()
print '  mean:', wind_data.mean()
print '  standard deviation:', wind_data.std()
print

print '6. Statistics over all locations for each day'
print '  min:', wind_data.min(axis=1)
print '  max:', wind_data.max(axis=1)
print '  mean:', wind_data.mean(axis=1)
print '  standard deviation:', wind_data.std(axis=1)
print

# Part 7 - January data
january_data = wind_data[wind_data.index.month == 1]
print "January windspeeds:"
print january_data.mean()
print

# Downsample the data to yearly, monthly and weekly data
print "8. Downsampled data:"
print "Yearly:", wind_data.resample('A', how='mean')

print "Monthly:", wind_data.resample('M', how='mean')

print "Weekly:", wind_data.resample('W', how='mean')
print

# 9. Plots
monthly_data = wind_data.resample('M', how='mean')
monthly_data.plot()
# Force this plot to happen in a separate figure
plt.figure()
monthly_data.boxplot()
plt.show()

# 10. This is just another way to group records:
unique_monthly_grouped = wind_data.groupby(lambda d: (d.month, d.year))
print '10. Mean wind speed for each month in each location'
print unique_monthly_grouped.mean()
print


# 11. Weekly stats over the first year
first_year = wind_data[wind_data.index.year == 1961]
stats = wind_data.resample('W', how='mean').apply(lambda x: x.describe())
set_option('display.max_rows', 999)
set_option('display.max_columns', 15)
set_option('display.notebook_repr_html', False)
print stats
