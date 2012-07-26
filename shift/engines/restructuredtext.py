from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class ReStructuredTextTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        parts = self.renderer(source=self.string, writer_name='html4css1')
        if 'html_body' in parts:
            return parts['html_body']
        else:
            return None

    @classmethod
    def on_initialize(klass):
        try:
            import docutils.core
        except ImportError:
            return False

        klass.renderer = staticmethod(docutils.core.publish_parts)
        return True

