===============================================================
SciPy2015 tutorial: Analyzing and Manipulating Data with Pandas
===============================================================

This repository contains all the material needed by students registered to the
Pandas tutorial of **SciPy 2015** (http://scipy2015.scipy.org/ehome/115969/289057/?&)
on July Mon July 6th 2015.


Content needed
===============
This github repository is all that is needed in terms of tutorial content. To
install it on your machine, you will need a git client.

Windows
-------
A good one git client for Windows can be downloaded at
http://www.git-scm.com/downloads.
When you install git, you will be asked where to make git available from and
what kind of line ending policy you prefer. If you are not sure, we recommend
that you allow to run git from the command prompt if possible, as it is more
flexible than only running git from the git bash tool that comes with it. Also,
for line ending, the option commonly chosen is
**Checkout Windows-Style, commit unix-style line endings**.


Mac OSX
-------
A good one git client for Windows can be downloaded at
http://www.git-scm.com/downloads.
It installs git in /usr/local/git/bin/, so to have it available from any
terminal, you will want to make sure that location is on your PATH environment
variable.


Linux
-----
The easiest on Linux is to install git from your distro's package manager (yum
for redhat based distros, apt-get for Ubuntu, ...). For example on Ubuntu, it
should be enough to type::

    $ sudo apt-get install git


Further instructions for all platforms
---------------------------------------

Once git is available, you will need to clone this repository. Its SSH URL is
git@github.com:jonathanrocher/pandas_tutorial.git. To do that, you should be
able to start a command prompt/terminal (or the git bash prompt if you chose to
only make git accessible from there) and type::

    git clone git@github.com:jonathanrocher/pandas_tutorial.git

That will create a new folder named SciPy2015_pandas_tutorial/ with all the
content you will need.

As you get closer to the day of the tutorial, it is highly recommended to
update this repository, as I will be improving it this week. To update it, open
a command prompt, move **into** the SciPy2015_pandas_tutorial/ folder and run::

    $ git pull


Python distribution and packages needed
=======================================

If you don't already have a working distribution, by far the easiest way to get
everything you need for this tutorial is to download
Enthought Canopy (https://store.enthought.com/, the free version is enough),
or Continuum's Anaconda (http://continuum.io/downloads). That is due to the
number of dependencies it has that we will want to play with during the
tutorial. The tutorial should be pretty agnostic of whether you are running
Python 2.7 or Python 3.3+, but I will be using Python 2.7 and if you don't
already have a distribution, I

If you already have a working distribution, you will need to make sure that you
install or update all needed packages. To be able to run the examples, demoes
and exercises, you must have the following packages installed:
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


Questions? Problems?
====================
Questions? Problems? Don't wait, shoot me and the rest of the group an email on
the tutorial mailing list.
