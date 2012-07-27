from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class GenshiMarkupTemplate(BaseTemplate):
    def load_string(self, template):
        self.renderer = self.MarkupTemplate(template)

    def load_file(self, file_path, root_dir=None):
        path = root_dir or '.'
        self.loader = self.Loader([path])
        self.renderer = self.loader.load(file_path)

    def render(self, context=None):
        ctx = context or {}
        return str(self.renderer.generate(**ctx))

    @classmethod
    def on_initialize(klass):
        try:
            import genshi.template.markup
            import genshi.template.loader
        except ImportError:
            return False

        klass.Loader = genshi.template.loader.TemplateLoader
        klass.MarkupTemplate = genshi.template.markup.MarkupTemplate
        return True


class GenshiTextTemplate(BaseTemplate):
    def load_string(self, template):
        self.renderer = self.Template(template)

    def render(self, context=None):
        ctx = context or {}
        return str(self.renderer.generate(**ctx))

    @classmethod
    def on_initialize(klass):
        try:
            import genshi.template.text
        except ImportError:
            return False

        klass.Template = genshi.template.text.NewTextTemplate
        return True

