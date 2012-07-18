import unittest

from akanda import models


class ModelsTestCase(unittest.TestCase):
    """
    """
    def test_ifname(self):
        iface = models.Interface(ifname="em0")
        self.assertEquals(iface.ifname, "em0")
        
    def test_to_dict(self):
        iface = models.Interface()
        result = iface.to_dict()
        expected = [
            '_addresses', '_description', '_primary_v4', 'extra_params',
            'flags', 'groups', 'ifname', 'media', 'mtu']
        self.assertTrue(isinstance(result, dict))
        self.assertEquals(sorted(result.keys()), expected)