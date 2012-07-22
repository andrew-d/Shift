from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class TextileTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self.renderer(template)

    @classmethod
    def on_initialize(klass):
        try:
            import textile
        except ImportError:
            return False

        klass.renderer = textile.textile
        return True

