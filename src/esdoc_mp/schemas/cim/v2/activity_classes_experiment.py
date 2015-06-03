# -*- coding: utf-8 -*-

"""
.. module:: activity_classes_experiment.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 activity class definitions related to numerical experiments.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def ensemble_requirement():
    """Defines details of experiment ensemble."""
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
            'ensemble_member': 'Constraint on each ensemble member'
        },
        'constraints':[
            ('additional_requirements', 'hidden'),
        ]
    }


def forcing_constraint():
    """Identifies a model forcing constraint.

    """
    return {
        'type': 'class',
        'is_abstract':False,
        'base': 'activity.numerical_requirement',
        'properties': [
            ('code', 'activity.vocab_member', '1.1'),
            ('category', 'activity.vocab_member', '1.1'),
            ('group', 'activity.vocab_member', '0.1'),
            ('forcing_Type', 'activity.forcingTypes', '1.1'),
            ('additional_constraint', 'shared.cim_text', '0.1'),
            ('origin', 'shared.citation', '0.1'),
            ('data_link', 'shared.onlineResource', '0.1')
        ],
        'doc_strings': {
            'code': 'Programme wide code from a controlled vocabulary (e.g. N2O)',
            'category': 'Category to which this belongs (from a CV, e.g. GASES)',
            'group': 'Sub-Category (e.g. GHG)',
            'forcing_Type': 'Type of integration',
            'additional_constraint': 'Additional information, e.g. hold constant from 2100-01-01',
            'origin': 'Pointer to origin, e.g. CMIP6 RCP database',
            'data_link': 'Link to actual data record if possible'
        },
        'constraints':[
            ('additional_requirements', 'hidden'),
        ],
    }


def numerical_experiment():
    """Defines a numerical experiment.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract' : False,
        'properties': [
            ('experiment_id', 'str', '0.1'),
            ('related_experiments', 'linked_to(activity.numerical_experiment)', '0.N'),
            ('requirements', 'linked_to(activity.numerical_requirement)', '0.N'),
        ],
        'doc_strings': {
            'experiment_id': 'Identifier used by experiment community',
            'related_experiments': 'A related experiment',
            'requirements': 'A requirement that a conformant simulation needs to satisfy'
        },
        'constraints': [
            ('duration', 'hidden'),
        ],
        'renamed_properties': [
            ('related_to_experiment', 'related_experiments'),
            ('has_requirements', 'requirements')
        ]
    }


def numerical_requirement():
    """Numerical requirement base class.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract' : False,
        'properties': [
            ('was_conformance_requested', 'bool', '1.1'),
            ('additional_requirements', 'linked_to(activity.numerical_requirement)', '0.N')
        ],
        'doc_strings': {
            'was_conformance_requested': "Indicator as to whether simulation documentation should include conformance information for this requirement",
            'additional_requirements': 'Additional requirement detail'
        },
        'constraints': [
            ('duration', 'hidden')
        ],
        'renamed_properties': [
            ('conformance_requested', 'was_conformance_requested')
        ]
    }


def output_temporal_requirement():
    """Defines gross details of output temporal requirements. Typically output
    will be required in one of three modes: (1) continuous,
    (2) continuos for a set of subset periods, or (3) sliced
    for a set of months in year or days a month.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('throughout', 'bool', '1.1'),
            ('continuous_subset', 'time.time_period', '0.N'),
            ('sliced_subset', 'time.timesliceList', '0.1'),
        ],
        'doc_strings': {
            'throughout': 'Whether or not output is required throughout simulation',
            'continuous_subset': 'Set of periods for which continuous output is required',
            'sliced_subset': 'Description of how slices are laid out',
        },
        'constraints': [
            ('additional_requirements', 'hidden'),
        ]
    }


def temporal_constraint():
    """A temporal constraint on a numerical experiment.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract':False,
        'properties': [
            ('required_duration', 'time.time_period', '0.1'),
            ('required_calendar', 'time.calendar', '0.1'),
            ('start_date', 'time.date_time', '0.1'),
            ('start_flexibility', 'time.time_period', '0.1')
        ],
        'doc_strings': {
            'required_duration': 'Constraint on time or length of simulation',
            'required_calendar': 'Required calendar (e.g. for paleo simulations)',
            'start_date': 'Required start date',
            'start_flexibility': 'Amount of time before required start date that it is permissible to begin integration'
        },
        'constraints':[
            ('additional_requirements', 'hidden')
        ]
    }
