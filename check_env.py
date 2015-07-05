""" Run this file to check your python installation.
"""
from os.path import dirname, join

HERE = dirname(__file__)

def test_import_pandas():
    import pandas


def test_pandas_version():
    import pandas
    version_found = pandas.__version__.split(".")
    version_found = tuple(int(num) for num in version_found)
    assert version_found > (0, 15)


def test_import_numpy():
    import numpy


def test_import_matplotlib():
    import matplotlib.pyplot as plt
    plt.figure
    plt.plot
    plt.legend
    plt.imshow


def test_import_statsmodels():
    import statsmodels as sm
    from statsmodels.formula.api import ols
    from statsmodels.tsa.ar_model import AR


def test_read_html():
    import pandas
    pandas.read_html(join(HERE, "demos", "climate_timeseries", "data",
                     "sea_levels", "Obtaining Tide Gauge Data.html"))


def test_scrape_web():
    import pandas as pd
    pd.read_html("http://en.wikipedia.org/wiki/World_population")


if __name__ == "__main__":
    import nose
    nose.run(defaultTest=__name__)
