from __future__ import with_statement

import os
import sys
import unittest
from .helpers import *

ensure_in_path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import shift

class ShiftTestCase(BaseTestCase):
    def setup(self):
        self.shift = shift.Shift()
        self.on_setup()


def suite():
    # Import test suites here.
    from .test_searchpaths import suite as suite_1

    suite = unittest.TestSuite()
    suite.addTest(suite_1())

    from .test_engines import suite as engines_suite
    suite.addTest(engines_suite())

    return suite


def main():
    """
    This runs the our tests, suitable for a command-line application
    """
    # try:
        # unittest.main(defaultTest='suite')
    # except Exception as e:
        # print "Exception: {0!s}".format(e)

    unittest.main(defaultTest='suite')

if __name__ == "__main__":
    main()

