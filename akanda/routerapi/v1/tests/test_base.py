"""
Base classes for Router API tests.
"""
import json
import logging
import unittest

import flask
from mock import patch

from akanda import models
from akanda.routerapi import v1
from akanda.routerapi.drivers.ifconfig import InterfaceManager as IFManager
from akanda.routerapi.tests import payloads


class BaseTestCase(unittest.TestCase):
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
        expected = payloads.sample_root
        self.assertEqual(rv.data, expected)
