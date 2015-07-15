# TODO move code from utils.validation to here# -*- coding: utf-8 -*-

"""A set of CIM meta-programming ontology configurqtion validation functions.

"""
import inspect
import os
import re


def _get_schema():
    """Returns configuration schema.

    """
    return {
        'ontology' : {
            'type' : dict,
            'fields' : {
                'name' : (str, True, '^[a-z_]+$'),
                'version' : (str, True, '^[0-9\.]+$'),
                'doc' : (str, True, None),
                'packages' : ('packages', True, None),
            },
        },
        'packages': {
            'type' : list,
            'item_type' : 'package',
        },
        'package' : {
            'type' : dict,
            'fields' : {
                'name' : (str, True, '^[a-z]+$'),
                'doc' : (str, True, None),
                'classes' : ('classes', True, None),
                'enums' : ('enums', True, None),
            },
        },
        'classes': {
            'type' : list,
            'item_type' : 'class',
        },
        'class' : {
            'type' : dict,
            'fields' : {
                'name' : (str, True, '^[a-z_0-9]+$'),
                'base' : (str, False, '^[a-z_]+\.?[a-z_]+$'),
                'abstract' : (bool, True, None),
                'doc' : (str, False, None),
                'properties' : ('properties', True, None),
                'decodings' : ('decodings', True, None),
            },
        },
        'properties': {
            'type' : list,
            'item_type' : 'property',
        },
        'property' : {
            'type' : tuple,
            'length' : '4',
            '0' : (str, True, '^[a-z_]+$'),                     # name
            '1' : (str, True, '^[a-z_]+\.?[a-z_]+$'),           # type
            '2' : (str, True, ['0.1', '0.N', '1.1', '1.N']),    # cardinality
            '3' : (str, False, None),                           # doc
        },
        'decodings': {
            'type' : list,
            'item_type' : 'decoding',
        },
        'decoding' : {
            'type' : tuple,
            'length' : '2|3',
            '0' : (str, True, '^[a-z_]+$'),                     # name
            '1' : (str, True, None),                            # decoding
            '2' : (str, True, '^[a-z_]+\.?[a-z_]+$'),           # sub-type
        },
        'enums': {
            'type' : list,
            'item_type' : 'enum',
        },
        'enum' : {
            'type' : dict,
            'fields' : {
                'name' : (str, True, '^[a-z_]+$'),
                'is_open' : (bool, True, None),
                'doc' : (str, False, None),
                'members' : ('enum_members', True, None),
            },
        },
        'enum_members': {
            'type' : list,
            'item_type' : 'enum_member',
        },
        'enum_member' : {
            'type' : tuple,
            'length' : '2',
            'fields' : {
                '0' : (str, True, '^[a-z-A-Z]+$'),          # name
                '1' : (str, False, None),                   # doc
            },
        },
    }


def _validate_field(field, field_data, field_elem, ctx):
    """Validates configuration data against passed dictionary configuration element.

    Keyword Arguments:
    data - data being validated.
    elem - dictionary configuration element that data is associatd with.
    ctx - validation context.

    """
    errors = []
    schema = _get_schema()

    # Unpack field attributes.
    field_type, field_value_required, field_validator = field_elem

    # Field value required validation.
    if field_data is None:
        if field_value_required:
            _set_error(ctx, 'Required field value :: {0}.'.format(field))

    # Simple field validation.
    elif field_type not in schema:
        # ... field type validation.
        if not isinstance(field_data, field_type):
            _set_error(ctx, '{0} value is of an invalid type (expected {1}).'.format(field_data, field_type))
        elif field_validator is not None:
            if isinstance(field_validator, list) and field_data not in field_validator:
                _set_error(ctx, '{0} value ({1}) is not permitted value :: expected one of {2}.'.format(field, field_data, field_validator))
            elif re.match(field_validator, field_data) is None:
                _set_error(ctx, '{0} format is invalid :: {1}.'.format(field, field_data))

    # Complex field validation.
    else:
        # ... field type validation.
        field_sub_type = schema[field_type]['type']
        if not isinstance(field_data, field_sub_type):
            _set_error(ctx, 'Invalid field type :: {0} (expected {1}).'.format(field, field_sub_type))
        # ... recurse sub-fields.
        else:
            _set_error(ctx, _validate(field_data, field_type, ctx))

    return errors


def _validate_dict(cfg, cfg_schema, ctx):
    """Validates configuration data against passed dictionary configuration element.

    Keyword Arguments:
    cfg - configuration being validated.
    cfg_schema - configuration schema.
    ctx - validation context.

    """
    errors = []

    elem_fields = cfg_schema['fields']
    for field in elem_fields:
        # Field required validation.
        if field not in cfg:
            _set_error(ctx, 'Required field :: {0}.'.format(field))
        # Other field level validation.
        else:
            field_data = cfg[field]
            field_elem = elem_fields[field]
            _set_error(ctx, _validate_field(field, field_data, field_elem, ctx))

    return errors


