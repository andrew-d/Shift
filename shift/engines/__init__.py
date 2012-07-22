# In this package, we simply import all the template engines. Once each engine
# has been imported, we register them.
from .bare import BareTemplate
from .jinja2 import JinjaTemplate



# Import the registry class.
from ..base import Shift

# Register all the classes.
Shift.register_class(BareTemplate, 'bare')
Shift.register_class(JinjaTemplate, 'jinja2')

