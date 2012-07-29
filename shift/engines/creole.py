from __future__ import absolute_import
from ..base import Shift, BaseTemplate
import sys

class CreoleTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template
        if sys.version_info[0] < 3:
            self.string = unicode(self.string)

    def render(self, context=None):
        return self.renderer(self.string)

    @classmethod
    def on_initialize(klass):
        try:
            import creole
        except ImportError:
            return False

        klass.renderer = staticmethod(creole.creole2html)
        return True

