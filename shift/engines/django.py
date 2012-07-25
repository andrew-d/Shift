from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class DjangoTemplate(BaseTemplate):
    def load_string(self, template):
        self.renderer = self.Template(template)

    def load_file(self, file_path, root_dir=None):
        root_dir = root_dir or '.'
        self.settings.configure(TEMPLATE_DIRS=(root_dir,))
        self.renderer = self.get_template(file_path)

    def render(self, context=None):
        context = self.Context(context)
        return self.renderer.render(context)

    @classmethod
    def on_initialize(klass):
        try:
            import django.template
            import django.template.loader
            from django.conf import settings
        except ImportError:
            return False

        klass.settings = settings
        klass.get_template = staticmethod(django.template.loader.get_template)
        klass.Template = django.template.Template
        klass.Context = django.template.Context
        return True

