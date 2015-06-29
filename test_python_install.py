from os.path import abspath, dirname, join


HERE = abspath(dirname(__file__))


def test_import_pandas():
    import pandas


def test_pandas_version():
    import pandas
    version_found = tuple(pandas.__version__.split("."))
    assert version_found > (0, 15)


def test_import_numpy():
    import numpy


def test_import_matplotlib():
    import matplotlib


def test_scrape_web():
    import pandas as pd
    pd.read_html("http://en.wikipedia.org/wiki/World_population")
