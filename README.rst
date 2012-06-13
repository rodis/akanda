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

* An Akanda instance up and running.

* The Akanda code installed


Installation
============

Building an OpenBSD Dev Environment
-----------------------------------

Set up your packge URL, e.g.::

  export BSD_MIRROR=mirror.ece.vt.edu
  export PKG_PATH=http://$BSD_MIRROR/pub/OpenBSD/5.1/packages/`machine -a`/

Then bootstrap the project::

  pkg_add -i git
  git clone ssh://git.newdream.net/dhc/akanda

Finally, get the rest of the deps::

  cd akanda
  make install-dev

Building a FreeBSD Dev Environment
----------------------------------

Get ports installed::

  portsnap fetch
  portsnap extract

When asked to enable PTH for multiprocessing support say "NO"! 

Then, continue::

  cd /usr/ports/devel/git && make install clean
  mkdir -p $BASE_DIR && cd $BASE_DIR
  git clone ssh://git.newdream.net/dhc/akanda

Finally, get the rest of the deps::

  cd akanda
  make install-dev
