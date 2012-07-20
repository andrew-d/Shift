from __future__ import with_statement


class Shift(object):
    """
    This class implements a template registry, where individual template
    classes can register themselves to handle template types.
    """
    def __init__(self):
        raise RuntimeError("Shift is a static class - do not create!")

    @staticmethod
    def new(template_path):
        pass

    @staticmethod
    def register_class(klass):
        print "Registering {0!r}...".format(klass)


class BaseTemplateMetaclass(type):
    def __init__(klass, name, bases, attrs):
        # If this class is not a base class, we add it to the registry.
        if not klass.__name__ == 'BaseTemplate':
            Shift.register_class(klass)

        # Call the base __new__ to finish creating the class.
        return type.__init__(klass, name, bases, attrs)


class BaseTemplate(object):
    """
    This is the base template class.  It specifies the interface that template
    renderers must conform to.
    """
    __metaclass__ = BaseTemplateMetaclass

    def __init__(self, file_path=None):
        self.file_path = file_path

    def on_render(self, context, template, *args, **kwargs):
        """
        This function does the actual rendering, given a context.  Any args or
        kwargs are passed to the underlying template engine.  This is the
        function that subclasses must overload to provide rendering.
        """
        raise NotImplementedError("on_render() is not implemented in the base template")

    def render(self, context, *args, **kwargs):
        """
        This function will render a template from a file.
        """
        with open(self.file_path, 'rb') as f:
            return self.on_render(context, f.read(), *args, **kwargs)
        return None

    def render_from_string(self, context, string, *args, **kwargs):
        """
        This renders a template from a string.
        """
        return self.on_render(context, string, *args, **kwargs)


