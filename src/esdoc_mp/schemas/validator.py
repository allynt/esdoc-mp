# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.schemas.validator
   :platform: Unix, Windows
   :synopsis: Validates an ontology schema definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect
import re



# Regular expressions to apply over various names.
_RE_SCHEMA_NAME = '^[a-z_]+$'
_RE_SCHEMA_VERSION = '^[0-9\.]+$'
_RE_CLASS_NAME = '^[a-z_0-9]+$'
_RE_CLASS_PROPERTY_NAME = '^[a-z_]+$'
_RE_CLASS_PROPERTY_TYPE = '^[a-z_]+\.?[a-z_]+$'
_RE_CLASS_REFERENCE = '^[a-z_]+\.?[a-z_]+$'
_RE_ENUM_NAME = '^[a-z_]+$'
_RE_ENUM_MEMBER_NAME = '^[a-zA-Z0-9-_ ]+$'
_RE_PACKAGE_NAME = '^[a-z]+$'

# Whitelist of valid types.
_TYPE_WHITELIST = {'class', 'enum'}

# Whitelist of valid class property cardinality.
_CLASS_PROPERTY_CARDINALITIES = {'0.1', '0.N', '1.1', '1.N'}

# Whitelist of valid class property simple types.
_SIMPLE_CLASS_PROPERTY_TYPES = {
    'bool',
    'date',
    'datetime',
    'float',
    'int',
    'str',
    'uri',
    'uuid'
}


class _ValidationContext(object):
    """Encapsulates schema validation processing information.

    """
    def __init__(self, schema):
        """Instance constructor.

        """
        self.schema = schema
        self.report = list()


    def set_error(self, err):
        """Adds an error to the manged collection.

        """
        self.report.append(err)


    @property
    def schema_name(self):
        """Gets schema name.

        """
        return self.schema.NAME


    @property
    def schema_version(self):
        """Gets schema version.

        """
        return "v{}".format(self.schema.VERSION)


    @property
    def package_factories(self):
        """Gets package factories.

        """
        return sorted(_get_functions(self.schema))


    @property
    def packages(self):
        """Gets package definitions.

        """
        result = list()
        for factory in self.package_factories:
            try:
                result.append((factory, factory()))
            except Exception as err:
                pass

        return sorted([p for p in result if isinstance(p[1], set) and len(p[1])])


    @property
    def type_modules(self):
        """Gets type modules.

        """
        result = list()
        for factory, modules in self.packages:
            result += [(factory, m) for m in modules
                       if inspect.ismodule(m) and _get_functions(m)]

        return sorted(result)


    @property
    def type_factories(self):
        """Gets type factories.

        """
        result = list()
        for factory, module in self.type_modules:
            result += [(module, f) for f in _get_functions(module)]

        return sorted(result)


    @property
    def types(self):
        """Gets type definitions.

        """
        result = list()
        for module, factory in self.type_factories:
            try:
                type_ = factory()
            except Exception as err:
                pass
            else:
                if isinstance(type_, dict):
                    result.append((module, factory, type_))

        return sorted(result)


    @property
    def classes(self):
        """Get class definitions.

        """
        return [t for t in self.types if 'type' in t[2] and t[2]['type'] == 'class']


    def get_name(self, factory, module=None):
        """Gets a name used when displaying an error message.

        """
        if module is None or module == self.schema:
            return "{0}.v{1}.{2}".format(
                self.schema.NAME,
                self.schema.VERSION,
                factory.__name__)
        else:
            return "{0}.v{1}.{2}.{3}".format(
                self.schema.NAME,
                self.schema.VERSION,
                module.__name__.split(".")[-1].split("_")[0],
                factory.__name__)


    def get_type_name(self, factory, module):
        """Gets a type name.

        """
        return "{0}.{1}".format(
            module.__name__.split(".")[-1].split("_")[0],
            factory.__name__)


def _get_functions(modules):
    """Returns a collection of function pointers declared within a module.

    """
    try:
        iter(modules)
    except TypeError:
        modules = [modules]

    result = set()
    for module in modules:
        result.update({m[1] for m in inspect.getmembers(module) if inspect.isfunction(m[1])})

    return result


