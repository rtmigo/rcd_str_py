import re
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from rcd_str import LazyRegex


class TestLazy(unittest.TestCase):

    def test_str(self):
        lr = LazyRegex("s.n", re.M)
        self.assertTrue(lr.compiled.match("sun"))
        self.assertTrue(lr.compiled.match("sin"))
        self.assertTrue(lr.compiled.match("son"))
        self.assertFalse(lr.compiled.match("win"))

    def test_path(self):
        with TemporaryDirectory() as tds:
            file = Path(tds) / "regex.txt"
            file.write_text(".ork")
            lr = LazyRegex(file, re.M)
            self.assertTrue(lr.compiled.match("work"))
            self.assertTrue(lr.compiled.match("york"))
            self.assertTrue(lr.compiled.match("kork"))
            self.assertFalse(lr.compiled.match("kraftwerk"))
