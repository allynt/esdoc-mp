# -*- coding: utf-8 -*-

"""
.. module:: designing_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def domain_properties():
    """Properties of the domain which needs to be simulated, extend and/or resolution.

    """
    return {
        'type': 'class',
        'base': 'designing.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('required_extent', 'science.extent', '0.1',
                "Constraint on extent of domain to be simulated."),
            ('required_resolution', 'science.resolution', '0.1',
                "Constraint on resolution required in simulated domain.")
        ],
        'constraints': [
            ('additional_requirements', 'cardinality', '0.0')
        ]
    }


def ensemble_requirement():
    """Defines an experiment ensemble.

    """
    return {
        'type': 'class',
        'base': 'designing.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('ensemble_member', 'linked_to(designing.numerical_requirement)', '0.N',
                "Constraint on each ensemble member."),
            ('ensemble_type', 'designing.ensemble_types', '1.1',
                "Type of ensemble."),
            ('minimum_size', 'int', '1.1',
                "Minimum number of members.")
        ],
        'constraints': [
            ('additional_requirements', 'cardinality', '0.0')
        ]
    }


def ensemble_types():
    """Defines the various axes along which one can set up an ensemble.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Perturbed Physics", "Members differ in some aspects of their physics"),
            ("Initialisation Method", "Members differ in how they are initialised"),
            ("Initialisation", "Members are initialised to sample possible starting states"),
            ("Staggered Start", "Members are initialised at different starting dates"),
            ("Forced", "Members used differing forcing data"),
            ("Resolution", "Members are run at different resolutions")
        ]
    }


def experimental_relationships():
    """Defines the canonical set of experimental relationships.

    """
    return {
        'type': 'enum',
        'is_open': True,
        'members': [
            ("control_for", "This experiment provides a control for the target experiment"),
            ("initialisation_for", "This experiment provides initialisation for the target experiment"),
            ("provides_constraints", "This experiment provides constraint(s) for the target experiment (e.g SST forcing)"),
            ("is_sibling", "Part of a family (e.g. experiments where solar forcing is either increased or reduced)")
        ]
    }


def forcing_constraint():
    """Identifies a model forcing constraint.

    """
    return {
        'type': 'class',
        'base': 'designing.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('additional_constraint', 'str', '0.1',
                "Additional information, e.g. hold constant from 2100-01-01."),
            ('category', 'str', '0.1',
                "Category to which this belongs (from a CV, e.g. GASES)."),
            ('code', 'str', '0.1',
                "Programme wide code from a controlled vocabulary (e.g. N2O)."),
            ('data_link', 'shared.online_resource', '0.1',
                "Link to actual data record if possible."),
            ('forcing_type', 'designing.forcing_types', '1.1',
                "Type of integration."),
            ('group', 'str', '0.1',
                "Sub-Category (e.g. GHG)."),
            ('origin', 'shared.reference', '0.1',
                "Pointer to origin, e.g. CMIP6 RCP database.")
        ],
        'constraints': [
            ('additional_requirements', 'cardinality', '0.0')
        ]
    }


def forcing_types():
    """Defines the possible set of forcing types for a forcing constraint.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("historical", "Best estimates of actual state (included synthesized)"),
            ("idealised", "Simplified and/or exemplar, e.g. 1%C02"),
            ("scenario", "Intended to represent a possible future, e.g. RCP4.5"),
            ("another simulation", "From another simulation")
        ]
    }


def multi_ensemble():
    """In the case of multiple ensemble axes, defines how they
    are set up and ordered.

    """
    return {
        'type': 'class',
        'base': 'designing.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('ensemble_axis', 'linked_to(designing.ensemble_requirement)', '1.N',
                "List of orthogonal ensembles.")
        ],
        'constraints': [
            ('additional_requirements', 'cardinality', '0.0')
        ]
    }


def multi_time_ensemble():
    """Defines an experiment ensemble with multiple start dates.

    """
    return {
        'type': 'class',
        'base': 'designing.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('ensemble_members', 'shared.datetime_set', '1.1',
                "Description of date or time set of start dates.")
        ],
        'constraints': [
            ('additional_requirements', 'cardinality', '0.0')
        ]
    }


def numerical_experiment():
    """Defines a numerical experiment.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('related_experiments', 'linked_to(designing.numerical_experiment)', '0.N',
                "A related experiment."),
            ('requirements', 'linked_to(designing.numerical_requirement, designing.experimental_relationships)', '0.N',
                "Requirements that conformant simulations need to satisfy.")
        ],
        'constraints': [
            ('duration', 'cardinality', '0.0'),
            ('rationale', 'cardinality', '1.1')
        ]
    }


def numerical_requirement():
    """A numerical requirement associated with a numerical experiment.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('additional_requirements', 'linked_to(designing.numerical_requirement)', '0.N',
                "Additional detail for this requirement."),
            ('conformance_is_requested', 'bool', '1.1',
                "Indicator as to whether ensemble documentation should include conformance information for this requirement.")
        ],
        'constraints': [
            ('duration', 'cardinality', '0.0')
        ]
    }


def output_temporal_requirement():
    """Provides details of when output is required from an experiment.
    Typically output will be required in one of three modes:
    (1) continuous,
    (2) continuous for a set of subset periods, or
    (3) sliced for a set of months in a year or days in a month.

    """
    return {
        'type': 'class',
        'base': 'designing.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('continuous_subset', 'shared.time_period', '0.N',
                "Set of periods for which continuous output is required."),
            ('sliced_subset', 'shared.timeslice_list', '0.1',
                "Description of how slices are laid out."),
            ('throughout', 'bool', '1.1',
                "Whether or not output is required throughout simulation.")
        ],
        'constraints': [
            ('additional_requirements', 'cardinality', '0.0')
        ]
    }


def project():
    """Describes a scientific project.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('previous_projects', 'linked_to(designing.project)', '0.N',
                "Previous projects with similar aims."),
            ('requires_experiments', 'linked_to(designing.numerical_experiment)', '0.N',
                "Experiments required to deliver project."),
            ('sub_projects', 'linked_to(designing.project)', '0.N',
                "Activities within the project with their own name and aim(s).")
        ],
        'constraints': [
            ('description', 'cardinality', '1.1')
        ]
    }


def simulation_plan():
    """Describes a simulation that needs to be run.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('expected_model', 'linked_to(science.model)', '1.1',
                "The model used to run the simulation."),
            ('expected_performance_sypd', 'float', '0.1',
                "Expected performance in simulated years per real day."),
            ('expected_platform', 'linked_to(platform.machine)', '0.1',
                "The machine on which the simulation will be run."),
            ('will_support_experiments', 'linked_to(designing.numerical_experiment)', '1.N',
                "An experiment with which the planned simulation will be associated.")
        ],
        'constraints': [
            ('duration', 'cardinality', '1.1')
        ]
    }


def temporal_constraint():
    """A temporal constraint on a numerical experiment.

    """
    return {
        'type': 'class',
        'base': 'designing.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('required_calendar', 'shared.calendar', '0.1',
                "Required calendar (e.g. for paleo simulations)."),
            ('required_duration', 'shared.time_period', '0.1',
                "Constraint on time or length of simulation."),
            ('start_date', 'shared.date_time', '0.1',
                "Required start date."),
            ('start_flexibility', 'shared.time_period', '0.1',
                "Amount of time before required start date that it is permissible to begin integration.")
        ],
        'constraints': [
            ('additional_requirements', 'cardinality', '0.0')
        ]
    }