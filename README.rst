===========================================================================
SciPy2015 & SciPy2016 tutorial: Analyzing and Manipulating Data with Pandas
===========================================================================

This repository contains all the material needed by students registered to the
Pandas tutorial of **SciPy 2016** (http://scipy2016.scipy.org/)
on July Tuesday July 12th 2016.

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

**Note for Enthought Canopy users:** To reduce download time, the Canopy
installer doesn't contain some of the packages we will need. After
installation, please login inside the application (on the welcome screen). Then
go to the package manager (in the Tools menu) and install any of the packages
below that are not already present. Specifically, statsmodels and pytables
aren't part of the free installer, though they can be installed with a free
account. If you prefer the command line, run:

    enpkg statsmodels pytables

**Note for Anaconda users:** The Python 3.5 installer has all the packages
needed except html5lib. Install it with a:

    conda install html5lib


You already have your distribution
----------------------------------
Version of python
*****************
The tutorial has been tested and can be run under Python 2.7.10+ and
Python 3.5+. Bring the flavor you want.

Packages needed
***************
If you already have a working distribution, you will need to make sure that you
install or update all needed packages. To be able to run the examples, demoes
and exercises, you must have the following packages installed:
- pandas 0.18+
- numpy 1.10+
- matplotlib 1.5+
- html5lib 0.999+
- lxml
- BeautifulSoup4 (careful to get BeautifulSoup4, not just BeautifulSoup!)
- jupyter 1.0 or ipython 4.0+ (for running, experimenting and doing exercises)
- statsmodels 0.6+
- pytables 3.1+
- nose (only to test your python installation)


Testing that you are all set
----------------------------
To test your installation, please execute the :py:`check_env.py`
script:

    $ python check_env.py
    ....
    ----------------------------------------------------------------------
    Ran ** tests in ** s

    OK

If you see some import errors, try to run:

    enpkg <PACKAGE NAME>

or:

    conda install <PACKAGE NAME>

depending on your distribution.


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
The easiest on Linux is to install git from your distro's package manager
(yum for redhat based distros, apt-get for Ubuntu, ...). For example on
Ubuntu, it should be enough to run::

    $ sudo apt-get install git


Step2: Download the material (all platforms)
--------------------------------------------

Once git is available, you will need to clone this repository. Its HTTPS URL is
https://github.com/jonathanrocher/pandas_tutorial.git. To do that, you should be
able to start a command prompt/terminal (or the git bash prompt if you chose to
only make git accessible from there) and type::

    git clone https://github.com/jonathanrocher/pandas_tutorial.git

That will create a new folder named pandas_tutorial/ with all the
content you will need, mostly a folder named climate_timeseries/ with the
demo notebook that we will follow for the whole tutorial.

As you get closer to the day of the tutorial, it is highly recommended to
update this repository, as I will be improving it this week. To update it, open
a command prompt, move **into** the pandas_tutorial/ folder and run::

    $ git pull



Questions? Problems?
====================
Questions? Problems? Don't wait! Shoot me and the rest of the group a message
on the tutorial's slack channel::

    https://scipy2016.slack.com/messages/pandas/

That requires to create a (free) slack account on
``https://scipy2016.slack.com``, following the instructions in the email you
(should have) received from Jill Cowan on June 29th 2016. Once the account is
created, you will need to click on ``CHANNELS (22)`` in the left banner to find
the pandas channel. If you have issues connecting to slack or finding the
pandas channel, ping me on twitter `@jonrocher`.
