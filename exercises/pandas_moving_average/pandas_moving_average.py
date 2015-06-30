# Copyright 2015 Enthought, Inc. All Rights Reserved
"""
Pandas Moving Average
---------------------

In this exercise, you will use Pandas to compute and plot the moving
average of a time series.  The file 'data.txt' contains measurements
from a lake, recorded every half hour.  There are missing data points
scattered throughout the data set.

*Note.*  The index in the DataFrame created below contains timestamps,
but no special time series features will be used, so it is not necessary
to have covered Pandas time series before doing this exercise.

0. Use pandas.read_table() to read the data from the file 'data.txt'
   into a Pandas DataFrame.  The columns in the DataFrame are 'temp'
   (temperature), 'sal' (salinity), 'ph' and 'depth'.  Plot the temperature.
   (Part 0 is done for you below.)

1. Use pandas.rolling_mean() to compute and plot the moving average of the
   temperature using a window of 12 hours.  (Note that the sample period of the
   data is a half hour, so 12 hours corresponds to a window of 24 samples.)
   Then do the same for windows of 24 and 48 hours.

   *Hint:* Use the `min_periods` argument to specify that at least 12
   samples are needed in a window.  What happens if you do not
   specify `min_periods`?

2. Add a plot of the exponentially weighted moving average to the plot
   created in part 1.  The function to compute this is pandas.ewma().
   If `x` is the input series, the exponentially weighted moving
   average is the time series `y` where::

       y[0] = x[0]
       y[k] = alpha * x[k] + (1 - alpha) * y[k - 1]  for k > 0.

   So the output at time `k` is a weighted combination of the input
   at time `k` and the output at time `k` - 1.

   The parameter `alpha` is not given directly.  Instead, `span` is
   given, where::

       alpha = 2 / (span + 1)

   Experiment with different values of `span`.  (You can also use the
   keyword argument `com`, where `alpha = 1 / (com + 1)`.)

See :ref:`pandas-moving-average-solution`.

"""

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


# 0.

# To parse the time field of the file, we use the following
# timestamp format:
fmt = "%Y%j+%H%M"

df = pd.read_table('data.txt', sep='\s+', skiprows=22, skip_footer=1,
                   names=['time', 'temp', 'sal', 'ph', 'depth'],
                   parse_dates=True,
                   date_parser=lambda s: datetime.strptime(s, fmt),
                   index_col=0)

temp = df['temp']

temp.plot(label='Raw data')


# 1.


# 2.


# ---
plt.legend(loc='best')
plt.ylabel('Temperature')
plt.show()
