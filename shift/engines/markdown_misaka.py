from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class MarkdownMisakaTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        return self.renderer(self.string)

    @classmethod
    def on_initialize(klass):
        try:
            import misaka
        except ImportError:
            return False

        klass.renderer = misaka.html
        return True

