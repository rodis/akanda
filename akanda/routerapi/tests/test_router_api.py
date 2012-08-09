
"""Base classes for Router API tests.
"""

import json
import unittest
import logging
import flask

from akanda.routerapi import v1

LOG = logging.getLogger(__name__)


class TestRouterAPI(unittest.TestCase):

    def setUp(self):
        super(TestRouterAPI, self).setUp()
        self.app = flask.Flask('test')
        self.app.register_blueprint(v1.blueprint)
        self.test_app = self.app.test_client()

        @self.app.before_request
        def attach_config():
            '''
               Add any config if needed
            '''
            pass

    def tearDown(self):
        pass

    def test_root(self):
        rv = self.test_app.get('/v1/')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_system_interfaces(self):
        rv = self.test_app.get('/v1/system/interfaces')
        try:
            #data = json.loads(rv.data)
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_system_interface(self):
        rv = self.test_app.get('/v1/system/interface/ge1')
        try:
            #data = json.loads(rv.data)
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_rules(self):
        rv = self.test_app.get('/v1/firewall/rules')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_states(self):
        rv = self.test_app.get('/v1/firewall/states')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_anchors(self):
        rv = self.test_app.get('/v1/firewall/anchors')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_sources(self):
        rv = self.test_app.get('/v1/firewall/sources')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_info(self):
        rv = self.test_app.get('/v1/firewall/info')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_tables(self):
        rv = self.test_app.get('/v1/firewall/tables')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_labels(self):
        rv = self.test_app.get('/v1/firewall/labels')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_timeouts(self):
        rv = self.test_app.get('/v1/firewall/timeouts')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_memory(self):
        rv = self.test_app.get('/v1/firewall/memory')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data
