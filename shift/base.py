from __future__ import with_statement

import os
import re
import sys
import abc
from collections import defaultdict
from copy import copy


class Shift(object):
    """
    This class implements a template registry, where individual template
    classes can register themselves to handle template types.
    """
    mappings = defaultdict(list)

    def __init__(self, template_root=None):
        template_root = template_root or "views"
        self.mappings = copy(Shift.mappings)
        self.template_root = os.path.abspath(template_root)

    def new(self, template_path, **kwargs):
        # Remove any "template_string" arguments from the kwargs - new() is always for files.
        kwargs.pop("template_string", None)

        # For each engine...
        for engine in self._engines_iterator(template_path):
            if engine.initialized:
                # We try to instantiate this renderer.  If an error is raised, we
                # catch it and try the next engine.
                # TODO: is it really a smart idea to try and catch ALL exceptions
                # here?  Perhaps not.
                renderer = engine(template_path=template_path, root_dir=self.template_root, **kwargs)
                return renderer
            else:               # pragma: no cover
                pass

        # Return None if we haven't found a match by now.
        return None

    @staticmethod
    def register_class(klass, mapping):
        assert issubclass(klass, BaseTemplate)
        klass.initialize()
        Shift.mappings[mapping].append(klass)

    def register_on_instance(self, klass, mapping):
        assert issubclass(klass, BaseTemplate)
        klass.initialize()
        self.mappings[mapping].append(klass)

    def _engines_iterator(self, path):
        for path in self._paths_iterator(path):
            if path in self.mappings:
                for engine in self.mappings[path]:
                    yield engine

    def _paths_iterator(self, path):
        """
        Find the best match for the given path.  Returns the mapping.
        """
        while True:
            # Error if the path is empty.
            if len(path) == 0:
                break

            yield path

            # Strip one segment from the path and try again.
            base_path = os.path.basename(path)
            if base_path == path:
                path = re.sub(r"^[^.]*\.?", "", path)
            else:
                path = base_path


class BaseTemplate(object):
    """
    This is the base template class.  It specifies the interface that template
    renderers must conform to.
    """
    initialized = False
    _initialize_called = False

    def __init__(self, template_path=None, template_string=None, root_dir=None, **kwargs):
        """
        Initialize the template, either with a string or a file.  If both are
        given, an assertion failure will be raised.
        The root_dir parameter is the root directory for templates.  This is
        particularily import for templates that support including other
        templates.
        """
        assert (template_path is None) or (template_string is None)
        if template_string is not None:
            self.load_string(template_string, **kwargs)
        elif template_path is not None:
            self.load_file(template_path, root_dir=root_dir, **kwargs)
        else:
            raise Exception("You must provide either a template string or a file!")

    def load_string(self, template, *args, **kwargs):
        """
        This function is called when we are loading a template from a string.
        """
        raise NotImplementedError("load_string() is not implemented in the base template")

    def load_file(self, file_path, root_dir=None, *args, **kwargs):
        """
        This function is called when we are loading a template from a file.
        By default, we simply read the file into memory and then call the
        load_string function.  Subclasses can override to provide better
        handling of file-loading.
        """
        if root_dir is not None:
            path = os.path.join(root_dir, file_path)
        else:
            path = file_path

        with open(path, 'rb') as f:
            contents = f.read()

            # If we're on Python 3, we convert to a string.
            if sys.version_info[0] >= 3:
                contents = str(contents, "utf-8")

            return self.load_string(contents, *args, **kwargs)

    def render(self, context=None, *args, **kwargs):
        """
        This function does the actual rendering, given a context.  Any args or
        kwargs are passed to the underlying template engine.  This is the
        function that subclasses must overload to provide rendering.
        """
        raise NotImplementedError("render() is not implemented in the base template")

    @classmethod
    def on_initialize(self):
        """
        This function is called exactly once for each template class.  It
        should perform any initialization steps that are required to set
        up the class.  If the class cannot be initialized, then this
        function should return False, which will prevent this template
        class from being instantiated.
        """
        raise NotImplementedError("on_initialize() is not implemented in the base template")

    @classmethod
    def initialize(klass):
        """
        This function will ensure that the on_initialize function is called
        only once for each engine class.
        """
        if not klass._initialize_called:
            klass.initialized = klass.on_initialize()
            klass._initialize_called = True

        return klass.initialized

