from __future__ import absolute_import
from ..base import Shift, BaseTemplate
import warnings

class CheetahTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        # We catch warnings here so we don't get the irritating "you don't
        # have the C extension installed" warning.
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
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

