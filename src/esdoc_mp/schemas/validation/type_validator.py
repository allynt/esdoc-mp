# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.schemas.validation.type_validator
   :platform: Unix, Windows
   :synopsis: Validates ontology type definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas.validation import class_validator
from esdoc_mp.schemas.validation import enum_validator


# Whitelist of valid types.
_TYPE_WHITELIST = {'class', 'enum'}


def _validate_base_class_references(ctx):
    """Validates base class references.

    """
    valid_classes = [ctx.get_type_name(factory, module)
                     for module, factory, cls in ctx.classes]

    for module, factory, cls in ctx.classes:
        if 'base' in cls and cls['base'] is not None and cls['base'] not in valid_classes:
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
        class_validator.validate(ctx, module, factory, type_)

    if type_['type'] == 'enum':
        enum_validator.validate(ctx, module, factory, type_)


def validate(ctx):
    """Asserts package types.

    """
    for module, type_factory, type_ in ctx.types:
        _validate_type(ctx, module, type_factory, type_)
    _validate_base_class_references(ctx)
    _validate_class_property_type_references(ctx)
