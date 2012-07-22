from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class DjangoTemplate(BaseTemplate):
    def on_render(self, template, context):
        renderer = self.Template(template)
        context = self.Context(context)
        return renderer.render(context)

    @classmethod
    def on_initialize(klass):
        try:
            import django.template
        except ImportError:
            return False

        klass.Template = django.template.Template
        klass.Context = django.template.Context
        return True

