# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.schemas.validation.utils
   :platform: Unix, Windows
   :synopsis: Ontology schema validation utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def parse_type(typeof):
    """Parses a type declaration.

    """
    if typeof.startswith('linked_to'):
        parts = [i.strip() for i in typeof[10:-1].split(",")]
        try:
            return parts[0], parts[1]
        except IndexError:
            return parts[0], None
    else:
        return typeof, None
