===============================================================
SciPy2015 tutorial: Analyzing and Manipulating Data with Pandas
===============================================================

This repository contains all the material needed by students registered to the
Pandas tutorial of **SciPy 2015** (http://scipy2015.scipy.org/ehome/115969/289057/?&)
on July Mon July 6th 2015.

For a smooth experience, you will need to make sure that you install or update
your python distribution and download the tutorial material **before** the day
of the tutorial as the wifi at the ATT center can be flakey.


Python distribution and Packages needed
=======================================

Downloading a pre-made distribution
------------------------------------
If you don't already have a working distribution, by far the easiest way to get
everything you need for this tutorial is to download
Enthought Canopy (https://store.enthought.com/, the free version is enough),
or Continuum's Anaconda (http://continuum.io/downloads). That is due to the
number of dependencies it has that we will want to play with during the
tutorial.

**Note for Enthought Canopy users:** To reduce download time, the regular
installer of Canopy doesn't contain some of the packages we will need. After
installation, please login inside the application (on the welcome screen). Then
go to the package manager (in the Tools menu) and install any of the packages
below that are not already present. Specifically, statsmodels, lxml,
beautifulSoup4 (note the 4, not just BeautifulSoup!), html5lib are the only
ones that may not be present depending on the version of installer you choose.


You already have your distribution
----------------------------------
Version of python
*****************
The tutorial should be pretty agnostic of whether you are running
Python 2.7+ or Python 3.3+, but I will be using Python 2.7 and my material has
been tested somewhat more on Python 2. If you don't already have a
distribution, I recommend that you intall a Python2 distribution. If you
already have a Python3 distribution, you will be fine, and might just have to
replace some print statements by functions in occasional places.

Packages needed
***************
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
- statsmodels 0.6+
- lxml
- beautifulsoup4 (careful to get BeautifulSoup4, not just BeautifulSoup!)
- html5lib


Testing that you are all set
----------------------------
To test your installation, please execute the :py:`check_env.py`
script:

    $ python check_env.py
    ....
    ----------------------------------------------------------------------
    Ran ** tests in ** s

    OK


Content needed
===============
This github repository is all that is needed in terms of tutorial content. To
install it on your machine, you will need a git client and then to clone this
repository. Make sure to update that clone *before* coming to the tutorial on
Monday morning to catch any update.

Step1: Install a git client
---------------------------
* Windows
---------
A good git client for Windows can be downloaded at
http://www.git-scm.com/downloads.
When you install git, you will be asked where to make git available from and
what kind of line ending policy you prefer. If you are not sure, we recommend
that you allow to run git from the command prompt if possible, as it is more
flexible than only running git from the git bash tool that comes with it. Also,
for line ending, the option commonly chosen is
**Checkout Windows-Style, commit unix-style line endings**.


* Mac OSX
---------
If you don't already have git available, a good git client for Mac can be
downloaded at http://www.git-scm.com/downloads.
It installs git in /usr/local/git/bin/, so to have it available from any
terminal, you will want to make sure that location is on your PATH environment
variable.


* Linux
-------
The easiest on Linux is to install git from your distro's package manager (yum
for redhat based distros, apt-get for Ubuntu, ...). For example on Ubuntu, it
should be enough to type::

    $ sudo apt-get install git


Step2: Download the material (all platforms)
--------------------------------------------

Once git is available, you will need to clone this repository. Its HTTPS URL is
https://github.com/jonathanrocher/pandas_tutorial.git. To do that, you should be
able to start a command prompt/terminal (or the git bash prompt if you chose to
only make git accessible from there) and type::

    git clone https://github.com/jonathanrocher/pandas_tutorial.git

That will create a new folder named SciPy2015_pandas_tutorial/ with all the
content you will need: the slides I will go through (slides.pdf), and a folder
of exercises.

As you get closer to the day of the tutorial, it is highly recommended to
update this repository, as I will be improving it this week. To update it, open
a command prompt, move **into** the SciPy2015_pandas_tutorial/ folder and run::

    $ git pull



Questions? Problems?
====================
Questions? Problems? Don't wait, shoot me and the rest of the group an email on
the tutorial mailing list: scipy2015-pandas-tutorial@googlegroups.com. You can
view all message and sign up at
https://groups.google.com/forum/#!forum/scipy2015-pandas-tutorial
