# -*- coding: utf-8 -*-

"""
.. module:: activity_enums.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 activity enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def ensemble_types():
    """Defines the various axes along which one can set up an ensemble.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('Perturbed Physics', 'Members differ in some aspects of their physics'),
            ('Initialisation Method', 'Members differ in how they are initialised'),
            ('Initialisation', 'Members are initialised to sample possible starting states'),
            ('Staggered Start', 'Members are initialised at different starting dates'),
            ('Forced', 'Members used differing forcing data'),
            ('Resolution', 'Members are run at different resolutions'),
        ],
    }


def model_types():
    """Defines a set of gross model classes.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('AGCM', 'GCM without fully dynamic ocean or carbon cycle'),
            ('AOGCM', 'GCM with coupled atmosphere ocean components'),
            ('AMGCM', 'GCM with atmosphere coupled to mixed layer ocean'),
            ('ESM', 'Earth system model including carbon cycle'),
        ]
    }


def forcing_types():
    """Defines the possible set of forcing types for a forcing constraint.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('observed', 'Best estimates of actual state'),
            ('idealised', 'Simplified and/or exemplar, e.g. 1%C02'),
            ('scenario', 'Intended to represent a possible future, e.g. RCP4.5'),
            ('control', 'From another simulation'),
        ]
    }


