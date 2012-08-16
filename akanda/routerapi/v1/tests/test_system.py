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

    @patch.object(IFManager, 'get_interfaces', FakeIFManager.fake_get_interfaces)
    def test_get_interfaces(self):
        result = self.test_app.get('/v1/system/interfaces')
        expected = payload.sample_system_interfaces
        self.assertEqual(result.data, expected)
