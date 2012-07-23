from __future__ import absolute_import
from ..base import Shift, BaseTemplate

class CheetahTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        renderer = self.Template(self.string, searchList=[context])
        return str(renderer)

    @classmethod
    def on_initialize(klass):
        try:
            import Cheetah.Template
        except ImportError:
            return False

        klass.Template = Cheetah.Template.Template
        return True

