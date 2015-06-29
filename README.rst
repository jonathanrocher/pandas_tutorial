===============================================================
SciPy2015 tutorial: Analyzing and Manipulating Data with Pandas
===============================================================

This repository contains all the material needed by students registered to the
Pandas tutorial of **SciPy 2015** (http://scipy2015.scipy.org/ehome/115969/289057/?&)
on July Mon July 6th 2015.


Packages needed
---------------

If you don't already have a working distribution, by far the easiest way to get
everything you need for this tutorial is to download
Enthought Canopy (https://store.enthought.com/, the free version is enough),
or Continuum's Anaconda (http://continuum.io/downloads). That is due to the
number of dependencies it has that we will want to play with during the
tutorial.

If you do, you will need to make sure that you install or update all needed
packages. To be able to run the examples, demoes and exercises, you must have
the following packages installed:
- pandas 0.15+
- numpy 1.8+
- matplotlib 1.4+
- ipython 2.0+ (for running, experimenting and doing exercises)
- nose (only to test your distribution)

In certain parts of the class, demoes or exercises, the following packages will
be used occasionally:
- statsmodels
- lxml
- beautifulsoup4
- html5lib

To test your installation, please execute the :py:`check_env.py`
script:

    $ python check_env.py
    ....
    ----------------------------------------------------------------------
    Ran ** tests in ** s

    OK
