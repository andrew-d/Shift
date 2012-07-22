from __future__ import absolute_import

from ..base import Shift, BaseTemplate

class ScssTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self.renderer.compile(template)

    @classmethod
    def on_initialize(klass):
        try:
            import scss
        except ImportError:
            return False

        klass.renderer = scss.Scss()
        return True

