from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class MarkdownTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        return self.renderer(self.string)

    @classmethod
    def on_initialize(klass):
        try:
            import markdown
        except ImportError:
            return False

        klass.renderer = markdown.markdown
        return True

