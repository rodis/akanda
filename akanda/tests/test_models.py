import unittest

from akanda import models


class ModelsTestCase(unittest.TestCase):
    """
    """
    def test_ifname(self):
        iface = models.Interface(ifname="em0")
        self.assertEquals(iface.ifname, "em0")