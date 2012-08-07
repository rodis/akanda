import json

from akanda.routerapi import base


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


class API(base.RESTAPIBase):
    """
    """
    firewall = Firewall()
    nat = NAT()
    vpn = VPN()
    meta = Metadata()

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
