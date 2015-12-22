# -*- coding: utf-8 -*-

"""
.. module:: activity_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def activity():
    """Base class for activities.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('canonical_name', 'str', '0.1',
                "Community defined identifier or name."),
            ('description', 'str', '0.1',
                "Description of what is to be done (or was done)."),
            ('duration', 'shared.time_period', '0.1',
                "Time the activity was (or will be) active."),
            ('keywords', 'str', '0.N',
                "User defined keywords."),
            ('long_name', 'str', '0.1',
                "Longer version of activity name."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata describing how this document was created."),
            ('name', 'str', '1.1',
                "Short name or abbreviation."),
            ('rationale', 'str', '0.1',
                "Explanation of why this activity was carried out and/or what it was intended to achieve."),
            ('references', 'shared.citation', '0.N',
                "Relevant documentation."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "People or organisations responsible for activity.")
        ]
    }


def axis_member():
    """Description of a given ensemble member. It will normally be related to a specific
    ensemble requirement. Note that start dates can be extracted directly from the simulations
    and do not need to be recorded with an axis member description.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '1.1',
                "Description of the member (or name of parameter varied)."),
            ('index', 'int', '1.1',
                "The ensemble member index."),
            ('value', 'float', '0.1',
                "If parameter varied, value thereof for this member.")
        ]
    }


def conformance():
    """A specific conformance. Describes how a particular numerical requirement has been implemented.
    Will normally be linked from an ensemble descriptor.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('target_requirement', 'designing.numerical_requirement', '1.1',
                "URI of the target numerical requirement.")
        ]
    }


def ensemble():
    """Generic ensemble definition.
    Holds the definition of how the various ensemble members have been configured.
    If ensemble axes are not present, then this is either a single member ensemble,
    or part of an uber ensemble.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('common_conformances', 'activity.conformance', '0.N',
                "Conformance documents for requirements common across ensemble."),
            ('has_ensemble_axes', 'activity.ensemble_axis', '0.N',
                "Set of axes for the ensemble."),
            ('members', 'activity.ensemble_member', '1.N',
                "The set of ensemble members."),
            ('part_of', 'activity.uber_ensemble', '0.N',
                "Link to one or more over-arching ensembles that might includes this one."),
            ('supported', 'designing.numerical_experiment', '1.N',
                "Experiments with which the ensemble is associated (may differ from constituent simulations).")
        ]
    }


def ensemble_axis():
    """Defines the meaning of r/i/p indices in an ensemble.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('axis',)),
        'properties': [
            ('extra_detail', 'str', '1.1',
                "Any extra detail required to describe how this ensemble axis was delivered."),
            ('member', 'activity.axis_member', '1.N',
                "Individual member descriptions along axis."),
            ('short_identifier', 'str', '1.1',
                "e.g. 'r' or 'i' or 'p' to conform with simulation ensemble identifier."),
            ('target_requirement', 'designing.numerical_requirement', '1.1',
                "URI of the target numerical requirement.")
        ]
    }


def ensemble_member():
    """An ensemble may be a complicated interplay of axes, for example, r/i/p, not all of which
    are populated, so we need a list of the actual simulations and how they map onto the ensemble
    axes.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('had_performance', 'platform.performance', '0.1',
                "Performance of the simulation."),
            ('ran_on', 'platform.machine', '1.1',
                "The machine on which the simulation was run."),
            ('simulation', 'data.simulation', '1.1',
                "Actual simulation description for an ensemble member.")
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


def parent_simulation():
    """Defines the relationship between a simulation and its parent.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('branch_time_in_child', 'shared.date_time', '0.1',
                "The time at which the present simulation started in the child calendar."),
            ('branch_time_in_parent', 'shared.date_time', '0.1',
                "The time in parent simulation calendar at which this simulation was branched."),
            ('parent', 'data.simulation', '1.1',
                "The parent simulation of this child.")
        ]
    }


def uber_ensemble():
    """An ensemble made up of other ensembles. Often used where parts of an ensemble were run by
    different institutes. Could also be used when a new experiment is designed which can use
    ensemble members from previous experiments and/or projects.

    """
    return {
        'type': 'class',
        'base': 'activity.ensemble',
        'is_abstract': False,
        'properties': [
            ('child_ensembles', 'activity.ensemble', '1.N',
                "Ensemble which are aggregated into this one.")
        ]
    }
