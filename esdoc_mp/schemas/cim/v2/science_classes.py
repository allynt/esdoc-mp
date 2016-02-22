# -*- coding: utf-8 -*-

"""
.. module:: science_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def algorithm():
    """Used to hold information associated with an algorithm which implements some key
    part of a process. In most cases this is quite a high level concept and isn't intended
    to describe the gory detail of how the code implements the algorithm rather the key
    scientific aspects of the algorithm. In particular, it provides a method
    of grouping variables which take part in an algorithm within a process.

    """
    return {
        'type': 'class',
        'base': 'science.science_context',
        'is_abstract': False,
        'properties': [
            ('climatology_variables', 'data.variable_collection', '0.1',
                "None"),
            ('diagnostic_variables', 'data.variable_collection', '0.1',
                "Diagnostic variables associated with this algorithm."),
            ('implementation_overview', 'str', '1.1',
                "Overview of the algorithm implementation."),
            ('prognostic_variables', 'data.variable_collection', '0.1',
                "Prognostic variables associated with this algorithm."),
            ('references', 'shared.reference', '0.N',
                "Relevant references.")
        ]
    }


def conservation_properties():
    """Describes how prognostic variables are conserved.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('corrected_conserved_prognostic_variables', 'data.variable_collection', '0.1',
                "Set of variables which are conserved by *more* than the numerical scheme alone."),
            ('correction_methodology', 'str', '0.1',
                "Description of method by which correction was achieved."),
            ('flux_correction_was_used', 'bool', '1.1',
                "Flag to indicate if correction involved flux correction.")
        ]
    }


def extent():
    """Key scientific characteristics of the grid use to simulate a specific domain.
    Note that the extent does not itself describe a grid, so, for example, a polar
    stereographic grid may have an extent of northern boundary 90N, southern boundary
    45N, but the fact that it is PS comes from the grid_type.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('region_known_as',)),
        'properties': [
            ('eastern_boundary', 'float', '0.1',
                "If not global, eastern boundary in degrees of longitude."),
            ('is_global', 'bool', '1.1',
                "True if horizontal coverage is global."),
            ('maximum_vertical_level', 'float', '0.1',
                "Maximum vertical level."),
            ('minimum_vertical_level', 'float', '0.1',
                "Minimum vertical level."),
            ('northern_boundary', 'float', '0.1',
                "If not global, northern boundary in degrees of latitude."),
            ('region_known_as', 'str', '0.N',
                "Identifier or identifiers for the region covered by the extent."),
            ('southern_boundary', 'float', '0.1',
                "If not global, southern boundary in degrees of latitude."),
            ('western_boundary', 'float', '0.1',
                "If not global, western boundary in degrees of longitude."),
            ('z_units', 'str', '1.1',
                "Units of vertical measure.")
        ]
    }


