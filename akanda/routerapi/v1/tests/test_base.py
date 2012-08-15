"""
Base classes for Router API tests.
"""
import flask

from akanda.routerapi import v1
from akanda.testing.payloads import routerapi_system as payload
from akanda.testing.testcase import UnitTestCase


class BaseAPITestCase(UnitTestCase):
    """
    This test case contains the unit tests for the Python server implementation
    of the Router API. The focus of these tests is to ensure that the server is
    behaving appropriately.
    """
    def setUp(self):
        self.app = flask.Flask('base_test')
        self.app.register_blueprint(v1.base.base)
        self.test_app = self.app.test_client()

    def test_root(self):
        rv = self.test_app.get('/v1/base', follow_redirects=True)
        expected = payload.sample_root
        self.assertEqual(rv.data, expected)
