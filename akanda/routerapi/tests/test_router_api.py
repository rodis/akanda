
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
            data = json.loads(rv.data)
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_system_interface(self):
        rv = self.test_app.get('/v1/system/interface/ge1')
        try:
            data = json.loads(rv.data)
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_firewall_rules(self):
        rv = self.test_app.get('/v1/firewall/rules')
        try:
            #data = json.loads(rv.data)
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data