def _validate_list(cfg, cfg_schema, ctx):
    """Validates configuration data against passed list configuration element.

    Keyword Arguments:
    cfg - configuration being validated.
    cfg_schema - configuration schema.
    ctx - validation context.

    """
    errors = []

    item_elem_name = cfg_schema['item_type']
    for item_data in cfg:
        _set_error(ctx, _validate(item_data, item_elem_name, ctx))

    return errors


def _validate_tuple(cfg, cfg_schema, ctx):
    """Validates configuration data against passed tuple configuration element.

    Keyword Arguments:
    cfg - configuration being validated.
    cfg_schema - configuration schema.
    ctx - validation context.

    """
    errors = []

    if len(cfg) not in map(int, cfg_schema['length'].split('|')):
        _set_error(ctx, 'Invalid tuple length.')

    return errors


def _validate(cfg, cfg_type_name, ctx):
    """Validates configuration data against passed configuration element.

    Keyword Arguments:
    cfg - configuration being validated.
    cfg_type_name - name of configuration schema type (E.G. ontology).
    ctx - validation context.

    """
    errors = []
    schema = _get_schema()

    if cfg_type_name not in schema:
        _set_error(ctx, 'Configuration element unsupported :: {0}.'.format(cfg_type_name))
    else:
        cfg_schema = schema[cfg_type_name]
        cfg_type = cfg_schema['type']
        if isinstance(cfg, cfg_type) == False:
            _set_error(ctx, 'Configuration element type invalid :: {0} (expected {1}).'.format(cfg_schema, cfg_type))
        else:
            if cfg_type == dict:
                _set_error(ctx, _validate_dict(cfg, cfg_schema, ctx))
            elif cfg_type == list:
                _set_error(ctx, _validate_list(cfg, cfg_schema, ctx))
            elif cfg_type == tuple:
                _set_error(ctx, _validate_tuple(cfg, cfg_schema, ctx))

    return errors


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


# Regular expressions to apply over schema.
_RE_SCHEMA_NAME = '^[a-z_]+$'
_RE_SCHEMA_VERSION = '^[0-9\.]+$'
_RE_SCHEMA_BASE_CLASS = '^[a-z_.]+$'
_RE_SCHEMA_CLASS_PROPERTY_NAME = '^[a-z_]+$'

_PROPERTY_CARDINALITY_WHITELIST = {'0.1', '0.N', '1.1', '1.N'}


class _ValidationContext(object):
    """Encapsulates schema validation processing information.

    """
    def __init__(self, schema):
        """Instance constructor.

        """
        self.schema = schema
        self.errors = []


    def set_error(self, err):
        """Adds an error to the manged collection.

        """
        self.errors.append(err)


    @property
    def package_factories(self):
        """Gets package factories.

        """
        return sorted(_get_functions(self.schema))


    @property
    def packages(self):
        """Gets package definitions.

        """
        result = []
        for factory in self.package_factories:
            try:
                type_modules = factory()
            except Exception as err:
                pass
            else:
                if isinstance(type_modules, set):
                    result.append((factory, type_modules))

        return sorted(result)


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
            result += [(factory, module, f) for f in _get_functions(module)]

        return sorted(result)


    @property
    def types(self):
        """Gets type definitions.

        """
        result = list()
        for package, module, type_factory in self.type_factories:
            try:
                type_ = type_factory()
            except Exception as err:
                pass
            else:
                if isinstance(type_, dict):
                    result.append((package, module, type_factory, type_))

        return sorted(result)


def _validate_package_factory(ctx, factory):
    """Asserts that a package has type modules.

    """
    try:
        factory()
    except:
        ctx.set_error('{} package is invalid: must be a no-arg callable'.format(factory.__name__))


def _validate_type_module(ctx, factory, module):
    """Asserts a type module.

    """
    if not inspect.ismodule(module):
        ctx.set_error('{} package is invalid: all type modules must be defined as python modules'.format(factory.__name__))
    elif not _get_functions(module):
        ctx.set_error('{} type module is invalid: does not contain at least one type factory'.format(module.__name__.split('.')[-1]))


def _validate_package(ctx, factory, type_modules):
    """Asserts that a package has type modules.

    """
    if not factory.__doc__ or not factory.__doc__.strip():
        ctx.set_error('{} package is invalid: must have a doc string'.format(factory.__name__))

    if not isinstance(type_modules, set) or not len(type_modules):
        ctx.set_error('{} package is invalid: type modules must be defined as a python set'.format(factory.__name__))
    else:
        for type_module in type_modules:
            _validate_type_module(ctx, factory, type_module)


def _validate_type_factory(ctx, package, type_module, type_factory):
    """Validates a type factory function pointer.

    """
    if not type_factory.__doc__ or not type_factory.__doc__.strip():
        ctx.set_error('{0}.{1} is invalid: must have a doc string'.format(package.__name__, type_factory.__name__))
    else:
        try:
            type_ = type_factory()
        except:
            ctx.set_error('{0}.{1} is invalid: must be a no-arg callable'.format(package.__name__, type_factory.__name__))
        else:
            if not isinstance(type_, dict):
                ctx.set_error('{0}.{1} is invalid: must return a dictionary'.format(package.__name__, type_factory.__name__))


