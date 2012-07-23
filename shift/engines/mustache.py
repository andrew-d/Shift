from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class MustacheTemplate(BaseTemplate):
    def load_string(self, template):
        self.template = template

    def render(self, context=None):
        ctx = context or {}
        return self._render(self.template, ctx)

    @classmethod
    def on_initialize(klass):
        try:
            import pystache
        except ImportError:
            return False

        klass._render = pystache.render
        return True

