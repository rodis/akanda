"""
Base classes for System Router API tests.
"""
import flask
from mock import patch

from akanda.routerapi import v1
from akanda.routerapi.drivers.ifconfig import InterfaceManager as IFManager
from akanda.testing.fakes.routerapi import FakeIFManager
from akanda.testing.payloads import routerapi_system as payload
from akanda.testing.testcase import UnitTestCase


<<<<<<< HEAD
<<<<<<< HEAD
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
        iface1 = models.Interface(
            media="null", state="down", ifname="ge0", groups="enc",
            lladdr="null", addresses=[])
        iface2 = models.Interface(
            media="Ethernet autoselect (1000baseT full-duplex,master)",
            state="up", ifname="ge1", groups="egress",
            lladdr="00:0c:29:e8:f9:2e",
            addresses=["fe80::20c:29ff:fee8:f92e/64", "192.168.229.129/24"])
        iface3 = models.Interface(
            media="Ethernet autoselect (1000baseT full-duplex,master)",
            state="up", ifname="ge2", groups=[],
            lladdr="00:0c:29:e8:f9:38",
            addresses=["192.168.57.101/24", "fe80::20c:29ff:fee8:f938/64"])
        return [iface1, iface2, iface3]


=======
>>>>>>> 12fe07e... Moved fake routerapi classes into testing.
=======
>>>>>>> ee95201270515cdb954593ee7239c8dae7d66b7d
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
        result = self.test_app.get('/v1/system/interface/ge1')
        expected = payload.sample_system_interface
        self.assertEqual(result.data, expected)

    @patch.object(
        IFManager, 'get_interfaces', FakeIFManager.fake_get_interfaces)
    def test_get_interfaces(self):
        result = self.test_app.get('/v1/system/interfaces')
        expected = payload.sample_system_interfaces
        self.assertEqual(result.data, expected)
