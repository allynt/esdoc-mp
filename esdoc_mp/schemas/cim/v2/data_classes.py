
# -*- coding: utf-8 -*-

"""
.. module:: data_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 ontology schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""


def data_association_types():
    """Set of possible dataset associations.
    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
			("revisonOf", "None"),
			("partOf", "None"),
			("isComposedOf", "None")
		]
    }


def dataset():
    """Dataset discovery information.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("availability", "shared.online_resource", "0.N"),
			("description", "str", "0.1"),
			("drs_datasets", "drs.drs_publication_dataset", "0.N"),
			("meta", "shared.doc_meta_info", "1.1"),
			("name", "str", "1.1"),
			("produced_by", "data.simulation", "0.1"),
			("produced_by_reference", "shared.doc_reference", "0.1"),
			("references", "shared.citation", "0.N"),
			("related_to_dataset", "data.related_data", "0.N"),
			("responsible_parties", "shared.responsibility", "0.N"),
			("responsible_parties_references", "shared.doc_reference", "0.N")
        ],
        "doc_strings": {
			"availability": "Where the data is located, and how it is accessed",
			"description": "Textural description of dataset",
			"drs_datasets": "Data available in the DRS",
			"meta": "Metadata describing the creation of this dataset description document.",
			"name": "Name of dataset",
			"produced_by": "Makes a link back to originating activity",
			"references": "Relevant reference document",
			"related_to_dataset": "Related dataset",
			"responsible_parties": "Individuals and organisations reponsible for the data"
        }
    }


def downscaling():
    """Defines a downscaling activity.

    """
    return {
        "type": "class",
        "base": "data.simulation",
        "is_abstract": False,
        "properties": [
			("downscaled_from", "data.simulation", "1.1"),
			("downscaled_from_reference", "shared.doc_reference", "1.1")
        ],
        "doc_strings": {
			"downscaled_from": "The simulation that was downscaled by this downscaling activity"
        }
    }


def related_data():
    """A related dataset and a controlled relationship.

    """
    return {
        "type": "class",
        "base": "shared.cim_link",
        "is_abstract": False,
        "properties": [
			("other_dataset", "data.dataset", "1.1"),
			("other_dataset_reference", "shared.doc_reference", "1.1"),
			("relationship", "data.data_association_types", "1.1")
        ],
        "doc_strings": {
			"other_dataset": "Remote dataset",
			"relationship": "Nature of relationship to the remote dataset"
        }
    }


def simulation():
    """Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

    """
    return {
        "type": "class",
        "base": "activity.activity",
        "is_abstract": False,
        "properties": [
			("calendar", "shared.calendar", "0.1"),
			("ensemble_identifier", "str", "1.1"),
			("parent_simulation", "activity.parent_simulation", "0.1"),
			("part_of_project", "designing.project", "1.N"),
			("part_of_project_references", "shared.doc_reference", "1.N"),
			("primary_ensemble", "activity.ensemble", "0.1"),
			("primary_ensemble_reference", "shared.doc_reference", "0.1"),
			("ran_for_experiments", "designing.numerical_experiment", "1.N"),
			("ran_for_experiments_references", "shared.doc_reference", "1.N"),
			("used", "science.model", "1.1"),
			("used_reference", "shared.doc_reference", "1.1")
        ],
        "doc_strings": {
			"calendar": "The calendar used in the simulation",
			"ensemble_identifier": "String that can be used to extract ensemble axis membership from the primary ensemble(e.g. cmip6 rip string as in the DRS)",
			"parent_simulation": "If appropriate, detailed information about how this simulation branched from a previous one",
			"part_of_project": "Project or projects for which simulation was run",
			"primary_ensemble": "Primary Ensemble (ensemble for which this simulation was first run).",
			"ran_for_experiments": "One or more experiments with which the simulation is associated",
			"used": "The model used to run the simulation"
        }
    }


def variable_collection():
    """A collection of variables within the scope of a code or process element.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("collection_name", "str", "0.1"),
			("variables", "str", "1.N")
        ],
        "doc_strings": {
			"collection_name": "Name for this variable collection",
			"variables": "Set of variable names"
        }
    }
