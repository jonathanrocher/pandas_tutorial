# Copyright 2015 Enthought, Inc. All Rights Reserved
"""
Stock returns
=============

We have loaded for you some data from the IO exercise which contains adjusted-
close data for 6 major stocks between 2005 and 2009.  In this exercise, we
will explore looking for correlations between these stocks.

1. Our first task is going to be cleaning up the missing values found in this
   dataset.  First, print the list of days where one of the stocks is a missing
   value.  Print the list of pairs (day, stock) for each missing value.

2. Since interpolating to fill in the missing values wouldn't be meaningful in
   this context, we will combine the loaded dataset with public stock market
   values that can be downloaded from the web.  Use IPython to learn about
   ``pandas.io.data.get_data_yahoo`` or ``pandas.io.data.get_data_google`` and
   download a Panel of stock values for a range of date that covers the range
   found in question 1.

Note: If you don't have an internet connection, clean the data by truncating
the dataset after the last date that has a missing value.  Then skip to
question 4.

3. Build a dataframe of 'Adjusted Close' values and use it to build a dataset
   similar to the one loaded from the txt file but that contains no more
   missing values.  We will assume that we don't trust online data as much as
   the one we loaded initially, so if there are 2 non-missing values, we will
   use the one from the text file.

4. Make a plot of all stock market timeseries.

5. Build another dataframe with all values renormalized by the value of the
   stock at their value on Jan 3rd, 2005.  Plot it in a different figure.

6. The daily return of a stock is defined by::

   >            adj clos(t+1) - adj clos(t)   adj clos(t+1)
   >     r(t) = --------------------------- = -------------  - 1
   >                   adj clos(t)             adj clos(t)

   Build another dataframe with the daily returns for each stock for each day
   except Jan 3rd, 2005.  Plot it in a different figure.

7. We would like to visualize how correlated these returns are.  In a new
   figure, make a scatter_matrix plot to show a scatter plot between each pair
   of tickers.  On the diagonal, let's display the reconstructed pdf of these
   returns using the kernel density estimator method.  For this, look at the
   optional keyword arguments of the scatter_matrix function.

8. The previous plot is simply a visualization of the values. Let's compute
   the actual correlation between each pair of returns.  Matplotlib's imshow
   represents a 2D array of data like an image.  That function can be used
   directly on dataframe.  Use imshow to build a heatmap of the correlations of
   returns.  Explore the different possible Explore how that map changes when a
   different correlaton algorithm is used.

See :ref:`stock-return-solution`.
"""
from pandas import read_table, scatter_matrix
from pandas.io.data import get_data_yahoo, get_data_google, RemoteDataError


import numpy as np
from matplotlib.pyplot import colorbar, figure, imshow, show, title, xticks, \
    yticks

# 0.
local_dataset = read_table("adj_close_stock_data_2005_2010.txt",
                           sep="\s+", parse_dates=[[0, 1, 2]], na_values="-")
local_dataset = local_dataset.set_index("year_month_day")
local_dataset.index.name = "Date"

# 1.

# 2.

# 3.

# 4:

# 5:

# 6.

# 7.

# 8.
