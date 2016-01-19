# -*- coding: utf-8 -*-

"""Encapsualtes a set of qxml specific name conversion operations.

"""

from esdoc_mp.generators.generator_utils import *
import os


# Language name constant.
LANGUAGE = 'qxml'

# Language file extension constant.
FILE_EXTENSION = '.xml'

# Set of simple type mappings.
_SIMPLE_TYPE_MAPPINGS = {
    # TODO: THE Q ALSO INCLUDES 'EMAIL' & 'TIME'
    # TODO: CIM2 IS SUPPOSED TO INCLUDE 'email'
    # TODO: CHECK THE STATUS OF THIS
    'bool' : 'BOOLEAN',
    'date' : 'DATE',
    'datetime' : 'DATETIME',
    'float' : 'DECIMAL',
    'int' : 'INTEGER',
    'str' : 'STRING',
    'unicode' : 'STRING',
    'uri' : 'URL',
    'uuid' : 'STRING',
}


# Standard null value.
_NULL_VALUE = 'None'

# Iterable null value.
_NULL_VALUE_ITERABLE = '[]'

QXML_ATOMIC_TYPE = "ATOMIC"
QXML_ENUMERATION_TYPE = "ENUMERATION"
QXML_RELATIONSHIP_TYPE = "RELATIONSHIP"


def _strip(name):
    """Returns stripped name.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name
    return name


def _strip_class_name(name):
    """Returns stripped class name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[len(name.split('.')) - 1]
    return name


def get_ontology_name(name):
    """Converts name to an ontology name suitable for QXML.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name

    return name.lower()


def get_ontology_version(name):
    """Converts version identifier to a version suitable for QXML.

    Keyword Arguments:
    name - name of version identifier being converted.

    """
    if isinstance(name, str) == False:
        name = name.version

    return name


def _get_ontology_directory(ctx, include_version=True):
    """Returns ontology directory into which code is generated.

    :param GeneratorContext ctx: Generation context information.
    :param str sub: Subpackage name.

    """
    _dir = ''
    if ctx.output_dir is not None:
        _dir += ctx.output_dir + '/'
    _dir += get_ontology_name(ctx.ontology)
    if include_version:
        _dir += '/'
        _dir += 'v' + get_ontology_version(ctx.ontology)
    return _dir


def _get_ontology_filename(ctx, include_version=True):
    """

    :param ctx:
    :param include_version:
    :return:
    """
    ontology = ctx.ontology
    ontology_filename = get_ontology_name(ontology)
    if include_version:
        ontology_filename += "_{0}".format(get_ontology_version(ontology).replace('.', '_'))
    ontology_filename += ".xml"
    return ontology_filename


def get_ontology_path(ctx):

    ontology_path = os.path.join(
        _get_ontology_directory(ctx, include_version=True),
        _get_ontology_filename(ctx, include_version=True)
    )
    return ontology_path


def get_package_name(name):
    """Converts name to a package name suitable for QXML.

    :param str name: Package name being converted.

    """
    return _strip_package_name(name)


def get_full_class_name(c):
    """Converts name to a python class name.

    :param str name: Class name being converted.

    """
    return get_package_name(c.package) + "." + get_class_name(c)


def get_class_name(name):
    """Converts name to a python class name.

    :param str name: Class name being converted.

    """
    return convert_to_camel_case(_strip_class_name(name))


# def get_class_import_name(name):
#     """Converts name to a python class import name.
#
#     :param str name: Class name being converted.
#
#     """
#     return _strip_class_name(name)
#
#
# def get_class_functional_name(name):
#     """Converts name to one suitable for use in a python function definition.
#
#     :param str name: Class name being converted.
#
#     """
#     return _strip_class_name(name)


def get_class_doc_string_name(name):
    """Converts name to one suitable for use in QXML documentation.

    :param str name: Class name being converted.

    """
    name = _strip_class_name(name)
    return name.replace('_', ' ')


# def _get_class_file_name(name):
#     """Converts name to a python class file name.
#
#     :param str name: Class name being converted.
#
#     """
#     name = _strip_class_name(name)
#     return name + FILE_EXTENSION


def _get_class_base_name(c):
    """Converts name to a python base class name.

    """
    if c.base is None:
        return 'object'
    elif c.base.package == c.package:
        return get_class_name(c.base)
    else:
        return get_full_class_name(c.base)


