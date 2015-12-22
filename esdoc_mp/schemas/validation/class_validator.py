# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.schemas.validation.class_validator
   :platform: Unix, Windows
   :synopsis: Validates ontology class definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import re



# Regular expressions.
_RE_CLASS_NAME = '^[a-z_0-9]+$'
_RE_CLASS_PROPERTY_NAME = '^[a-z_]+$'
_RE_CLASS_PROPERTY_TYPE = '^[a-z_]+\.?[a-z_]+$'
_RE_CLASS_REFERENCE = '^[a-z_]+\.?[a-z_]+$'

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
    'unicode',
    'uri',
    'uuid'
}



def _validate_class_property(ctx, module, factory, cls, name, typeof, cardinality):
    """Validates a class property.

    """
    if not re.match(_RE_CLASS_PROPERTY_NAME, name):
        err = 'Invalid property: {0}.[{1}] --> name format must be lower_case_underscore'
        err = err.format(ctx.get_name(factory, module), name)
        ctx.set_error(err)

    if not re.match(_RE_CLASS_PROPERTY_TYPE, typeof):
        err = 'Invalid property: {0}.[{1}] --> type format must be lower_case_underscore '
        err += '(for class references a "." is expected)'
        err = err.format(ctx.get_name(factory, module), name)
        ctx.set_error(err)

    if len(typeof.split('.')) == 1 and \
       typeof not in _SIMPLE_CLASS_PROPERTY_TYPES:
        err = 'Invalid property: {0}.[{1}] --> simple type must be in {2}'
        err = err.format(ctx.get_name(factory, module), name, _SIMPLE_CLASS_PROPERTY_TYPES)
        ctx.set_error(err)

    if cardinality not in _CLASS_PROPERTY_CARDINALITIES:
        err = 'Invalid property: {0}.[{1}] --> cardinality must be in {2}'
        err = err.format(ctx.get_name(factory, module), name, _CLASS_PROPERTY_CARDINALITIES)
        ctx.set_error(err)


def validate(ctx, module, factory, cls):
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
        err = 'Invalid class: {0} --> base class reference [{1}] format must be lower_case_underscore'
        err = err.format(ctx.get_name(factory, module), cls['base'])
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

    if [p for p in cls.get('properties', []) if not isinstance(p, tuple) or not len(p) in {3, 4}]:
        err = 'Invalid class: {} --> all properties must be tuples (name, type, cardinality, doc_string)'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    for p in cls.get('properties', []):
        _validate_class_property(ctx, module, factory, cls, p[0], p[1], p[2])

