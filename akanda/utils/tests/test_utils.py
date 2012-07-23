import json
import unittest

from akanda import utils


class ModelSerializerTestCase(unittest.TestCase):
    """
    """
    def test_default(self):
        data = {
            "a": [1, 2, 3],
            "b": {"c": 4},
            "d": "e",
            "f": u"g",
            "h": 42,
            "i": 3.14159,
            "j": False,
            "k": None,
            "l": (4, 5, 6),
            "m": 12345671238792347L,
            }
        expected = (
            '{"a": [1, 2, 3], "b": {"c": 4}, "d": "e", "f": "g", '
            '"i": 3.14159, "h": 42, "k": null, "j": false, '
            '"m": 12345671238792347, "l": [4, 5, 6]}')
        serialized = json.dumps(data, cls=utils.ModelSerializer)
        self.assertEqual(serialized, expected)

    def test_default_with_set(self):
        data = {"a": set([1, 2, 3])}
        expected = '{"a": [1, 2, 3]}'
        serialized = json.dumps(data, cls=utils.ModelSerializer)
        self.assertEqual(serialized, expected)
