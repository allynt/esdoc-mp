# -*- coding: utf-8 -*-

"""
.. module:: activity_classes.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 activity class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def axis_member():
    """Describes an individual ensemble member.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract' : False,
        'properties': [
            ('description', 'str', '1.1'),
            ('index', 'int', '1.1'),
            ('start_date', 'time.date_time', '0.1'),
            ('value', 'float', '0.1'),
        ],
        'doc_strings': {
            'description': 'Description of the member (or name of parameter varied)',
            'index': 'The ensemble member index',
            'start_date': 'Start date of ensemble member',
            'value': 'If parameter varied, value thereof for this member'
        }
    }


def ensemble():
    """Provides the ensemble r/i/p definitions.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract' : False,
        'properties': [
            ('supported', 'linked_to(activity.numerical_experiment)', '1.N'),
            ('simulations_include', 'linked_to(activity.simulation)', '1.N'),
            ('r_defined_by', 'activity.memberDescription', '1.1'),
            ('i_defined_by', 'activity.memberDescription', '1.1'),
            ('p_defined_by', 'activity.memberDescription', '1.1'),
            ('s_defined_by', 'activity.memberDescription', '0.1')
        ],
        'doc_strings': {
            'supported': 'Experiments with which the ensemble is associated (may differ from constituent simulations)',
            'simulations_include': 'Set of simulations with which ensemble is associated',
            'r_defined_by': 'Description of "r" ensemble axis members',
            'i_defined_by': 'Description of "i" ensemble axis members',
            'p_defined_by': 'Description of "p" ensemble axis members',
            's_defined_by': 'Description of start date ensemble axis (if appropriate)'
        }
    }


def ensemble_requirement():
    """Defines details of an experiment ensemble requirement.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract':False,
        'properties': [
            ('ensemble_type', 'activity.ensembleTypes', '1.1'),
            ('minimum_size', 'int', '1.1'),
            ('ensemble_member', 'linked_to(activity.numerical_requirement)', '0.N')
        ],
        'doc_strings': {
            'ensemble_type': 'Type of ensemble',
            'minimum_size': 'Minimum number of members',
            'ensemble_member': 'Constraint on each ensemble member',
        },
        'constraints':[
            ('additional_requirements', 'hidden'),
        ]
    }


def member_description():
    """Defines the r/i/p axes of an ensemble.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract' : False,
        'properties': [
            ('axis', 'activity.ensembleTypes', '1.1'),
            ('description', 'shared.cim_text', '0.1'),
            ('member', 'activity.axis_member', '1.N')
        ],
        'doc_strings': {
            'axis': 'The type of ensemble axis',
            'description': 'Description of ensemble axis',
            'member': 'Individual axis description'
        }
    }


def multi_ensemble():
    """In the case of multiple ensemble axes, defines how they are set up and ordered.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract':False,
        'properties': [
            ('ensemble_axis', 'linked_to(activity.ensembleRequirement)', '1.N'),
        ],
        'doc_strings': {
            'ensemble_axis': 'List of orthogonal ensembles',
        },
        'constraints':[
            ('additional_requirements', 'hidden'),
        ]
    }


def multi_time_ensemble():
     """Defines an experiment ensemble with multiple start dates.

     """
     return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract':False,
        'properties': [
            ('ensemble_members', 'time.datetimeSet', '1.1')
        ],
        'doc_strings': {
            'ensemble_members': 'Description of date or time set of start dates'
        },
        'constraints':[
            ('additional_requirements', 'hidden'),
        ]
    }
