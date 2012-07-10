from twisted.application import internet
from twisted.python import usage
from twisted.web import server

from akanda.routerapi import api


class Options(usage.Options):
    """
    """
    optParameters = [
        ["port", "p", "9999", "The port to run the REST service on."]]


def makeService(options):
    """
    """
    port = int(options.get("port"))
    service = internet.TCPServer(port, server.Site(api))
    service.setName("Akanda REST Service")
    return service
