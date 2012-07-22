from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class GenshiMarkupTemplate(BaseTemplate):
    def on_render(self, template, context):
        renderer = klass.renderer(template)
        return renderer.generate(**context)

    @classmethod
    def on_initialize(klass):
        try:
            import genshi.template.markup
        except ImportError:
            return False

        klass.renderer = genshi.template.markup.MarkupTemplate
        return True


class GenshiTextTemplate(BaseTemplate):
    def on_render(self, template, context):
        renderer = klass.renderer(template)
        return renderer.generate(**context)

    @classmethod
    def on_initialize(klass):
        try:
            import genshi.template.text
        except ImportError:
            return False

        klass.renderer = genshi.template.text.NewTextTemplate
        return True

