from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class ReStructuredTextTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self.renderer(source=template, writer_name='html4css1')

    @classmethod
    def on_initialize(klass):
        try:
            import docutils.core
        except ImportError:
            return False

        klass.renderer = docutils.core.publish_parts
        return True

