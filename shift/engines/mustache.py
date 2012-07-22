from __future__ import absolute_import

from ..base import Shift, BaseTemplate

class MustacheTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self._render(context)

    @classmethod
    def on_initialize(klass):
        try:
            import pystache
        except ImportError:
            return False

        klass._render = pystache.render
        return True

