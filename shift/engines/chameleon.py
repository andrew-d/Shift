from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class ChameleonTemplate(BaseTemplate):
    def load_string(self, template):
        self.renderer = self.Template(template)

    def load_file(self, file_path, root_dir=None):
        self.loader = self.PageTemplateLoader(root_dir)
        self.renderer = self.loader[file_path]

    def render(self, context=None):
        ctx = context or {}
        return self.renderer(**ctx)

    @classmethod
    def on_initialize(klass):
        try:
            import chameleon
        except ImportError:
            return False

        klass.PageTemplateLoader = chameleon.PageTemplateLoader
        klass.Template = chameleon.PageTemplate
        return True

