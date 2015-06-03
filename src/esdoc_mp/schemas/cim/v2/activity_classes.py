# -*- coding: utf-8 -*-

"""
.. module:: activity_classes.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 activity package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def activity():
    """Base class for activities.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('canonical_name', 'activity.vocab_member', '0.1'),
            ('duration', 'time.time_period', '0.1'),
            ('description', 'shared.cim_text', '0.1'),
            ('keywords', 'str', '0.N'),
            ('long_name', 'str', '0.1'),
            ('meta', 'shared.meta', '1.1'),
            ('name', 'str', '1.1'),
            ('references', 'shared.citation', '0.N'),
            ('responsible_parties', 'shared.responsibility', '0.N')
        ],
        'doc_strings': {
            'canonical_name': 'Community defined identifier or name',
            'duration': 'Time the activity was (or will be) active',
            'description': 'Textual description of activity',
            'keywords': 'User defined keywords',
            'long_name': 'Longer version of activity name',
            'meta': 'Metadata describing how this document was created',
            'name': 'Short name or abbreviation',
            'references': 'Relevant documentation',
            'responsible_parties': 'People or organisations responsible for activity'
        },
        'renamed_properties': [
            ('responsible_party', 'responsible_parties')
        ]
    }


def configuration():
    """Aggregation of conformance information for a particular configuration of a model for a particular experiment.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract' : False,
        'properties': [
            ('conformances', 'linked_to(activity.conformance)', '1.N'),
            ('description', 'str', '0.1'),
        ],
        'doc_strings': {
            'conformances': 'Individual conformance documents for each requirement',
            'description': 'Description of configuration details for this experiment'
        },
        'renamed_properties': [
            ('conformance', 'conformances')
        ]
    }


def conformance():
    """Conformance information for a particular numerical requirement.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract' : False,
        'properties': [
            ('conformance_detail', 'shared.cim_text', '1.1'),
            ('target_name', 'str', '1.1'),
            ('target_requirement', 'str', '1.1'),
        ],
        'doc_strings': {
            'conformance_detail': 'Detailed information about the conformance',
            'target_name': 'Name of the target numerical requirement',
            'target_requirement': 'URI of the target numerical requirement',
        }
    }


def project():
    """Describes a scientific project.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract' : False,
        'properties': [
            ('previous_projects', 'linked_to(activity.project)', '0.N'),
            ('required_experiments', 'linked_to(activity.numerical_experiment)', '0.N'),
            ('sub_projects', 'linked_to(activity.project)', '0.N'),
        ],
        'doc_strings': {
            'previous_projects': 'Previous projects with similar aims.',
            'required_experiments': 'Experiments required to deliver project.',
            'sub_projects': 'Related sub projects.',
        },
        'constraints': [
            ('description', 'cardinality', '1.1')
        ],
        'renamed_properties': [
            ('follows_from', 'previous_projects'),
            ('requires_experiments', 'required_experiments'),
            ('sub_project', 'sub_projects'),
        ]
    }


def simulation():
    """Provides the integrating link about what models were run and why.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract' : False,
        'properties': [
            ('conformed_via', 'linked_to(activity.configuration)', '0.1'),
            ('had_performance', 'linked_to(platform.performance)', '0.1'),
            ('ran_on', 'linked_to(platform.machine)', '0.1'),
            ('supported', 'linked_to(activity.numerical_experiment)', '1.N'),
            ('used', 'linked_to(software.configured_model)', '1.1'),
        ],
        'doc_strings': {
            'conformed_via': 'Set of conformances to experiment numerical requirements',
            'had_performance': 'Performance of the simulation',
            'ran_on': 'The machine on which the simulation was run',
            'supported': 'An experiment with which the simulation is associated',
            'used': 'The model used to run the simulation'
        }
    }


def simulation_plan():
    """Describes a simulation that needs to be run.

    """
    # FIXME: Consider whether we should have this, or an EnsemblePlan
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract' : False,
        'properties': [
            ('experiments', 'linked_to(activity.numerical_experiment)', '1.N'),
            ('machine', 'linked_to(platform.machine)', '0.1'),
            ('model', 'linked_to(software.configured_model)', '1.1'),
            ('expected_performance', 'linked_to(platform.performance)', '0.1'),
        ],
        'doc_strings': {
            'experiments': 'Experiments with which the planned simulation will be associated',
            'machine': 'The machine on which the simulation will be run',
            'model': 'The model used to run the simulation',
            'expected_performance': 'Performance of the simulation'
        },
        'constraints':[
            ('duration', 'hidden')
        ],
        'renamed_properties': [
            ('will_support', 'experiments'),
            ('will_run_on', 'machine'),
            ('will_use', 'model'),
        ]
    }
