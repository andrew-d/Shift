from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class BareTemplate(BaseTemplate):
    """
    This template class simply returns the input, unmodified
    """
    @classmethod
    def on_initialize(klass):
        return True

    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        return self.string

