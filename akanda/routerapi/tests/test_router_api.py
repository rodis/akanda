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
from akanda.routerapi.drivers.ifconfig import InterfaceManager
from akanda.routerapi.tests import payloads


def fake_get_interface(self, ifname):
    iface_data = json.loads(payloads.sample_system_interface)
    return models.Interface.from_dict(iface_data)


def fake_get_interfaces(self):
    # XXX this needs to be updated to load the data as json, and return a list
    # of interface objects.
    return payloads.sample_system_interfaces


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


class SystemTestCase(unittest.TestCase):
    """
    This test case contains the unit tests for the Python server implementation
    of the Router API. The focus of these tests is to ensure that the server is
    behaving appropriately.
    """
    def setUp(self):
        self.app = flask.Flask('system_test')
        self.app.register_blueprint(v1.system.system)
        self.test_app = self.app.test_client()

    @patch.object(InterfaceManager, 'get_interface', fake_get_interface)
    def test_get_interface(self):
        rv = self.test_app.get('/v1/system/interface/ge1')
        import pdb;pdb.set_trace()
        expected = payloads.sample_system_interface
        self.assertEqual(rv.data, expected)

    def test_get_interfaces(self):
        rv = self.test_app.get('/v1/system/interfaces')
        expected = payloads.sample_system_interfaces
        self.assertEqual(rv.data, expected)


class FirewallTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        # XXX adjust mock for firewall usage
        self.if_mock_patch = mock.patch(
            'akanda.routerapi.drivers.ifconfig.InterfaceManager')
        self.if_mock = self.if_mock_patch.start()
        self.app = flask.Flask('firewall_test')
        self.app.register_blueprint(v1.firewall.firewall)
        self.test_app = self.app.test_client()

    def tearDown(self):
        self.if_mock_patch.stop()

    def test_rules(self):
        rv = self.test_app.get('/v1/firewall/rules')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_states(self):
        rv = self.test_app.get('/v1/firewall/states')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_anchors(self):
        rv = self.test_app.get('/v1/firewall/anchors')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_sources(self):
        rv = self.test_app.get('/v1/firewall/sources')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_info(self):
        rv = self.test_app.get('/v1/firewall/info')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_tables(self):
        rv = self.test_app.get('/v1/firewall/tables')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_labels(self):
        rv = self.test_app.get('/v1/firewall/labels')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_timeouts(self):
        rv = self.test_app.get('/v1/firewall/timeouts')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data

    def test_memory(self):
        rv = self.test_app.get('/v1/firewall/memory')
        try:
            data = rv.data
        except ValueError:
            print 'RAW DATA:', rv
            raise
        return data
