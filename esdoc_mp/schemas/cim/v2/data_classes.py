# -*- coding: utf-8 -*-

"""
.. module:: data_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def data_association_types():
    """Set of possible dataset associations.
    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("revisonOf", None),
            ("partOf", None),
            ("isComposedOf", None)
        ]
    }


def dataset():
    """Dataset discovery information.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('availability', 'shared.online_resource', '0.N',
                "Where the data is located, and how it is accessed."),
            ('description', 'str', '0.1',
                "Textural description of dataset."),
            ('drs_datasets', 'drs.drs_publication_dataset', '0.N',
                "Data available in the DRS."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata describing the creation of this dataset description document."),
            ('name', 'str', '1.1',
                "Name of dataset."),
            ('produced_by', 'data.simulation', '0.1',
                "Makes a link back to originating activity."),
            ('references', 'shared.citation', '0.N',
                "Relevant reference document."),
            ('related_to_dataset', 'data.related_data', '0.N',
                "Related dataset."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "Individuals and organisations reponsible for the data.")
        ]
    }


def downscaling():
    """Defines a downscaling activity.

    """
    return {
        'type': 'class',
        'base': 'data.simulation',
        'is_abstract': False,
        'properties': [
            ('downscaled_from', 'data.simulation', '1.1',
                "The simulation that was downscaled by this downscaling activity.")
        ]
    }


def related_data():
    """A related dataset and a controlled relationship.

    """
    return {
        'type': 'class',
        'base': 'shared.cim_link',
        'is_abstract': False,
        'properties': [
            ('other_dataset', 'data.dataset', '1.1',
                "Remote dataset."),
            ('relationship', 'data.data_association_types', '1.1',
                "Nature of relationship to the remote dataset.")
        ]
    }


def simulation():
    """Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('calendar', 'shared.calendar', '0.1',
                "The calendar used in the simulation."),
            ('ensemble_identifier', 'str', '1.1',
                "String that can be used to extract ensemble axis membership from the primary ensemble(e.g. cmip6 rip string as in the DRS)."),
            ('parent_simulation', 'activity.parent_simulation', '0.1',
                "If appropriate, detailed information about how this simulation branched from a previous one."),
            ('part_of_project', 'designing.project', '1.N',
                "Project or projects for which simulation was run."),
            ('primary_ensemble', 'activity.ensemble', '0.1',
                "Primary Ensemble (ensemble for which this simulation was first run)."),
            ('ran_for_experiments', 'designing.numerical_experiment', '1.N',
                "One or more experiments with which the simulation is associated."),
            ('used', 'science.model', '1.1',
                "The model used to run the simulation.")
        ]
    }


def variable_collection():
    """A collection of variables within the scope of a code or process element.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('collection_name', 'str', '0.1',
                "Name for this variable collection."),
            ('variables', 'str', '1.N',
                "Set of variable names.")
        ]
    }