def _validate_class(ctx, module, factory, cls):
    """Validates a class definition.

    """
    if 'base' not in cls:
        err = 'Invalid class: {} --> required attribute "base" is missing'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if 'is_abstract' not in cls:
        err = 'Invalid class: {} --> required attribute "is_abstract" is missing'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if not re.match(_RE_CLASS_NAME, factory.__name__):
        err = 'Invalid class: {} --> name format must be lower_case_underscore'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if cls['base'] is not None and not re.match(_RE_CLASS_REFERENCE, cls['base']):
        err = 'Invalid class: {} --> base class reference format must be lower_case_underscore'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if cls['base'] is not None and not len(cls['base'].split('.')) == 2:
        err = 'Invalid class: {} --> base class reference must contain a "." spliting the package and type references, e.g. activity.numerical_activity'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if not isinstance(cls['is_abstract'], bool):
        err = 'Invalid class: {} --> "is_abstract" attribute must be a boolean'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if 'doc_strings' in cls and not isinstance(cls['doc_strings'], dict):
        err = 'Invalid class: {} --> "doc_strings" attribute must be a dict'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if 'properties' in cls and not isinstance(cls['properties'], list):
        err = 'Invalid class: {} --> "properties" attribute must be a list'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if [p for p in cls.get('properties', []) if not isinstance(p, tuple) or not len(p) == 3]:
        err = 'Invalid class: {} --> all properties must be 3 item tuples (name, type, cardinality)'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    for p in cls.get('properties', []):
        _validate_class_property(ctx, module, factory, cls, p[0], p[1], p[2])


def _validate_class_property(ctx, module, factory, cls, name, typeof, cardinality):
    """Validates a class property.

    """
    if not re.match(_RE_CLASS_PROPERTY_NAME, name):
        err = 'Invalid class property: {0}.[{1}] --> name format must be lower_case_underscore'
        err = err.format(ctx.get_name(factory, module), name)
        ctx.set_error(err)

    if not re.match(_RE_CLASS_PROPERTY_TYPE, typeof):
        err = 'Invalid class property: {0}.[{1}] --> type format must be lower_case_underscore '
        err += '(for class references a "." is expected)'
        err = err.format(ctx.get_name(factory, module), name)
        ctx.set_error(err)

    if len(typeof.split('.')) == 1 and \
       typeof not in _SIMPLE_CLASS_PROPERTY_TYPES:
        err = 'Invalid class property: {0}.[{1}] --> type must be in {2}'
        err = err.format(ctx.get_name(factory, module), name, _SIMPLE_CLASS_PROPERTY_TYPES)
        ctx.set_error(err)

    if len(typeof.split('.')) == 2:
        pass
        # print('TODO: validate complex type reference: {}'.format(typeof))

    if cardinality not in _CLASS_PROPERTY_CARDINALITIES:
        err = 'Invalid class property: {0}.[{1}] --> cardinality must be in {2}'
        err = err.format(ctx.get_name(factory, module), name, _CLASS_PROPERTY_CARDINALITIES)
        ctx.set_error(err)


def _validate_base_class_references(ctx):
    """Validates base class references.

    """
    valid_classes = [ctx.get_type_name(factory, module)
                     for module, factory, cls in ctx.classes]

    for module, factory, cls in ctx.classes:
        if cls['base'] and cls['base'] not in valid_classes:
            err = 'Invalid class: {0} --> base class "{1}" is unrecognized'
            err = err.format(ctx.get_name(factory, module), cls['base'])
            ctx.set_error(err)


def _validate_class_property_type_references(ctx):
    """Validates base class references.

    """
    valid_types = [ctx.get_type_name(factory, module)
                   for module, factory, type_ in ctx.types]

    for module, factory, cls in ctx.classes:
        for name, typeof in [(p[0], p[1]) for p in cls.get('properties', [])
                             if len(p[1].split(".")) == 2 and p[1] not in valid_types]:
            err = 'Invalid class property: {0}.[{1}] --> type reference "{2}" is unrecognized'
            err = err.format(ctx.get_name(factory, module), name, typeof)
            ctx.set_error(err)


def _validate_enum(ctx, module, factory, enum):
    """Validates an enumeration.

    """
    if not re.match(_RE_ENUM_NAME, factory.__name__):
        err = 'Invalid enum: {} --> name format must be lower_case_underscore'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if 'is_open' not in enum:
        err = 'Invalid enum: {} --> required attribute "is_open" is missing'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if not isinstance(enum['is_open'], bool):
        err = 'Invalid enum: {} --> "is_open" attribute must be a boolean'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if 'members' in enum and not isinstance(enum['members'], list):
        err = 'Invalid enum: {} --> "members" attribute must be a list'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if [m for m in enum.get('members', []) if not isinstance(m, tuple) or not len(m) == 2]:
        err = 'Invalid enum: {} --> all members must be 2 item tuples (name, doc_string)'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    for m in enum.get('members', []):
        _validate_enum_member(ctx, module, factory, enum, m[0], m[1])


def _validate_enum_member(ctx, module, factory, enum, name, doc_string):
    """Validates an enumeration member.

    """
    if not re.match(_RE_ENUM_MEMBER_NAME, name):
        err = 'Invalid enum member: {0}.{1} --> name contain invalid characters'
        err = err.format(ctx.get_name(factory, module), name)
        ctx.set_error(err)

    if doc_string is not None and not len(doc_string.strip()):
        err = 'Invalid enum member: {0}.{1} --> doc string must be either None or a string'
        err = err.format(ctx.get_name(factory, module), name)
        ctx.set_error(err)


