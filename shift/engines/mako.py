from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class MakoTemplate(BaseTemplate):
    def on_render(self, template, context):
        renderer = self.Template(template)
        return renderer.render(**context)

    @classmethod
    def on_initialize(klass):
        try:
            import mako.template
        except ImportError:
            return False

        klass.Template = mako.template.Template
        return True

