"""
Base classes for Router API tests.
"""
import flask
from mock import patch

from akanda.routerapi import v1
from akanda.routerapi.drivers.pf import PfManager
from akanda.testing.fakes.routerapi import FakePfManager
from akanda.testing.payloads import routerapi_firewall as payload
from akanda.testing.testcase import UnitTestCase



class FakePfManager(object):
    """
    The methods implemented here in the fake PF manager should not be
    built using the payloads, since that's what we're using to verify the data.
    Instead, each method should create akanda objects as needed that will
    serialize to the appropriate data to return the proper payload.

    However, since for version 1 we are simply presenting the actual textual
    results of the commands and not converting them to models, we just do
    straight-up text here.
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
        return("""
Status: Enabled for 0 days 01:57:48              Debug: err

State Table                          Total             Rate
  current entries                        4
  searches                            5638            0.8/s
  inserts                               86            0.0/s
  removals                              82            0.0/s
Counters
  match                                 86            0.0/s
  bad-offset                             0            0.0/s
  fragment                               0            0.0/s
  short                                  0            0.0/s
  normalize                              0            0.0/s
  memory                                 0            0.0/s
  bad-timestamp                          0            0.0/s
  congestion                             0            0.0/s
  ip-option                              0            0.0/s
  proto-cksum                            0            0.0/s
  state-mismatch                         0            0.0/s
  state-insert                           0            0.0/s
  state-limit                            0            0.0/s
  src-limit                              0            0.0/s
  synproxy                               0            0.0/s
""")

    @classmethod
    def fake_get_tables(self):
        return ("""
tcp.first                   120s
tcp.opening                  30s
tcp.established           86400s
tcp.closing                 900s
tcp.finwait                  45s
tcp.closed                   90s
tcp.tsdiff                   30s
udp.first                    60s
udp.single                   30s
udp.multiple                 60s
icmp.first                   20s
icmp.error                   10s
other.first                  60s
other.single                 30s
other.multiple               60s
frag                         30s
interval                     10s
adaptive.start             6000 states
adaptive.end              12000 states
src.track                     0s
""")

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
        result = self.test_app.get('/v1/firewall/rules').data.strip()
        expected = payload.sample_pfctl_sr.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_states', FakePfManager.fake_get_states)
    def test_get_states(self):
        result = self.test_app.get('/v1/firewall/states').data.strip()
        expected = payload.sample_pfctl_ss.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_anchors', FakePfManager.fake_get_anchors)
    def test_get_anchors(self):
        result = self.test_app.get('/v1/firewall/anchors').data.strip()
        expected = payload.sample_pfctl_sA.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_sources', FakePfManager.fake_get_sources)
    def test_get_sources(self):
        result = self.test_app.get('/v1/firewall/sources').data.strip()
        expected = payload.sample_pfctl_sS.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_info', FakePfManager.fake_get_info)
    def test_get_info(self):
        result = self.test_app.get('/v1/firewall/info').data.strip()
        expected = payload.sample_pfctl_si.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_timeouts', FakePfManager.fake_get_timeouts)
    def test_get_timeouts(self):
        result = self.test_app.get('/v1/firewall/timeouts').data.strip()
        expected = payload.sample_pfctl_st.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_labels', FakePfManager.fake_get_labels)
    def test_get_labels(self):
        result = self.test_app.get('/v1/firewall/labels').data.strip()
        expected = payload.sample_pfctl_sl.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_tables', FakePfManager.fake_get_tables)
    def test_get_tables(self):
        result = self.test_app.get('/v1/firewall/tables').data.strip()
        expected = payload.sample_pfctl_sT.strip()
        self.assertEqual(result, expected)

    @patch.object(PfManager, 'get_memory', FakePfManager.fake_get_memory)
    def test_get_memory(self):
        result = self.test_app.get('/v1/firewall/memory').data.strip()
        expected = payload.sample_pfctl_sm.strip()
        self.assertEqual(result, expected)
