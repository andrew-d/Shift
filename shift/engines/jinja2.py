from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class JinjaTemplate(BaseTemplate):
    def load_string(self, template):
        self.renderer = self.Template(template)

    def load_file(self, file_path, root_dir=None, **kwargs):
        if self.root_dir is not None:
            encoding = kwargs.pop('encoding', 'utf-8')
            self.loader = self.FileSystemLoader(self.root_dir, encoding=encoding)
            self.env = self.Environment(loader=self.loader, **kwargs)
        else:
            self.env = self.Environment()

        self.renderer = self.env.get_template(file_path)

    def render(self, context=None):
        return self.renderer.render(context)

    @classmethod
    def on_initialize(klass):
        try:
            import jinja2
        except ImportError:
            return False

        klass.Loader = jinja2.FileSystemLoader
        klass.Environment = jinja2.Environment
        klass.Template = jinja2.Template
        return True

