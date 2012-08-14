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


class FakeIFManager(object):
    """
    The methods implemented here in the fake interface manager should not be
    built using the payloads, since that's what we're using to verify the data.
    Instead, each method should create akanda objects as needed that will
    serialize to the appropriate data to return the proper payload.
    """
    @classmethod
    def fake_get_interface(cls, ifname):
        return models.Interface(
            media="Ethernet autoselect (1000baseT full-duplex,master)",
            state="up",
            ifname="ge1",
            groups="egress",
            lladdr="00:0c:29:e8:f9:2e",
            addresses=["fe80::20c:29ff:fee8:f92e/64", "192.168.229.129/24"])

    @classmethod
    def fake_get_interfaces(cls):
        # XXX this needs to be updated to return a list of interface objects.
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

    @patch.object(IFManager, 'get_interface', FakeIFManager.fake_get_interface)
    def test_get_interface(self):
        rv = self.test_app.get('/v1/system/interface/ge1')
        expected = payloads.sample_system_interface
        self.assertEqual(rv.data, expected)

    # XXX add a patch decorator here
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