# def get_property_ctor(p):
#     """Converts class property to a python property constructor declaration.
#
#     """
#     return 'self.{0} = {1}'.format(get_property_name(p),
#                                    get_property_default_value(p))
#
#
# def get_property_reference_ctor(p):
#     """Converts class property to a python reference property constructor declaration.
#
#     """
#     return 'self.reference_to_{0} = {1}'.format(get_property_name(p), get_property_default_value(p))
#
#
# def get_property_name(name):
#     """Converts name to a python class property name.
#
#     """
#     return _strip(name)
#
#
# def get_property_field_name(name):
#     """Converts name to a python class property field name.
#
#     """
#     return _PROPERTY_FIELD_PREFIX + _strip(name)
#
#
# def get_property_default_value(p):
#     """Returns property default value.
#
#     """
#     # Return value based upon property type:
#     # ... meta information;
#     if p.name == "meta":
#         if p.package == p.type.package:
#             return "{0}()".format(get_type_name(p.type))
#         else:
#             return "{0}.{1}()".format(get_package_name(p.type.package),
#                                       get_type_name(p.type))
#
#     # ... iterative types;
#     elif p.is_iterative:
#         return _NULL_VALUE_ITERABLE
#
#     # ... enum / complex / simple types.
#     else:
#         return _NULL_VALUE
#
#
# def get_type_name(type):
#     """Returns python type name.
#
#     :param str name: Type name being converted.
#
#     """
#     name = type.name
#     if type.is_simple:
#         return _get_simple_type_mapping(name)
#     elif type.is_enum:
#         return _get_simple_type_mapping('unicode')
#     elif type.is_complex:
#         return get_class_name(name)
#
#
# def get_type_functional_name(t, get_full_name=False):
#     """Returns python type functional name.
#
#     :param str name: Type name being converted.
#
#     """
#     name = t.name
#     if t.is_simple:
#         return _get_simple_type_mapping(name)
#     elif t.is_enum:
#         return 'unicode'
#     elif t.is_complex:
#         if get_full_name:
#             return get_package_name(name) + "." + get_class_name(name)
#         else:
#             return get_class_name(name)
#
#
# def get_type_doc_name(t):
#     """Returns python type documentation name.
#
#     :param str name: Type name being converted.
#
#     """
#     name = t.name
#     if t.is_simple:
#         return _get_simple_type_mapping(name)
#     elif t.is_enum:
#         return '{0}.{1}'.format(get_package_name(name), get_enum_name(name))
#     elif t.is_complex:
#         return '{0}.{1}'.format(get_package_name(name), get_class_name(name))
#
#
# def _strip_enum_name(name):
#     """Returns stripped enum name.
#
#     """
#     name = _strip(name)
#     if name.find('.') != -1:
#         name = name.split('.')[len(name.split('.')) - 1]
#     return name
#
#
# def get_enum_name(name):
#     """Converts name to a python enum name.
#
#     :param str name: Enum name being converted.
#
#     """
#     return convert_to_camel_case(_strip_enum_name(name))
#
#
# def get_enum_file_name(name):
#     """Converts name to a python enum file name.
#
#     :param str name: Enum name being converted.
#
#     """
#     return _strip_enum_name(name) + FILE_EXTENSION
#
#
# def _get_simple_type_mapping(simple):
#     """Returns matching simple type mapping.
#
#     """
#     return _SIMPLE_TYPE_MAPPINGS[simple]


def _strip_package_name(name):
    """Returns stripped package name.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[0]
    return name


def get_qualified_enum_name(enum):
    if enum.package:
        return "{0}.{1}".format(enum.package, enum.name)
    else:
        return enum.name

def get_atomic_property_type(property):
    """
    returns the corresponding QXML atomic property type
    :param property:
    :return:
    """
    property_type = property.type
    property_type_name = property_type.name_of_type
    if property_type_name not in _SIMPLE_TYPE_MAPPINGS:
        # TODO: REMOVE THIS ONCE I'M SURE EVERYTHING WORKS
        raise ValueError("Unable to locate '{0}' in ATOMIC TYPE MAP for {1}".format(property_type, property))
    return _SIMPLE_TYPE_MAPPINGS[property_type_name]


def get_relationship_property_target(property):
    """
    returns a QXML compatible name of the class that this property points to
    :param property:
    :return:
    """
    property_type = property.type
    property_type_name = property_type.name_of_type
    return property_type_name


def get_property_type(property):
    """
    returns the corresponding QXML property type
    :param property:
    :return:
    """
    property_type = property.type
    if property_type.is_class:
        return QXML_RELATIONSHIP_TYPE
    elif property_type.is_enum:
        return QXML_ENUMERATION_TYPE
    else:
        return QXML_ATOMIC_TYPE


def recurse_through_base_classes(fn, cls, **kwargs):
    """
    apply fn to all elements in hierarchy of base classes, starting w/ cls
    :param cls: class to start recursion from
    :return: list of fn values for all base classes
    """
    ret = kwargs.pop("ret", [])
    ret.insert(0, fn(cls))
    base_cls = cls.base
    if base_cls is None:
        return ret
    return recurse_through_base_classes(fn, base_cls, ret=ret)


def format(o):
    """Pythonizes ontology names.

    """
    o.op_name = get_ontology_name(o)
    o.op_version = get_ontology_version(o)

    for p in o.packages:
        p.op_name = get_package_name(p)

    for c in o.classes:
        c.op_base_name = _get_class_base_name(c)
        c.op_doc_string_name = get_class_doc_string_name(c)
        # c.op_file_name = _get_class_file_name(c)
        # c.op_functional_name = get_class_functional_name(c)
        # c.op_import_name = get_class_import_name(c)
        c.op_name = get_class_name(c)
        c.op_full_name = get_full_class_name(c)
