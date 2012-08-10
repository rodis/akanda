
"""Base classes for Router API tests.
"""
import json
import logging
import unittest

import flask

import mock

from akanda import models
from akanda.routerapi import v1


LOG = logging.getLogger(__name__)


class ClientTestCase(unittest.TestCase):
    """
    This test case contains the unit tests for the REST API specification. In
    particular, it tests example payloads made via client requests.
    """
    def test_root(self):
        pass

    def test_system_interface(self):
        pass

    def test_system_interfaces(self):
        pass


class ServerTestCase(unittest.TestCase):
    """
    This test case contains the unit tests for the Python server implementation 
    of the Router API. The focus of these tests is to ensure that the server is 
    behaving appropriately.
    """
    def setUp(self):
        self.if_mock_patch = mock.patch(
            'akanda.routerapi.drivers.ifconfig.InterfaceManager')
        self.if_mock = self.if_mock_patch.start()
        self.app = flask.Flask('test')
        self.app.register_blueprint(v1.blueprint, url_prefix="/v1")
        self.test_app = self.app.test_client()

    def tearDown(self):
        self.if_mock_patch.stop()

    def test_root(self):
        rv = self.test_app.get('/v1/')
        expected = "Welcome to the Akanda appliance"
        self.assertEqual(rv.data, expected)

    def test_system_interface(self):
            self.if_mock.get_interface.return_value = models.Interface(
                ifname='ge1')
            rv = self.test_app.get('/v1/system/interface/ge1')
            try:
                data = json.loads(rv.data)
                #data = rv.data
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
