from . import ShiftTestCase
from .. import Shift, BaseTemplate
from ..engines import JinjaTemplate
import unittest

class TestJinja2(ShiftTestCase):
    def on_setup(self):
        pass

    def test_jinja2_will_load(self):
        self.shift

def suite():
    suite = unittest.TestSuite()

    return suite

