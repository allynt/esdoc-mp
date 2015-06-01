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
            ('ensemble_type', 'activity.ensembleTypes', '1.1', 'Type of ensemble'),
            ('minimum_size', 'int', '1.1', 'Minimum number of members'),
            ('ensemble_member', 'linked_to(activity.numerical_requirement)', '0.N',
                'Constraint on each ensemble member'),
            ],
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
            ('code', 'activity.vocab_member', '1.1', 'Programme wide code from a controlled vocabulary (e.g. N2O)'),
            ('category', 'activity.vocab_member', '1.1', 'Category to which this belongs (from a CV, e.g. GASES)'),
            ('group', 'activity.vocab_member', '0.1', 'Sub-Category (e.g. GHG)'),
            ('forcing_Type', 'activity.forcingTypes', '1.1', 'Type of integration'),
            ('additional_constraint', 'shared.cim_text', '0.1', 'Additional information, e.g. hold constant from 2100-01-01'),
            ('origin', 'shared.citation', '0.1', 'Pointer to origin, e.g. CMIP6 RCP database'),
            ('data_link', 'shared.onlineResource', '0.1', 'Link to actual data record if possible')
            ],
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
            ('experiment_id', 'str', '0.1', 'Identifier used by experiment community'),
            ('related_experiments', 'linked_to(activity.numerical_experiment)', '0.N', 'A related experiment'),
            ('requirements', 'linked_to(activity.numerical_requirement)', '0.N', 'A requirement that a conformant simulation needs to satisfy'),
        ],
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
            ('was_conformance_requested', 'bool', '1.1', "Indicator as to whether simulation documentation should include conformance information for this requirement"),
            ('additional_requirements', 'linked_to(activity.numerical_requirement)', '0.N', 'Additional requirement detail')
        ],
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
            ('throughout', 'bool', '1.1', 'Whether or not output is required throughout simulation'),
            ('continuous_subset', 'time.time_period', '0.N', 'Set of periods for which continuous output is required'),
            ('sliced_subset', 'time.timesliceList', '0.1', 'Description of how slices are laid out'),
            ],
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
            ('required_duration', 'time.time_period', '0.1', 'Constraint on time or length of simulation'),
            ('required_calendar', 'time.calendar', '0.1', 'Required calendar (e.g. for paleo simulations)'),
            ('start_date', 'time.date_time', '0.1', 'Required start date'),
            ('start_flexibility', 'time.time_period', '0.1',
                'Amount of time before required start date that it is permissible to begin integration'),
            ],
        'constraints':[
            ('additional_requirements', 'hidden')
        ]
    }


