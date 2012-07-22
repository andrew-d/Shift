from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class ChameleonTemplate(BaseTemplate):
    def on_render(self, template, context):
        renderer = self.Template(template)
        return renderer(**context)

    @classmethod
    def on_initialize(klass):
        try:
            import chameleon
        except ImportError:
            return False

        klass.Template = chameleon.PageTemplate
        return True

