# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.schemas.reformatter.py
   :platform: Unix, Windows
   :synopsis: Manages reformatting of schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""


def _get_formatter(schema):
    """Returns the schemas formatting module.

    """
    try:
        return schema.FORMATTER
    except Exception:
        pass


def _get_class_formatter(schema):
    """Returns a class formatter.

    """
    formatter = _get_formatter(schema)
    if formatter:
        try:
            return formatter.reformat_class
        except AttributeError:
            pass


def _get_enum_formatter(schema):
    """Returns an enum formatter.

    """
    formatter = _get_formatter(schema)
    if formatter:
        try:
            return formatter.reformat_enum
        except AttributeError:
            pass


def _reformat(type_formatter, module, type_):
    """Reformats type definition using passed formatter.

    """
    # Escape if no formatter specified.
    if type_formatter is None:
        return type_

    # Apply reformatting.
    reformatted = type_formatter(get_package_name(module), type_)
    if reformatted == type_:
        return type_

    # Copy across missing keys.
    for key in [k for k in type_ if k not in reformatted]:
        reformatted[key] = type_[key]

    return reformatted



def get_package_name(package):
    """Returns name of a package from a module.

    """
    try:
        return package['name']
    except TypeError:
        return package.__name__.split('.')[-1].split('_')[0]


def reformat_class(schema, module, cls):
    """Returns a reformatted class definition.

    """
    formatter = _get_class_formatter(schema)

    return _reformat(formatter, module, cls)


def reformat_enum(schema, module, enum):
    """Returns a reformatted enum definition.

    """
    formatter = _get_enum_formatter(schema)

    return _reformat(formatter, module, enum)
