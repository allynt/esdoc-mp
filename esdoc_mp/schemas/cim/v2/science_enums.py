
# -*- coding: utf-8 -*-

"""
.. module:: science_enums.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 ontology schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""


def grid_layouts():
    """Defines the set of grid layouts (e.g. Arakawa C-Grid) which are understood.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("Arakawa-C", "Arakawa C Grid")
		]
    }


def grid_types():
    """Defines the set of grid types (e.g Cubed Sphere) which are understood.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("LatLon", "Standard lat-lon grid"),
            ("Cubed-Sphere", "Cubed sphere grid"),
            ("Spectral-Gaussian", "Spectral with Gaussian grid")
		]
    }


def model_types():
    """Defines a set of gross model classes.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("Atm Only", "Atmosphere Only"),
            ("Ocean Only", "Ocean Only"),
            ("Regional", "Regional Model"),
            ("GCM", "Global Climate Model (Atmosphere, Ocean, no carbon cycle)"),
            ("IGCM", "Intermediate Complexity GCM"),
            ("GCM-MLO", "GCM with mixed layer ocean"),
            ("Mesoscale", "Mesoscale Model"),
            ("Process", "Limited Area process model"),
            ("Planetary", "Non-Earth model")
		]
    }
