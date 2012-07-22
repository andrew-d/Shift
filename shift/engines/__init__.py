# In this package, we simply import all the template engines. Once each engine
# has been imported, we register them.
from .bare import BareTemplate
from .jinja2 import JinjaTemplate
from .mustache import MustacheTemplate
from .scss import ScssTemplate
from .coffeescript import CoffeeScriptTemplate


# Import the registry class.
from ..base import Shift

# Register all the classes.
Shift.register_class(BareTemplate, 'bare')
Shift.register_class(JinjaTemplate, 'jinja2')
Shift.register_class(MustacheTemplate, 'mustache')
Shift.register_class(ScssTemplate, 'scss')
Shift.register_class(ScssTemplate, 'sass')
Shift.register_class(CoffeeScriptTemplate, 'coffee')
Shift.register_class(CoffeeScriptTemplate, 'coffeescript')

