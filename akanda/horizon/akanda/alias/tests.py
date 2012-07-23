from horizon import test


class AliasTests(test.TestCase):
    # Unit tests for alias.
    def test_me(self):
        self.assertTrue(1 + 1 == 2)
