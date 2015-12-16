
# -*- coding: utf-8 -*-

"""
.. module:: software_enums.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 ontology schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""


def coupling_framework():
    """The set of terms which define known coupling frameworks.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("OASIS", "None"),
            ("OASIS3-MCT", "None"),
            ("ESMF", "None"),
            ("NUOPC", "None"),
            ("Bespoke", "Customised coupler developed for this model"),
            ("Unknown", "It is not known what/if-a coupler is used"),
            ("None", "No coupler is used")
		]
    }


def programming_language():
    """The set of terms which define programming languages used for earth
    system simulation.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("Fortran", "None"),
            ("C", "None"),
            ("C++", "None"),
            ("Python", "None")
		]
    }