def _validate_factory(ctx, module, factory, expected_type, type_description):
    """Validates a factory function.

    """
    try:
        instance = factory()
    except:
        err = 'Invalid {0}: {1} --> must be a no-arg callable'
        err = err.format(type_description, ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if not isinstance(instance, expected_type):
        err = 'Invalid {0}: {1} --> unexpected return type (was expecting {2})'
        err = err.format(type_description, ctx.get_name(factory, module), expected_type.__name__)
        ctx.set_error(err)
        return

    if not len(instance):
        err = 'Invalid {0}: {1} --> must not return an empty collection'
        err = err.format(type_description, ctx.get_name(factory, module))
        ctx.set_error(err)


def _validate_package(ctx, factory, modules):
    """Validates a package.

    """
    if not re.match(_RE_PACKAGE_NAME, factory.__name__):
        err = 'Invalid package: {} --> must be a single word in lower case'
        err = err.format(ctx.get_name(factory))
        ctx.set_error(err)

    if not factory.__doc__ or not factory.__doc__.strip():
        err = 'Invalid package: {} --> must have a doc string'
        err = err.format(ctx.get_name(factory))
        ctx.set_error(err)
        return

    if not len(modules):
        err = 'Invalid package: {} --> must have at least one package type module'
        err = err.format(ctx.get_name(factory))
        ctx.set_error(err)
        return

    for module in modules:
        if not inspect.ismodule(module):
            err = 'Invalid package: {} --> all package type modules must be defined as python modules'
            err = err.format(ctx.get_name(factory))
            ctx.set_error(err)
            continue

        if not _get_functions(module):
            err = 'Invalid package: {} --> all package type modules must must contain at least one type factory'
            err = err.format(ctx.get_name(factory))
            ctx.set_error(err)
            continue

        for type_factory in  _get_functions(module):
            _validate_factory(ctx, module, type_factory, dict, 'type')


def _validate_packages(ctx):
    """Validates package level attributes.

    """
    for factory, modules in ctx.packages:
        _validate_package(ctx, factory, modules)


def _validate_schema(ctx):
    """Validates schema level attributes.

    """
    if not inspect.ismodule(ctx.schema):
        ctx.set_error('Invalid schema --> must be python modules.')
        return

    if not hasattr(ctx.schema, 'NAME'):
        ctx.set_error('Invalid schema --> required attribute NAME is missing')

    if not hasattr(ctx.schema, 'VERSION'):
        ctx.set_error('Invalid schema --> required attribute VERSION is missing')

    if not hasattr(ctx.schema, 'DOC'):
        ctx.set_error('Invalid schema --> required attribute DOC is missing')

    if not ctx.package_factories:
        ctx.set_error('Invalid schema --> must declare at least one package')

    if ctx.report:
        return

    if ctx.schema.DOC is None or not ctx.schema.DOC.strip():
        ctx.set_error('Invalid schema --> required attribute DOC is missing')

    if not re.match(_RE_SCHEMA_NAME, ctx.schema.NAME):
        ctx.set_error('Invalid schema --> NAME must be a single word in lower case')

    if not re.match(_RE_SCHEMA_VERSION, ctx.schema.VERSION):
        ctx.set_error('Invalid schema --> VERSION must be a postive integer')

    for factory in ctx.package_factories:
        _validate_factory(ctx, ctx.schema, factory, set, 'package')


def _validate_type(ctx, module, factory, type_):
    """Asserts package types.

    """
    if not factory.__doc__ or not factory.__doc__.strip():
        err = 'Invalid type: {} --> must specify a doc string'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if 'type' not in type_:
        err = 'Invalid type: {} --> must specify a type attribute'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if type_['type'] not in _TYPE_WHITELIST:
        err = 'Invalid type: {0} --> type attribute must be in {1}'
        err = err.format(ctx.get_name(factory, module), _TYPE_WHITELIST)
        ctx.set_error(err)
        return

    if type_['type'] == 'class':
        _validate_class(ctx, module, factory, type_)

    if type_['type'] == 'enum':
        _validate_enum(ctx, module, factory, type_)


def _validate_types(ctx):
    """Asserts package types.

    """
    for module, type_factory, type_ in ctx.types:
        _validate_type(ctx, module, type_factory, type_)


def validate(schema):
    """Validates ontology schema.

    :param module schema: Ontology schema definition.

    :returns: Set of validation errors (if any).
    :rtype: set

    """
    ctx = _ValidationContext(schema)
    for validator in (
        _validate_schema,
        _validate_packages,
        _validate_types,
        _validate_base_class_references,
        _validate_class_property_type_references
        ):
        validator(ctx)
        if ctx.report:
            break

    return ctx.report
