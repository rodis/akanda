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

    @classmethod
    def fake_get_states(self):
        return ('all tcp 192.168.229.129:22 <- 192.168.229.1:52130'
                '       ESTABLISHED:ESTABLISHED\n'
                'all udp 192.168.229.255:17500 <- 192.168.229.1:17500'
                '       NO_TRAFFIC:SINGLE\n'
                'all udp 172.16.5.255:17500 <- 172.16.5.1:17500'
                '       NO_TRAFFIC:SINGLE')

    @classmethod
    def fake_get_anchors(self):
        pass

    @classmethod
    def fake_get_sources(self):
        pass

    @classmethod
    def fake_get_info(self):
        return(
            """
            Status: Enabled for 0 days 01:57:48              Debug: err\n

            State Table                          Total             Rate\n
              current entries                        4
              searches                            5638            0.8/s\n
              inserts                               86            0.0/s\n
              removals                              82            0.0/s\n
            Counters\n
              match                                 86            0.0/s\n
              bad-offset                             0            0.0/s\n
              fragment                               0            0.0/s\n
              short                                  0            0.0/s\n
              normalize                              0            0.0/s\n
              memory                                 0            0.0/s\n
              bad-timestamp                          0            0.0/s\n
              congestion                             0            0.0/s\n
              ip-option                              0            0.0/s\n
              proto-cksum                            0            0.0/s\n
              state-mismatch                         0            0.0/s\n
              state-insert                           0            0.0/s\n
              state-limit                            0            0.0/s\n
              src-limit                              0            0.0/s\n
              synproxy                               0            0.0/s
            """)

    @classmethod
    def fake_get_tables(self):
        return ('tcp.first                   120s\n'
                'tcp.opening                  30s\n'
                'tcp.established           86400s\n'
                'tcp.closing                 900s\n'
                'tcp.finwait                  45s\n'
                'tcp.closed                   90s\n'
                'tcp.tsdiff                   30s\n'
                'udp.first                    60s\n'
                'udp.single                   30s\n'
                'udp.multiple                 60s\n'
                'icmp.first                   20s\n'
                'icmp.error                   10s\n'
                'other.first                  60s\n'
                'other.single                 30s\n'
                'other.multiple               60s\n'
                'frag                         30s\n'
                'interval                     10s\n'
                'adaptive.start             6000 states\n'
                'adaptive.end              12000 states\n'
                'src.track                     0s')

    @classmethod
    def fake_get_labels(self):
        pass

    @classmethod
    def fake_get_timeouts(self):
        pass

    @classmethod
    def fake_get_memory(self):
        return ('states        hard limit    10000\n'
                'src-nodes     hard limit    10000\n'
                'frags         hard limit     5000\n'
                'tables        hard limit     1000\n'
                'table-entries hard limit   200000')



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

    @patch.object(PfManager, 'get_states', FakePfManager.fake_get_states)
    def test_get_states(self):
        result = self.test_app.get('/v1/firewall/states')
        expected = payloads.sample_pfctl_ss.strip('\n')
        self.assertEqual(result.data, expected)

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

    @patch.object(PfManager, 'get_info', FakePfManager.fake_get_info)
    def test_get_info(self):
        result = self.test_app.get('/v1/firewall/info')
        expected = payloads.sample_pfctl_si.strip()
        self.assertEqual(result.data, expected)

    @patch.object(PfManager, 'get_tables', FakePfManager.fake_get_tables)
    def test_get_tables(self):
        result = self.test_app.get('/v1/firewall/tables')
        expected = payloads.sample_pfctl_st.strip()
        self.assertEqual(result.data, expected)

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

    @patch.object(PfManager, 'get_memory', FakePfManager.fake_get_memory)
    def test_get_memory(self):
        result = self.test_app.get('/v1/firewall/memory')
        expected = payloads.sample_pfctl_sm.strip()
        self.assertEqual(result.data, expected)
