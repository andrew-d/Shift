from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class CreoleTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        return self.renderer(unicode(self.string))

    @classmethod
    def on_initialize(klass):
        try:
            import creole
        except ImportError:
            return False

        klass.renderer = staticmethod(creole.creole2html)
        return True

