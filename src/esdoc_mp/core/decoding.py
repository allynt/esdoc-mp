# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.core.decoding
   :platform: Unix, Windows
   :synopsis: Represents an ontological decoding definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class Decoding(object):
    """Represents information used for decoding from a non-standard representation, e.g. Metafor CIM XML.

    :ivar property_name: Name of property with which decoding is associated.
    :ivar decoding: Decoding information (e.g. an xpath expression).
    :ivar type: Target type to be decoded (either a class or enum).

    """

    def __init__(self, property_name, decoding, type):
        """Constructor.

        :param property_name: Name of property with which decoding is associated.
        :type property_name: str
        
        :param decoding: Decoding information (e.g. an xpath expression).
        :type decoding: str

        :param type: Target type to be decoded (either a class or enum).
        :type type: str | None
        
        """
        # Set attributes.
        self.property_name = property_name
        self.decoding = decoding
        self.type = type
