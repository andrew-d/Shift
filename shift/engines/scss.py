from __future__ import absolute_import
from ..base import Shift, BaseTemplate
import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

class ScssTemplate(BaseTemplate):
    def load_string(self, template):
        self.string = template

    def render(self, context=None):
        return self.renderer.compile(self.string)

    @classmethod
    def on_initialize(klass):
        # We patch sys.stderr here, since pyScss insists on printing to stderr
        # if it can't find the C extensions.
        old_err = sys.stderr

        try:
            sys.stderr = StringIO()
            try:
                import scss
            except ImportError:
                return False
        finally:
            sys.stderr = old_err

        klass.renderer = scss.Scss()
        return True

