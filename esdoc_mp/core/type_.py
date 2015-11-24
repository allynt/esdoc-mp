# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.core.property
   :platform: Unix, Windows
   :synopsis: Represents an ontological type reference definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.core.class_ import Class
from esdoc_mp.core.enum import Enum



class Type(object):
    """Represents a type within an ontology.

    :ivar name: Name of type.

    """

    def __init__(self, name):
        """Instance constructor.

        :param str name: Name of type.

        """
        self._complex_type = None
        self._is_enum = False
        self.is_class = False
        self.is_complex = len(name.split('.')) > 1
        self.is_simple = not self.is_complex
        self.name = name
        self.name_of_package = '' if self.is_simple else name.split('.')[0]
        self.name_of_type = name if self.is_simple else name.split('.')[1]


    def __repr__(self):
        """Instance string representation.

        """
        return self.name


    @property
    def complex_type(self):
        """Gets complex type.

        """
        return self._complex_type


    @complex_type.setter
    def complex_type(self, value):
        """Sets complex type.

        :param Class|Enum value: Name of type.

        """
        if self.is_complex == False:
            raise TypeError("Type is not complex.")
        if isinstance(value, Class) == False and isinstance(value, Enum) == False:
            raise TypeError("Value is of incorrect type.")
        self._complex_type = value
        self._is_enum = isinstance(value, Enum)


    @property
    def is_enum(self):
        """Gets flag indicating whether type represents an enumerated type.

        """
        return self.is_complex and not self.is_class

