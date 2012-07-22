from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class MarkdownTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self.renderer(template)

    @classmethod
    def on_initialize(klass):
        try:
            import markdown
        except ImportError:
            return False

        klass.renderer = markdown.markdown
        return True

