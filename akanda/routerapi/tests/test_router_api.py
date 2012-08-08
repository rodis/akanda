
"""Base classes for Router API tests.
"""

import json
import logging
import unittest

import flask

from akanda.routerapi import v1

LOG = logging.getLogger(__name__)


class TestBase(unittest.TestCase):

    def setUp(self):
        super(TestBase, self).setUp()
        self.app = flask.Flask('test')
        self.app.register_blueprint(v1.blueprint)
        self.test_app = self.app.test_client()

        @self.app.before_request
        def attach_storage_connection():
            pass

    def tearDown(self):
        pass

    def get(self, path):
        rv = self.test_app.get(path)
        try:
            data = json.loads(rv.data)
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data
