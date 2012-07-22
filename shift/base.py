from __future__ import with_statement

import os
import re
import abc
from collections import defaultdict


class Shift(object):
    """
    This class implements a template registry, where individual template
    classes can register themselves to handle template types.
    """
    mappings = defaultdict(list)

    def __init__(self):
        raise NotImplementedError("Shift is a static class - do not instantiate!")

    @staticmethod
    def new(template_path):
        for engine in Shift._engines_iterator(template_path):
            if engine.initialized:
                # print "Engine {0} is initialized - trying it...".format(engine)

                # We try to instantiate this renderer.  If an error is raised, we
                # catch it and try the next engine.
                # TODO: is it really a smart idea to try and catch ALL exceptions
                # here?  Perhaps not.
                try:
                    renderer = engine(template_path)
                    return renderer
                except Exception:
                    pass
            else:
                # print "Engine {0} isn't initialized.".format(engine)
                pass

        # Return None if we haven't found a match by now.
        return None

    @staticmethod
    def register_class(klass, mapping):
        assert issubclass(klass, BaseTemplate)
        # print "Registering {0!r} for {1!r}".format(klass, mapping)

        klass.initialize()
        Shift.mappings[mapping].append(klass)

    @staticmethod
    def _engines_iterator(path):
        """
        Find the best match for the given path.  Returns the mapping.
        TODO: this shoud be an iterator
        """
        while True:
            # print "Checking: {0}".format(path)

            # Error if the path is empty.
            if len(path) == 0:
                break

            if path in Shift.mappings:
                for engine in Shift.mappings[path]:
                    yield engine

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

    def __init__(self, file_path=None):
        self.file_path = file_path

    def on_render(self, template, context, *args, **kwargs):
        """
        This function does the actual rendering, given a context.  Any args or
        kwargs are passed to the underlying template engine.  This is the
        function that subclasses must overload to provide rendering.
        """
        raise NotImplementedError("on_render() is not implemented in the base template")

    @classmethod
    def on_initialize():
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

    def render(self, context=None, *args, **kwargs):
        """
        This function will render a template from a file.
        """
        try:
            with open(self.file_path, 'rb') as f:
                return self.on_render(f.read(), context, *args, **kwargs)
        except IOError:
            pass
        return None

    def render_from_string(self, string, context=None, *args, **kwargs):
        """
        This renders a template from a string.
        """
        return self.on_render(string, context, *args, **kwargs)


