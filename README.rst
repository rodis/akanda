~~~~~~
akanda
~~~~~~

An open source packet filter solution for OpenStack deployments.


About
=====


The Code
--------
The code for this project contains the following:

* a simple, blocking API that wraps py-pf

* various scripts that make use of this API

* a non-blocking REST server that also makes use of this API


The Product
-----------

Basically, any OS with the following installed and running on it, we consider
an Akanda product:

* PF

* py-pf

* the Akanda REST server


The Name
--------

We originally wanted to go with the name अनर्थक (anarthaka, "bullshit"). But
sadly, this term also conveys things like "worthless," "useless," and
"unprofitable." As a product (even an open source one), these are not very
positive associations ;-)

However, we found we were able to say something more clearly and with a bevy of
excellent synonyms by using the Sanskrit word अखण्ड (akhaNDa) which has such
lovely connotations as "non-stop," "undivided," "entire," "whole," and most
importantly, "**not broken**."


Dependencies
============

* An Akanda instance up and running (a BSD with packet filter installed and
  configured)

* The Akanda code installed (this will install other dependencies
  automatically)


Installation
============


Building an OpenBSD Dev Environment
-----------------------------------

Set up your packge URL, e.g.::

  export BSD_MIRROR=mirror.ece.vt.edu
  export PKG_PATH=http://$BSD_MIRROR/pub/OpenBSD/5.1/packages/`machine -a`/

Then bootstrap the project::

  pkg_add -i git gmake
  git clone git@github.com:dreamhost/akanda.git

Finally, get the rest of the deps::

  cd akanda
  gmake install-dev


Building a FreeBSD Dev Environment
----------------------------------

Get ports installed::

  portsnap fetch
  portsnap extract

When asked to enable PTH for multiprocessing support say "NO"!

Then, continue::

  cd /usr/ports/devel/git && make install clean
  mkdir -p $BASE_DIR && cd $BASE_DIR
  git clone git@github.com:dreamhost/akanda.git

Finally, get the rest of the deps::

  cd akanda
  make install-dev


The Akanda REST API
===================

The discussion below assums that all actions will take place at the top-level
of the check-out directory.


The Service Plugin
------------------

The plugin is in the ``twisted/plugins`` directory. Note that the string value
of service module in the plugin file enables one to define the service before
the service module in question is present in the Python namespace.

The filename of the plugin has no impact on usage; the plugin name is given as
a string value in the service definition in the plugin file.

You can get a complete list of plugins via::

  $ twistd --help

You can get a list of options particular to this plugin via::

  $ twistd akanda --help

You start the service in the foreground using the twistd command line tool::

  $ twistd -n akanda

Or, you can run it as a daemon with::

  $ twistd akanda

Once the service is up and running, you can test it via a web browser by
accessing the following URLs:

* http://localhost:9999/json/v1/
* http://localhost:9999/json/v1/demo
* http://localhost:9999/json/v1/meta/version


Adding New API Classes/Methods
------------------------------

Edit ``akanda/api/v1.py`` or ``v2.py``.


Mapping URLs to Objects
-----------------------

The akanda plugin uses txroutes, which in turn uses the Routes package. All
rules are defined ``akanda/api/routes.py``.


Thinking in REST
----------------

General guidelines for API development are given in the
``akanda/api/v1.py`` and ``akanda/api/routes.py`` files.

The Horizon Plugin
==================

Installing Akanda Support in Horizon
------------------------------------

TBD

Viewing Akanda in Horizon
-------------------------

TBD
