from txroutes import Dispatcher

from akanda.routerapi import v1, v2


apiv1 = v1.API()
# XXX The next line is just a reminder to not lose track of the fact tht we
# will eventually need to make changes that are not compatible with what is
# currently deployed. As such, everything we do needs to ensure that future
# versions are first-class citizens in our API :-)
apiv2 = v2.API()


# XXX For information on the Dispatcher class, see:
#   https://github.com/dreamhost/txroutes
dispatcher = Dispatcher()
# Let's make an easy-to-type alias for connect (one that's also semantically
# correct, if you look at the Routes source code).
rule = dispatcher.connect


# XXX For information on Routes (used by txroutes), see:
#   http://routes.readthedocs.org/en/latest/setting_up.html
#   http://routes.readthedocs.org/en/latest/restful.html
#
# In particular, the restful.html link above defines a route mapping via the
# Routes API that produces a logical map like the following:
#
# GET    /messages        => messages.index()    => url("messages")
# POST   /messages        => messages.create()   => url("messages")
# GET    /messages/new    => messages.new()      => url("new_message")
# PUT    /messages/1      => messages.update(id) => url("message", id=1)
# DELETE /messages/1      => messages.delete(id) => url("message", id=1)
# GET    /messages/1      => messages.show(id)   => url("message", id=1)
# GET    /messages/1/edit => messages.edit(id)   => url("edit_message", id=1)
#
# We should create a document that defines something similar for our Firewall,
# VPN, NAT, Config, etc., API components. Once we have a definition like this,
# we can work it backwards to see what our Routes connect ("rule", below)
# method calls/parameters will look like.


# Version 1
rule("index", "/json/v1", controller=apiv1, action="index")
rule("demo", "/json/v1/demo", controller=apiv1.demo,
     action="longRunningProcess")
rule("version", "/json/v1/meta/version", controller=apiv1.meta,
     action="version")
rule("system", "/json/v1/system/get_interface", controller=apiv1.system,
     action="get_interface")
rule("system", "/json/v1/system/get_interfaces", controller=apiv1.system,
     action="get_interfaces")


# Version 2
rule("index", "/json/v2", controller=apiv2, action="index")
