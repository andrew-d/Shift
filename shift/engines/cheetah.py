from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class CheetahTemplate(BaseTemplate):
    def on_render(self, template, context):
        renderer = self.Template(template, searchList=[context])
        return str(renderer)

    @classmethod
    def on_initialize(klass):
        try:
            import Cheetah.Template
        except ImportError:
            return False

        klass.Template = Cheetah.Template.Template
        return True

