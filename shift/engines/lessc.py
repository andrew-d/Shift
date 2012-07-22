from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class LessCSSTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self.renderer(template)

    @classmethod
    def on_initialize(klass):
        try:
            import lesscss.lessc
        except ImportError:
            return False

        klass.renderer = lesscss.lessc.compile
        return True

