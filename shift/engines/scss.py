from __future__ import absolute_import
from ..base import Shift, BaseTemplate
import sys
import StringIO

class ScssTemplate(BaseTemplate):
    def on_render(self, template, context):
        return self.renderer.compile(template)

    @classmethod
    def on_initialize(klass):
        # We patch sys.stderr here, since pyScss insists on printing to stderr
        # if it can't find the C extensions.
        old_err = sys.stderr

        try:
            sys.stderr = StringIO.StringIO()
            try:
                import scss
            except ImportError:
                return False
        finally:
            sys.stderr = old_err

        klass.renderer = scss.Scss()
        return True

