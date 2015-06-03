# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.utils.factory
   :platform: Unix, Windows
   :synopsis: Encapsulates process of instantiating objects, i.e. generators, schemas and ontologies.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect

from esdoc_mp.core import Class
from esdoc_mp.core import Decoding
from esdoc_mp.core import Enum
from esdoc_mp.core import EnumMember
from esdoc_mp.core import Ontology
from esdoc_mp.core import Package
from esdoc_mp.core import Property



def _get_type_definition(func):
    """Returns a type definition instantiated from a module function.

    """
    result = func()
    result['name'] = func.__name__
    result['doc'] = func.__doc__.strip()

    return result


def _get_type_definitions(modules):
    """Returns a collection of type definitions instantiated from a module.

    :param module mod: Python module in which type definitions are declared.

    :returns: Collection of type definitions.
    :rtype: List

    """
    try:
        iter(modules)
    except TypeError:
        modules = [modules]

    funcs = []
    for module in modules:
        funcs += [m[1] for m in inspect.getmembers(module) if inspect.isfunction(m[1])]

    return [_get_type_definition(i) for i in funcs]


def _get_class_properties(class_):
    """Returns class property definitions.

    """
    result = []
    doc_strings = class_.get('doc_strings', dict())
    for prop in class_.get('properties', []):
        if len(prop) != 3:
            print class_['name'], prop[0]

    for name, type_name, cardinality in class_.get('properties', []):
        doc_string = doc_strings.get(name, None)
        result.append(Property(name, type_name, cardinality, doc_string))

    return result


def _get_class_decodings(class_):
    """Returns class decoding definitions.

    """
    result = []
    for decoding in class_.get('decodings', []):
        property_type = None if len(decoding) == 2 else decoding[2]
        result.append(Decoding(decoding[0], decoding[1], property_type))

    return result


def _get_package_classes(package):
    """Returns package class definitions.

    """
    result = []
    for class_ in _get_type_definitions(package.get('classes', [])):
        result.append(
            Class(class_['name'],
                  class_.get('base', None),
                  class_.get('is_abstract', False),
                  class_.get('doc', None),
                  _get_class_properties(class_),
                  class_.get('constants', []),
                  _get_class_decodings(class_))
        )

    return result


def _get_package_enums(package):
    """Returns package enum definitions.

    """
    result = []
    for enum in _get_type_definitions(package.get('enums', [])):
        result.append(
            Enum(enum['name'],
                 enum.get('is_open', True),
                 enum.get('doc', None),
                 [EnumMember(m[0], m[1]) for m in enum.get('members', [])])
            )

    return result


def _get_ontology_packages(schema):
    """Returns ontology package definitions.

    """
    result = []
    for package in schema['packages']:
        result.append(
            Package(package['name'],
                    package['doc'],
                    _get_package_classes(package),
                    _get_package_enums(package)
                    )
            )

    return result


def create_ontology(schema):
    """Factory method to instantiate an ontology instance from a schema declaration.

    :param dict schema: An ontology schema declaration.

    :returns: An ontology declaration.
    :rtype: esdoc_mp.core.Ontology

    """
    return Ontology(schema['name'],
                    schema['version'],
                    schema['doc'],
                    _get_ontology_packages(schema))


def create_ontology_schema(name, version):
    """Factory method to instantiate an ontology schema instance.

    :param name: Schema name.
    :param version: Schema version.
    :type name: str
    :type version: str
    :returns: An ontology schema.
    :rtype: dict

    """
    from esdoc_mp.schemas import schemas as ontology_schemas

    for schema in ontology_schemas:
        if schema['name'].lower() == name.lower() and \
           schema['version'].lower() == version.lower():
            return schema
    return None