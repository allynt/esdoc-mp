# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.core.property
   :platform: Unix, Windows
   :synopsis: Represents an ontological type property definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
from esdoc_mp.core.type import Type



class Property(object):
    """Represents a property within an ontology.

    :ivar name: Property name.
    :ivar doc_string: Property docuemtnation string.
    :ivar type_name: Property type name.
    :ivar cardinality: Type of relationship to associated class (i.e. 0.1 | 1.1 | 0.N | 1.N).

    """

    def __init__(self, name, type_name, cardinality, doc_string):
        """Constructor.

        :param str name: Property name.
        :param str doc_string: Property docuemtnation string.
        :param str type_name: Property type name.
        :param str cardinality: Type of relationship to associated class (i.e. 0.1 | 1.1 | 0.N | 1.N).

        """
        # Defensive programming.
        if name.lower() in ("ext", ):
            raise AttributeError("{0} is a reserved property name.".format(name))

        # Set attributes.
        self.cls = None
        self.decodings = []
        self.doc_string = doc_string if doc_string is not None else ''
        self.cardinality = cardinality
        self.max_occurs = cardinality.split('.')[1]
        self.min_occurs = cardinality.split('.')[0]
        self.name = name
        self.type = Type(type_name)

        # Derived attributes.
        self.is_required = self.min_occurs != '0'
        self.is_iterative = self.max_occurs == 'N'


    def __repr__(self):
        """String representation for debugging."""
        return self.name
