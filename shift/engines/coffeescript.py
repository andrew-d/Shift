from __future__ import absolute_import

from ..base import Shift, BaseTemplate

class CoffeeScriptTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self.renderer(template)

    @classmethod
    def on_initialize(klass):
        try:
            import coffeescript
        except ImportError:
            return False

        klass.renderer = coffeescript.compile
        return True

