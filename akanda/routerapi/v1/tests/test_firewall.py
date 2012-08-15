"""
Base classes for Router API tests.
"""
import flask

from akanda.routerapi import v1
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
        return ('pass all flags S/SA block drop in on ! lo0 proto tcp from '
                'any to any port 6000:6010')

class FirewallAPITestCase(UnitTestCase):
    """
    """
    def setUp(self):
        self.app = flask.Flask('firewall_test')
        self.app.register_blueprint(v1.firewall.firewall)
        self.test_app = self.app.test_client()

    # XXX decorate with patch.object
    def test_rules(self):
        rv = self.test_app.get('/v1/firewall/rules')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    # XXX decorate with patch.object
    def test_states(self):
        rv = self.test_app.get('/v1/firewall/states')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    # XXX decorate with patch.object
    def test_anchors(self):
        rv = self.test_app.get('/v1/firewall/anchors')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    # XXX decorate with patch.object
    def test_sources(self):
        rv = self.test_app.get('/v1/firewall/sources')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    # XXX decorate with patch.object
    def test_info(self):
        rv = self.test_app.get('/v1/firewall/info')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    # XXX decorate with patch.object
    def test_tables(self):
        rv = self.test_app.get('/v1/firewall/tables')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    # XXX decorate with patch.object
    def test_labels(self):
        rv = self.test_app.get('/v1/firewall/labels')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    # XXX decorate with patch.object
    def test_timeouts(self):
        rv = self.test_app.get('/v1/firewall/timeouts')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    # XXX decorate with patch.object
    def test_memory(self):
        rv = self.test_app.get('/v1/firewall/memory')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data