def _validate_class_property(ctx, package, module, type_factory, cls, prop):
    """Validates a class property.

    """
    if not isinstance(prop, tuple):
        ctx.set_error('{0}.{1} is invalid: all properties must be declared as a tuple of 3 members (name, type, cardinality)'.format(package.__name__, type_factory.__name__))
    elif not len(prop) == 3:
        ctx.set_error('{0}.{1} is invalid: all properties must be declared as a tuple of 3 members (name, type, cardinality)'.format(package.__name__, type_factory.__name__))
    else:
        prop_name, prop_type, prop_cardinality = prop
        if not re.match(_RE_SCHEMA_CLASS_PROPERTY_NAME, prop_name):
            ctx.set_error('{0}.{1}.{2} is invalid: property name is not in lower case underscore format'.format(package.__name__, type_factory.__name__, prop_name))
        if prop_cardinality not in _PROPERTY_CARDINALITY_WHITELIST:
            ctx.set_error('invalid class property --> {0}.{1}.{2}: cardinality must be in {3}'.format(package.__name__, type_factory.__name__, prop_name, _PROPERTY_CARDINALITY_WHITELIST))


def _validate_class(ctx, package, module, type_factory, cls):
    """Validates a class definition.

    """
    if 'base' not in cls:
        ctx.set_error('{0}.{1} is invalid: does not contain a "base" attribute'.format(package.__name__, type_factory.__name__))
    elif cls['base'] is not None and not re.match(_RE_SCHEMA_BASE_CLASS, cls['base']):
        ctx.set_error('{0}.{1} is invalid: "base" attribute does not refer to a class'.format(package.__name__, type_factory.__name__))

    if 'is_abstract' not in cls:
        ctx.set_error('{0}.{1} is invalid: does not contain an "is_abstract" attribute'.format(package.__name__, type_factory.__name__))
    elif not isinstance(cls['is_abstract'], bool):
        ctx.set_error('{0}.{1} is invalid: "is_abstract" attribute must be a boolean'.format(package.__name__, type_factory.__name__))

    if 'properties' in cls:
        if not isinstance(cls['properties'], list):
            ctx.set_error('{0}.{1} is invalid: "properties" attribute must be a set'.format(package.__name__, type_factory.__name__))
        else:
            for prop in cls['properties']:
                _validate_class_property(ctx, package, module, type_factory, cls, prop)




def _validate_enum(ctx, package, module, type_factory, enum):
    """Validates an enum definition.

    """
    pass


def _validate_type(ctx, package, module, type_factory, type_):
    """Asserts package types.

    """
    if 'type' not in type_:
        ctx.set_error('Type definition {0}.{1} is invalid: does not contain a type attribute'.format(package.__name__, type_factory.__name__))
    elif type_['type'] not in ['class', 'enum']:
        ctx.set_error('Type definition {0}.{1} is invalid: must be either a class or enum'.format(package.__name__, type_factory.__name__))
    else:
        sub_validator = _validate_class if type_['type'] == 'class' else _validate_enum
        sub_validator(ctx, package, module, type_factory, type_)


def _validate_schema(ctx):
    """Validates schema level attributes.

    """
    if not inspect.ismodule(ctx.schema):
        ctx.set_error('Schemas must be python modules.')

    if not hasattr(ctx.schema, 'DOC') or not ctx.schema.DOC.strip():
        ctx.set_error('Schema must declare a DOC attribute')

    if not hasattr(ctx.schema, 'NAME'):
        ctx.set_error('Schema must declare a NAME attribute')

    if not re.match(_RE_SCHEMA_NAME, ctx.schema.NAME):
        ctx.set_error('Schema NAME must be a single word')

    if not hasattr(ctx.schema, 'VERSION'):
        ctx.set_error('Schema must declare a VERSION attribute')

    if not re.match(_RE_SCHEMA_VERSION, ctx.schema.VERSION):
        ctx.set_error('Schema version must be a postive integer')


def _validate_package_factories(ctx):
    """Asserts package type modules.

    """
    if not ctx.package_factories:
        ctx.set_error('Schema must declare at least one package factory function')

    for factory in ctx.package_factories:
        _validate_package_factory(ctx, factory)


def _validate_packages(ctx):
    """Validates package level attributes.

    """
    for factory, type_modules in ctx.packages:
        _validate_package(ctx, factory, type_modules)


def _validate_type_factories(ctx):
    """Asserts package type modules.

    """
    for package, type_module, factory in ctx.type_factories:
        _validate_type_factory(ctx, package, type_module, factory)


def _validate_types(ctx):
    """Asserts package types.

    """
    for package, module, type_factory, type_ in ctx.types:
        _validate_type(ctx, package, module, type_factory, type_)


def validate(schema):
    """Validates ontology schema.

    :param module schema: Ontology schema definition.

    :returns: List of validation errors (if any).
    :rtype: list

    """
    ctx = _ValidationContext(schema)
    for validator in (
        _validate_schema,
        _validate_package_factories,
        _validate_packages,
        _validate_type_factories,
        _validate_types
        ):
        validator(ctx)
        if ctx.errors:
            break

    return ctx.errors
