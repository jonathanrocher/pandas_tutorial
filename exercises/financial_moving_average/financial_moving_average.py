# Copyright 2015 Enthought, Inc. All Rights Reserved
"""

Financial moving average
=========================

We have loaded for you some data from the IO exercise which contains adjusted
close data for 6 major stocks between 2005 and 2009. In this timeseries, we
will experiment with windowed operations, and he rolling average in particular.

1. Make a timeseries of the adjusted close for Exxon Mobil. We will call it
`ts`. Plot it.

2. Make 3 other times series, built from ts, but made of its moving average
with window sizes of 20, 40 and 80. Plot all 3 of them on top of the raw data.

3. Zoom in the plot of the timeseries around the first 100 values and observe
how each rolling average starts at different point in time because of the sizes
of their windows. However, notice how the first rolling average (with
window=20) is discontinuous. Why is that?

4. Let's find or build our own average function that ignores missing values
(NaN). For that, it will be valuable to look at NumPy's function that contain
nan in their names. Apply that function to the timeseries using a window of 20.
Plot the result to compare with the curve given by the regular rolling_mean.
Did that help?

5. The reason it didn't help is that before the custom function is applied, the
presence of nan values is tested by pandas' rolling functions (rolling_mean and
rolling_apply). The solution resides in the use of its min_periods keyword
argument. Use it to compute the rolling average without discontinuities.

Bonus
~~~~~
6. Add a plot of the exponentially weighted moving average to the plot
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

See :ref:`financial-moving-average-solution`.
"""
from pandas import read_table, ewma, rolling_apply, rolling_mean
import numpy as np
from matplotlib.pyplot import legend, show

# 1.
df = read_table("adj_close_stock_data_yahoo_2005_2010.txt",
                   sep="\s+", parse_dates=[[0,1,2]], na_values="-")
df = df.set_index("year_month_day")
