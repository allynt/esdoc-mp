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

from esdoc_mp.schemas import reformatter



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


def _get_type_definitions(modules):
    """Returns set of type definitions instantiated from a set of modules.

    """
    def _get_definition(func):
        """Returns a type definition."""
        result = func()
        result['name'] = func.__name__
        result['doc'] = func.__doc__.strip()

        return result

    return [_get_definition(i) for i in _get_functions(modules)]


def _get_package_definitions(modules):
    """Returns set of package definitions instantiated from a set of modules.

    """
    def _get_definition(func):
        """Returns a package definition."""
        return {
            'name': func.__name__,
            'doc': func.__doc__.strip(),
            'types': func()
        }

    return [_get_definition(f) for f in _get_functions(modules)]


def _get_class_properties(class_):
    """Returns class property definitions.

    """
    result = []
    doc_strings = class_.get('doc_strings', dict())
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


def _get_package_classes(schema, package, types):
    """Returns package class definitions.

    """
    result = []
    classes = [reformatter.reformat_class(schema, package, t) for t in types if t['type'] == 'class']
    for cls in [c for c in classes if not reformatter.is_class_excluded(schema, package, c)]:
        result.append(
            Class(cls['name'],
                  cls.get('base', None),
                  cls.get('is_abstract', False),
                  cls.get('doc', None),
                  _get_class_properties(cls),
                  cls.get('constants', []),
                  _get_class_decodings(cls))
        )

    return result


def _get_package_enums(schema, package, types):
    """Returns package enum definitions.

    """
    result = []
    enums = [reformatter.reformat_enum(schema, package, t) for t in types if t['type'] == 'enum']
    for enum in enums:
        result.append(
            Enum(enum['name'],
                 enum.get('is_open', True),
                 enum.get('doc', None),
                 [EnumMember(m[0], m[1]) for m in enum.get('members', [])])
            )

    return result


def _get_package_types(schema, package):
    """Returns package type definitions.

    """
    types = _get_type_definitions(package.get('types', []))

    return _get_package_classes(schema, package, types), \
           _get_package_enums(schema, package, types)


def _get_ontology_packages(schema):
    """Returns ontology package definitions.

    """
    result = []
    for package in _get_package_definitions(schema):
        classes, enums = _get_package_types(schema, package)
        result.append(
            Package(package['name'],
                    package['doc'],
                    classes,
                    enums
                    )
            )

    return result


def create_ontology(schema):
    """Factory method to instantiate an ontology instance from a schema declaration.

    :param module schema: An ontology schema declaration.

    :returns: An ontology declaration.
    :rtype: esdoc_mp.core.Ontology

    """
    return Ontology(schema.NAME,
                    schema.VERSION,
                    schema.DOC,
                    _get_ontology_packages(schema))
