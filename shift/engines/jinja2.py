from __future__ import absolute_import

from ..base import Shift, BaseTemplate

class JinjaTemplate(BaseTemplate):
    def on_render(self, template, context):
        renderer = self.Template(template)
        return renderer.render(context)

    @classmethod
    def on_initialize(klass):
        try:
            import jinja2
        except ImportError:
            return False

        klass.Template = jinja2.Template
        return True

