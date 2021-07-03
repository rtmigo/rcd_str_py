import unittest

from rcd_str import wildFullMatch


class TestWild(unittest.TestCase):
    def test_wildMatch(self):
        self.assertTrue(
            wildFullMatch("эники беники ели вареники", "эники* ели вареники"))
        self.assertFalse(wildFullMatch("хреники эники беники ели вареники",
                                       "эники* ели вареники"))
        self.assertFalse(
            wildFullMatch("хреники беники ели вареники", "эники* ели вареники"))
        self.assertFalse(wildFullMatch("эники беники ели вареники и драники",
                                       "эники* ели вареники"))