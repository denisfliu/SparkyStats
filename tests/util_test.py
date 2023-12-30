import unittest
import io
import sys

from src.util import warning
import src.util as sqbs


class TestMisc(unittest.TestCase):
    def test_minor_warning_disabled(self):
        out = io.StringIO()
        sys.stdout = out
        sqbs.SKIP_MINOR_WARNINGS = True
        warning("", "", True)
        sys.stdout = sys.__stdout__
        self.assertEqual("", out.getvalue())

    def test_minor_warning_enabled(self):
        out = io.StringIO()
        sys.stdout = out
        sqbs.SKIP_MINOR_WARNINGS = False
        warning("hi", "h", True)
        sys.stdout = sys.__stdout__
        self.assertEqual("[MINOR WARNING | hi]: h\n", out.getvalue())


if __name__ == "__main__":
    unittest.main()
