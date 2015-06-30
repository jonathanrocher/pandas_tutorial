# Copyright 2015 Enthought, Inc. All Rights Reserved
"""
Pandas DataFrame
----------------

This is a basic fluency exercise.  Each part can be solved with just one line
of code.

Topics: Pandas DataFrame, pivot, pivot_table, groupby

1. In the code below, read_csv() reads the file "sales.csv" into the DataFrame
   df1.  It looks like this::

            Quarter    Name  Product  Service
        0         1    Kahn    345.7     90.0
        1         1  Porter    291.0      0.0
        2         1     Lin    406.5    131.0
        3         1   Mason    222.0     14.0
        4         2    Kahn    295.0     65.5
        5         2  Porter    131.0     19.1
        6         2     Lin    319.5     12.0
        7         2   Mason    263.1     45.0
        8         3    Kahn    195.0      6.7
        9         3  Porter    155.9     33.9
        10        3     Lin    126.5     89.0
        11        3   Mason    140.0    101.5
        12        4    Kahn    445.1      8.2
        13        4  Porter    308.3     90.0
        14        4     Lin    410.0     14.0
        15        4   Mason    251.6     63.0

   Use the pivot() method to create a new DataFrame whose index is 'Name',
   whose columns are the Quarters, and whose values are from the 'Product'
   column.  It should look like this::

        Quarter      1      2      3      4
        Name
        Kahn     345.7  295.0  195.0  445.1
        Lin      406.5  319.5  126.5  410.0
        Mason    222.0  263.1  140.0  251.6
        Porter   291.0  131.0  155.9  308.3

2. Use the pivot_table() method of df1 to generate a DataFrame that looks
   like this::

                 Product                       Service
        Quarter        1      2      3      4        1     2      3     4
        Name
        Kahn       345.7  295.0  195.0  445.1       90  65.5    6.7   8.2
        Lin        406.5  319.5  126.5  410.0      131  12.0   89.0  14.0
        Mason      222.0  263.1  140.0  251.6       14  45.0  101.5  63.0
        Porter     291.0  131.0  155.9  308.3        0  19.1   33.9  90.0

   Note that no aggregation is performed in that table.  Also note that
   the column index is hierarchical: it has the form (s, q), where
   s is either 'Product' or 'Service' and q is the Quarter.

3. This part requires the use of the `aggfunc` argument of pivot_table().
   From df1 of part 1, use the pivot_table() method to create a DataFrame
   that looks like this::

                 Product  Service
        Quarter
        1         1265.2    235.0
        2         1008.6    141.6
        3          617.4    231.1
        4         1415.0    175.2

   The table shows the quarterly sales totals for the 'Product' and
   'Service' categories.

4. A slight variation of part 3: from df1 of part 1, use the pivot_table()
   method to create a DataFrame that looks like this::

                Product  Service
        Name
        Kahn     1280.8    170.4
        Lin      1262.5    246.0
        Mason     876.7    223.5
        Porter    886.2    143.0

   It shows the total product and service sales for each person.

5. Modify your answer to part 4 to include the column sums in the result.
   Hint: look at the 'margins' argument to pivot_table().

6. Add a 'Total' column to result of part 5, so that it looks like::

                Product  Service   Total
        Name
        Kahn     1280.8    170.4  1451.2
        Lin      1262.5    246.0  1508.5
        Mason     876.7    223.5  1100.2
        Porter    886.2    143.0  1029.2
        All      4306.2    782.9  5089.1

7. Reproduce the answer of part 3 using the groupby() method.

8. Reproduce the answer of part 4 using the groupby() method.

   Your first attempt might produce this DataFrame::

                Quarter  Product  Service
        Name
        Kahn         10   1280.8    170.4
        Lin          10   1262.5    246.0
        Mason        10    876.7    223.5
        Porter       10    886.2    143.0

   The 'Quarter' column is not useful; a slight modification can be used
   to keep just the 'Product' and 'Service' columns.


See :ref:`pandas-dataframe-solution`.
"""

import pandas as pd


df1 = pd.read_csv('sales.csv')


# 1

print "1.", "-" * 65
print df1.pivot(index='Name', columns='Quarter', values='Product')
print


# 2

print "2.", "-" * 65
print df1.pivot_table(index='Name', columns=['Quarter'])
print


# 3

print "3.", "-" * 65
print df1.pivot_table(values=['Product', 'Service'], index='Quarter', aggfunc='sum')
print

# 4

df2 = df1.pivot_table(values=['Product', 'Service'], index='Name', aggfunc='sum')

print "4.", "-" * 65
print df2
print


# 5

df2 = df1.pivot_table(values=['Product', 'Service'], index='Name', aggfunc='sum', margins=True)

print "5.", "-" * 65
print df2
print


# 6

df2['Total'] = df2['Product'] + df2['Service']

print "6.", "-" * 65
print df2
print


# 7

print "7.", "-" * 65
print df1.groupby('Quarter').sum()
print


# 8

print "8.", "-" * 65
# Use groupby(), and then keep only the 'Product' and 'Service' columns
# before applying the sum() method.
print df1.groupby('Name')['Product', 'Service'].sum()
print

# ...or drop the 'Quarter' column before performing the groupby operation:
# print df1.drop('Quarter', axis=1).groupby('Name').sum()
