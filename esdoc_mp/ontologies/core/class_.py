# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.ontologies.core.class
   :platform: Unix, Windows
   :synopsis: Represents an ontological class definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import itertools
from collections import defaultdict

import constants


class Class(object):
    """Represents an ontological class definition.

    """
    def __init__(self,
                 name,
                 base,
                 is_abstract,
                 doc_string,
                 properties,
                 computed_properties,
                 constraints,
                 decodings
                 ):
        """Instance constructor.

        :param str name: Class name.
        :param str base: Base class used in object hierarchies.
        :param bool is_abstract: Flag indicating whether this is an abstract class or not.
        :param str doc_string: Class documentation string.
        :param set properties: Set of associated properties.
        :param set computed_properties: Set of associated computed properties.
        :param set constraints: Set of associated constraints.
        :param set decodings: Set of associated property decodings.

        """
        self.base = base
        self.circular_imports = set()
        self.cls = None
        self.computed_properties = set(sorted(computed_properties, key=lambda p: p.name))
        self.constraints = set(sorted(constraints, key=lambda ct: ct.property_name))
        self.decodings = set(sorted(decodings, key=lambda dc: dc.property_name))
        self.doc_string = doc_string if doc_string is not None else ''
        self.imports = set()
        self.is_abstract = is_abstract
        self.name = name

        self.op_base_name = None
        self.op_doc_string_name = None
        self.op_file_name = None
        self.op_full_name = None
        self.op_func_name = None
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
        if 'meta' in [p.name for p in self.properties]:
            return True
        if self.base:
            return self.base.is_entity
        return False


    @property
    def constants(self):
        """Gets collection of constant constraints.

        """
        return [(ct.property_name, ct.value) for ct in self.constraints
                if ct.typeof == constants.CONSTRAINT_TYPE_CONSTANT]


    @property
    def all_constraints(self):
        """Gets all associated constraints including those of base class (sorted by name).

        Note that child constraints overrides parent constraints.

        """
        result = defaultdict(lambda: defaultdict(list))

        # Own constraints.
        for ct in self.constraints:
            if ct.property_name not in result[ct.typeof]:
                result[ct.typeof][ct.property_name] = (ct.property_name, ct.typeof, ct.value)

        # Base class(es) constraints.
        if self.base:
            for ct in self.base.constraints:
                if ct.property_name not in result[ct.typeof]:
                    result[ct.typeof][ct.property_name] = (ct.property_name, ct.typeof, ct.value)

        # Own properties converted to constraints.
        for p in self.all_properties:
            if p.name not in result['cardinality']:
                result['cardinality'][p.name] = (p.name, "cardinality", p.cardinality)
            if p.name not in result['type']:
                result['type'][p.name] = (p.name, "type", p.type)

        return list(itertools.chain.from_iterable([v.values() for v in result.values()]))


    @property
    def all_properties(self):
        """Gets all associated properties including those of base class (sorted by name).

        """
        if self.base:
            return set(self.properties).union(self.base.all_properties)
        return set(self.properties)


    @property
    def all_computed_properties(self):
        """Gets all associated computed properties including those of base class (sorted by name).

        """
        if self.base:
            return set(self.computed_properties).union(self.base.all_computed_properties)
        return set(self.computed_properties)


    @property
    def all_decodings(self):
        """Gets class plus base class decodings.

        """
        if self.base:
            return set(self.decodings).union(self.base.all_decodings)
        return set(self.decodings)


    def get_property_decodings(self, prp):
        """Returns set of property decodings.

        :param esdoc_mp.ontologies.core.Property prp: A property being processed.

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

