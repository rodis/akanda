"""
Base classes for Router API tests.
"""
import flask
from mock import patch

from akanda.routerapi import v1
from akanda.routerapi.drivers.pf import PfManager
from akanda.testing.fakes.routerapi import FakePfManager
from akanda.testing.payloads import routerapi_firewall as payload
from akanda.testing.testcase import UnitTestCase


class FirewallAPITestCase(UnitTestCase):
    """
    """
    def setUp(self):
        self.app = flask.Flask('firewall_test')
        self.app.register_blueprint(v1.firewall.firewall)
        self.test_app = self.app.test_client()

    @patch.object(PfManager, 'get_rules', FakePfManager.fake_get_rules)
    def test_get_rules(self):
        result = self.test_app.get('/v1/firewall/rules').data.strip()
        expected = payload.sample_pfctl_sr.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_states', FakePfManager.fake_get_states)
    def test_get_states(self):
        result = self.test_app.get('/v1/firewall/states').data.strip()
        expected = payload.sample_pfctl_ss.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_anchors', FakePfManager.fake_get_anchors)
    def test_get_anchors(self):
        result = self.test_app.get('/v1/firewall/anchors').data.strip()
        expected = payload.sample_pfctl_sA.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_sources', FakePfManager.fake_get_sources)
    def test_get_sources(self):
        result = self.test_app.get('/v1/firewall/sources').data.strip()
        expected = payload.sample_pfctl_sS.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_info', FakePfManager.fake_get_info)
    def test_get_info(self):
        result = self.test_app.get('/v1/firewall/info').data.strip()
        expected = payload.sample_pfctl_si.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_timeouts', FakePfManager.fake_get_timeouts)
    def test_get_timeouts(self):
        result = self.test_app.get('/v1/firewall/timeouts').data.strip()
        expected = payload.sample_pfctl_st.strip()
        self.assertEqual(result, expected)

    # XXX decorate with patch.object
    def test_get_labels(self):
        result = self.test_app.get('/v1/firewall/labels').data.strip()

    # XXX decorate with patch.object
    def test_get_tables(self):
        result = self.test_app.get('/v1/firewall/tables').data.strip()

    @patch.object(PfManager, 'get_memory', FakePfManager.fake_get_memory)
    def test_get_memory(self):
        result = self.test_app.get('/v1/firewall/memory').data.strip()
        expected = payload.sample_pfctl_sm.strip()
        self.assertEqual(result, expected)
