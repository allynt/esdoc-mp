# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.core.class
   :platform: Unix, Windows
   :synopsis: Represents an ontological class definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class Class(object):
    """Represents an ontological class definition.

    """
    def __init__(self, name, base, is_abstract, doc_string, properties, constants, decodings):
        """Instance constructor.

        :param str name: Class name.
        :param str base: Base class used in object hierarchies.
        :param bool is_abstract: Flag indicating whether this is an abstract class or not.
        :param str doc_string: Class documentation string.
        :param set properties: Set of associated properties.
        :param set constants: Set of associated property constants.
        :param set decodings: Set of associated property decodings.

        """
        self.base = base
        self.circular_imports = set()
        self.constants = constants
        self.decodings = set(sorted(decodings, key=lambda dc: dc.property_name))
        self.doc_string = doc_string if doc_string is not None else ''
        self.imports = set()
        self.is_abstract = is_abstract
        self.name = name
        self.op_base_name = None
        self.op_doc_string_name = None
        self.op_file_name = None
        self.op_full_name = None
        self.op_functional_name = None
        self.op_import_name = None
        self.op_name = None
        self.properties = set(sorted(properties, key=lambda p: p.name))
        self.package = None


    def __repr__(self):
        """Instance string representation.

        """
        return self.name


    @property
    def is_entity(self):
        """Gets a flag indicating whether this class is considered an entity.

        """
        return 'meta' in [p.name for p in self.properties]


    @property
    def all_constants(self):
        """Gets all associated constants including those of base class (sorted by name).

        """
        result = set(self.constants)
        if self.base:
            result = result.union(self.base.all_constants)

        return result


    @property
    def all_properties(self):
        """Gets all associated properties including those of base class (sorted by name).

        """
        result = set(self.properties)
        if self.base:
            result = result.union(self.base.all_properties)

        return result


    @property
    def all_decodings(self):
        """Gets class plus base class decodings.

        """
        result = set(self.decodings)
        if self.base:
            result = result.union(self.base.all_decodings)

        return result


    def get_property_decodings(self, prp):
        """Returns set of property decodings.

        :param esdoc_mp.core.Property prp: A property being processed.

        """
        return set(dc for dc in self.all_decodings if dc.property_name == prp.name)


    def get_property(self, name):
        """Recursively gets associated property either from self or from base class.

        :param str name: Name of a property.

        """
        for prp in self.properties:
            if prp.name == name:
                return prp
        if self.base:
            return self.base.get_property(name)
