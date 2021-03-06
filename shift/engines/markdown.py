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
            import markdown2
            klass.renderer = staticmethod(markdown2.markdown)
            return True
        except ImportError:
            pass

        try:
            import markdown
            klass.renderer = staticmethod(markdown.markdown)
            return True
        except ImportError:
            pass

        return False


