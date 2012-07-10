import json, os

from twisted.internet import utils
from twisted.python import log
from twisted.web import resource, server

from txroutes import Dispatcher

from akanda import meta
from akanda.routerapi import base


# For info on how to run long-running processes (e.g., use deferreds) see the
# examples here:
#   https://github.com/dreamhost/txroutes


# Thoughts that should guide REST implementations:
#
#   For collections (e.g., /json/v1/firewall/groups):
#       GET - list the details of the groups
#       PUT - replace the current groups data entirely with new groups data
#       POST - create a new group in the groups collection
#       DELETE - delete the entire collection
#
#   For elements (e.g., /json/v1/firewall/{name}/rule/{rule-number}):
#       GET - retreive rule data for the given firewall rule
#       PUT - replace the given firewall rule with a new one
#       DELETE - delete the given firewall rule
#
#   For elements (e.g., /json/v1/firewall/{name}/rule/):
#       POST - create a new firewall rule
#
# Also, be sure to look at akanda.api.routes (both code and comments), as
# this provides useful information on how the API methods below will be used.


class Demo(base.RESTAPIBase):
    """
    """
    def longRunningProcess(self, request):

        # XXX generalized forms of these can be created and then moved out to
        # the top-level class (at which point the request object will no longer
        # be in-scope, so you'll need to pass it when calling the
        # callbacks or errbacks).
        def yay(result):
            stdout, stderr, exitCode = result
            if exitCode == 0:
                log.msg(result)
                request.write(json.dumps({"date": stdout.strip()}))
            else:
                log.err(result)
                request.write("Error! See the log for more details.")
            request.finish()

        def uhoh(failure):
            log.err(failure)
            request.write("Error! See the log for more details.")
            request.finish()

        #cmd = "/bin/ls"
        cmd = "/bin/date"
        args = []#["/Users/oubiwann/*"]
        deferred = utils.getProcessOutputAndValue(
            cmd, args, env=os.environ)
        deferred.addCallback(yay)
        deferred.addErrback(uhoh)
        return server.NOT_DONE_YET


class Configuration(base.RESTAPIBase):
    """
    """


class Firewall(base.RESTAPIBase):
    """
    """


class NAT(base.RESTAPIBase):
    """
    """


class VPN(base.RESTAPIBase):
    """
    """


class Metadata(base.RESTAPIBase):
    """
    """
    # XXX create a json.dumps decorator for json-returning methods
    def version(self, request):
        major, minor, point = meta.version.split(".")
        return json.dumps({"version": {
            "major": 0,
            "minor": 1,
            "point": 0}})


class API(base.RESTAPIBase):
    """
    """
    demo = Demo()
    config = Configuration()
    firewall = Firewall()
    nat = NAT()
    vpn = VPN()
    meta = Metadata()

    # XXX create a json.dumps decorator for json-returning methods
    def index(self, request):
        """
        This is really nothing more than a demo of what can be done and to
        provide some initial data with which we can test a running instance of
        the REST service.
        """
        return json.dumps({
            "class name": self.__class__.__name__,
            "class methods": dir(self),
            "class data": vars(self),
            })
