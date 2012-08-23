~~~~~~
akanda
~~~~~~

An open source packet filter solution for `OpenStack`_ deployments.

----

.. contents:: **Links to Document Sections**
   :local:

About
=====


The Code
--------

The code for this project contains the following:

* a set of APIs that manipulate PF (in-progress)

* a service-facing REST server for controlling PF (in-progress)

* a user-facing REST server that passes requests to a user's Akanda instance
  and that instance's REST server (forth-coming)

* a GUI for integrating Akanda into OpenStack `Horizon`_

* a set of tools/scripts for developing Akanda and building Akanda images

In the future, this will be extended to make use of the IOCTL interface for
controlling PF and a Python library for manipulating it.

The Product
-----------

Akanda "the product" is this code bundled into an OpenBSD .iso image. The make
file provides a target for building your own image.

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

Setting up a Linux/Mac OS X Dev Environment
-------------------------------------------

Get the source code::

  $ git clone git@github.com:dreamhost/akanda.git
  $ cd akanda

Set up a virtualenv for Python, to avoid any conflicts or inconsistencies::

  $ make setup-venv
  $ . .venv/bin/activate

Akanda works with Python 2.6, so feel free to substitute the version number
above, if you have such a requirement.

Finally, get the rest of the deps::

  $ (.venv) make python-deps

Run the unit tests to make sure that everything is okay::

  $ (.venv) make check

If you are writing code and want to keep tabs on your pep8 violations, code
flakes, and coverage::

  $ (.venv) make check-dev

Setting up an OpenBSD Dev Environment
-------------------------------------

Set up your packge URL, e.g.::

  $ export BSD_MIRROR=mirror.ece.vt.edu
  $ export PKG_PATH=http://$BSD_MIRROR/pub/OpenBSD/5.1/packages/`machine -a`/

Then bootstrap the project::

  $ pkg_add -i git gmake

  $ git clone git@github.com:dreamhost/akanda.git
  $ cd akanda

Set up a virtualenv for Python, to avoid any conflicts or inconsistencies::

  $ gmake setup-venv
  $ . .venv/bin/activate

Akanda works with Python 2.6, so feel free to substitute the version number
above, if you have such a requirement.

Or, for OpenBSD::

  $ (.venv) gmake install-dev


Building an Akanda ISO
======================

Akanda is intended to be used in OpenStack deployments, uploaded to `Glance`_
as an ``.iso`` image. OpenStack deployments can then spin up Akanda router
instances to manage the Layer 3 features supported by Akanda.

At this time, building an ISO requires an OpenBSD system. Future iterations
will potentially use other mechanisms.

To build an .iso image:

#. ssh into your OpenBSD dev server or VM instance

#. ``cd akanda`` (the git clone dir)

#. ``gmake iso`` This script will invoke the download of OpenBSD base and
   eventually drop into a chroot jail environment.

#. Follow the instructions highlighted in the chroot login screen.

#. Type 'exit' when complete to build the .iso image.

The ``.iso`` image (Ramdisk) requires at least 512mb of RAM to run. The current
``.iso`` should be around around 384mb with base packages required to run
Akanda.  The booted ``.iso`` should contain akanda under /var/akanda.

The Akanda REST APIs
====================

Akanda comes with two REST APIs:

#. The REST API that runs on the router instance itself, recieving simple
   pf-related administrative commands (e.g., "take this data and have pf parse
   it"). This REST API runs only so long a router instance is up and running.
   This is not the user-facing, 24/7 REST API.

#. Then there is the user-facing, 24/7, load-balanced REST API :-) This is what
   users will be able to interact with in order to programmatically manage
   their router instances (e.g., set NAT, port-forwarding, and basic firewall
   rules). This API is exposed as Quantum extensions.

The Router-Instance REST API
----------------------------

This section assumes that all provided commands will be executed at the
top-level of the check-out directory.

TBD

The User-Facing REST API
------------------------

This API will be created using the standard REST service tools that come with
OpenStack. Current implementation will use Quantum extensions.

Adding New API Classes/Methods
------------------------------

For the Router-instance API, edit ``akanda/api/v1.py`` or ``v2.py``.

For the User-facing API, edit ``TBD``.


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

Be sure to have Akanda installed on the system that will be running Akanda::

  $ make install

[more info soon on deploying the Akanda Horizon plugin]

Viewing Akanda in Horizon
-------------------------

TBD

.. Links/References
.. _OpenStack: http://www.openstack.org/
.. _Horizon: http://docs.openstack.org/developer/horizon/
.. _PF: http://www.openbsd.org/faq/pf/
.. _Glance: http://docs.openstack.org/developer/glance/
