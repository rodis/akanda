"""
Base classes for Router API tests.
"""
import flask
from mock import patch

from akanda.routerapi import v1
from akanda.routerapi.drivers.pf import PfManager
from akanda.routerapi.tests import payloads
from akanda.testing.testcase import UnitTestCase


class FakePfManager(object):
    """
    The methods implemented here in the fake PF manager should not be
    built using the payloads, since that's what we're using to verify the data.
    Instead, each method should create akanda objects as needed that will
    serialize to the appropriate data to return the proper payload.
    """
    @classmethod
    def fake_get_rules(self):
        return ('pass all flags S/SA\n'
                'block drop in on ! lo0 proto tcp from '
                'any to any port 6000:6010')


class FirewallAPITestCase(UnitTestCase):
    """
    """
    def setUp(self):
        self.app = flask.Flask('firewall_test')
        self.app.register_blueprint(v1.firewall.firewall)
        self.test_app = self.app.test_client()

    @patch.object(PfManager, 'get_rules', FakePfManager.fake_get_rules)
    def test_get_rules(self):
        result = self.test_app.get('/v1/firewall/rules')
        expected = payloads.sample_pfctl_sr.strip()
        self.assertEqual(result.data, expected)

    # XXX decorate with patch.object
    def test_states(self):
        result = self.test_app.get('/v1/firewall/states')
        try:
            data = result.data
        except ValueError:
            print 'RAW DATA:', result
            raise
        return data

    # XXX decorate with patch.object
    def test_anchors(self):
        result = self.test_app.get('/v1/firewall/anchors')
        try:
            data = result.data
        except ValueError:
            print 'RAW DATA:', result
            raise
        return data

    # XXX decorate with patch.object
    def test_sources(self):
        result = self.test_app.get('/v1/firewall/sources')
        try:
            data = result.data
        except ValueError:
            print 'RAW DATA:', result
            raise
        return data

    # XXX decorate with patch.object
    def test_info(self):
        result = self.test_app.get('/v1/firewall/info')
        try:
            data = result.data
        except ValueError:
            print 'RAW DATA:', result
            raise
        return data

    # XXX decorate with patch.object
    def test_tables(self):
        result = self.test_app.get('/v1/firewall/tables')
        try:
            data = result.data
        except ValueError:
            print 'RAW DATA:', result
            raise
        return data

    # XXX decorate with patch.object
    def test_labels(self):
        result = self.test_app.get('/v1/firewall/labels')
        try:
            data = result.data
        except ValueError:
            print 'RAW DATA:', result
            raise
        return data

    # XXX decorate with patch.object
    def test_timeouts(self):
        result = self.test_app.get('/v1/firewall/timeouts')
        try:
            data = result.data
        except ValueError:
            print 'RAW DATA:', result
            raise
        return data

    # XXX decorate with patch.object
    def test_memory(self):
        result = self.test_app.get('/v1/firewall/memory')
        try:
            data = result.data
        except ValueError:
            print 'RAW DATA:', result
            raise
        return data
