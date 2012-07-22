from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class CreoleTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self.renderer(template)

    @classmethod
    def on_initialize(klass):
        try:
            import creole
        except ImportError:
            return False

        klass.renderer = creole.creole2html
        return True

