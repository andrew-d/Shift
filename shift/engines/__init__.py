# In this package, we simply import all the template engines. Once each engine
# has been imported, we register them.
from .bare import BareTemplate
from .jinja2 import JinjaTemplate
from .mustache import MustacheTemplate
from .scss import ScssTemplate
from .coffeescript import CoffeeScriptTemplate
from .lessc import LessCSSTemplate
from .mako import MakoTemplate
from .markdown import MarkdownTemplate
from .misaka import MarkdownMisakaTemplate
from .django import DjangoTemplate
from .genshi import GenshiMarkupTemplate, GenshiTextTemplate
from .cheetah import CheetahTemplate
from .chameleon import ChameleonTemplate
from .creole import CreoleTemplate


# Import the registry class.
from ..base import Shift

# Register all the classes.
# NOTE: Order does matter - the registration order defines the order
# in which template engines are tried (first to last).
Shift.register_class(BareTemplate, 'bare')
Shift.register_class(JinjaTemplate, 'jinja2')
Shift.register_class(JinjaTemplate, 'j2')
Shift.register_class(MustacheTemplate, 'mustache')
Shift.register_class(ScssTemplate, 'scss')
Shift.register_class(ScssTemplate, 'sass')
Shift.register_class(CoffeeScriptTemplate, 'coffee')
Shift.register_class(CoffeeScriptTemplate, 'coffeescript')
Shift.register_class(LessCSSTemplate, 'less')
Shift.register_class(MakoTemplate, 'mako')
Shift.register_class(MarkdownMisakaTemplate, 'markdown')
Shift.register_class(MarkdownMisakaTemplate, 'md')
Shift.register_class(MarkdownTemplate, 'markdown')
Shift.register_class(MarkdownTemplate, 'md')
Shift.register_class(DjangoTemplate, 'django')
Shift.register_class(GenshiMarkupTemplate, 'markup.genshi')
Shift.register_class(GenshiTextTemplate, 'text.genshi')
Shift.register_class(CheetahTemplate, 'cheetah')
Shift.register_class(ChameleonTemplate, 'chameleon')
Shift.register_class(ChameleonTemplate, 'pt')
Shift.register_class(CreoleTemplate, 'creole')

