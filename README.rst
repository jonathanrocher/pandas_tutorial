pandas_tutorial
===============

This repository contains all the material needed by students registered to the
Pandas tutorial of `SciPy 2015<http://scipy2015.scipy.org/ehome/115969/289057/?&>`_
on July Mon July 6th 2015.


Packages needed
---------------

If you don't already have a working distribution, by far the easiest way to get
everything you need is to download `Enthought Canopy<https://store.enthought.com/>`_,
or `Anaconda<http://continuum.io/downloads>`_. That is due to the complexity of
compiling pandas by yourself, and the number of (optional) dependencies it has
that we will want to play with during the tutorial.

To be able to run the core demoes and exercises, you must have the following
packages installed:
- pandas 0.15+
- numpy 1.8+
- matplotlib
- nose (only to test your distribution)

In certain parts of the class, demoes or exercises, the following packages will
be used occasionally:
- ipython
- pytables
- lxml
- beautifulsoup4
- html5lib

To test your installation, please execute the :py:`test_python_install.py`
script using the `nosetests` executable:

    $ nosetests test_python_install.py
    ....
    ----------------------------------------------------------------------
    Ran ** tests in ** s

    OK
