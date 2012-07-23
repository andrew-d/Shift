from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class ReStructuredTextTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        return self.renderer(source=self.string, writer_name='html4css1')

    @classmethod
    def on_initialize(klass):
        try:
            import docutils.core
        except ImportError:
            return False

        klass.renderer = docutils.core.publish_parts
        return True

