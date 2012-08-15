"""
Base classes for System Router API tests.
"""
import flask
from mock import patch

from akanda import models
from akanda.routerapi import v1
from akanda.routerapi.drivers.ifconfig import InterfaceManager as IFManager
from akanda.routerapi.tests import payloads
from akanda.testing.testcase import UnitTestCase


class FakeIFManager(object):
    """
    The methods implemented here in the fake interface manager should not be
    built using the payloads, since that's what we're using to verify the data.
    Instead, each method should create akanda objects as needed that will
    serialize to the appropriate data to return the proper payload.
    """
    @classmethod
    def fake_get_interface(cls, ifname):
        return models.Interface(
            media="Ethernet autoselect (1000baseT full-duplex,master)",
            state="up",
            ifname="ge1",
            groups="egress",
            lladdr="00:0c:29:e8:f9:2e",
            addresses=["fe80::20c:29ff:fee8:f92e/64", "192.168.229.129/24"])

    @classmethod
    def fake_get_interfaces(cls):
        # XXX this needs to be updated to return a list of interface objects.
        interfaces = [models.Interface(media="null", state="down", ifname="ge0",
                                       groups="enc", lladdr="null", addresses=[]),

                      models.Interface(media="Ethernet autoselect (1000baseT full-duplex,master)",
                                       state="up", ifname="ge1", groups="egress",
                                       lladdr="00:0c:29:e8:f9:2e", 
                                       addresses=["fe80::20c:29ff:fee8:f92e/64", "192.168.229.129/24"]),

                      models.Interface(media="Ethernet autoselect (1000baseT full-duplex,master)",
                                       state="up", ifname="ge2", groups= [], lladdr="00:0c:29:e8:f9:38",
                                       addresses=["192.168.57.101/24", "fe80::20c:29ff:fee8:f938/64"]) ]
        return interfaces


class SystemAPITestCase(UnitTestCase):
    """
    This test case contains the unit tests for the Python server implementation
    of the Router API. The focus of these tests is to ensure that the server is
    behaving appropriately.
    """
    def setUp(self):
        self.app = flask.Flask('system_test')
        self.app.register_blueprint(v1.system.system)
        self.test_app = self.app.test_client()

    @patch.object(IFManager, 'get_interface', FakeIFManager.fake_get_interface)
    def test_get_interface(self):
        rv = self.test_app.get('/v1/system/interface/ge1')
        expected = payloads.sample_system_interface
        self.assertEqual(rv.data, expected)

    # XXX add a patch decorator here
    @patch.object(IFManager, 'get_interfaces', FakeIFManager.fake_get_interfaces)
    def test_get_interfaces(self):
        rv = self.test_app.get('/v1/system/interfaces')
        expected = payloads.sample_system_interfaces
        self.assertEqual(rv.data, expected)
