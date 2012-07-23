from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class MakoTemplate(BaseTemplate):
    def load_string(self, template):
        self.renderer = self.Template(template)

    def load_file(self, file_path, root_dir=None):
        path = root_dir or '.'
        self.loader = self.TemplateLookup(directories=[path])
        self.renderer = self.loader.get_template(file_path)

    def render(self, context=None):
        ctx = context or {}
        return self.renderer.render(**ctx)

    @classmethod
    def on_initialize(klass):
        try:
            import mako.template
            import mako.lookup
        except ImportError:
            return False

        klass.TemplateLookup = mako.lookup.TemplateLookup
        klass.Template = mako.template.Template
        return True

