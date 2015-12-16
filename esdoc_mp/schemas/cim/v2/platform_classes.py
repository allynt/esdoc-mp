
# -*- coding: utf-8 -*-

"""
.. module:: platform_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 ontology schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""


def component_performance():
    """Describes the simulation rate of a component in seconds per model day.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("component", "software.software_component", "0.1"),
            ("component_name", "str", "1.1"),
            ("cores_used", "int", "0.1"),
            ("nodes_used", "int", "0.1"),
            ("speed", "float", "1.1")
        ],
        "doc_strings": {
			"component": "Link to a CIM software component description",
			"component_name": "Short name of component",
			"cores_used": "Number of cores used for this component",
			"nodes_used": "Number of nodes used for this component",
			"speed": "Time taken to simulate one real day (s)"
        }
    }


def compute_pool():
    """Homogeneous pool of nodes within a computing machine.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("accelerator_type", "str", "0.1"),
            ("accelerators_per_node", "int", "0.1"),
            ("compute_cores_per_node", "int", "0.1"),
            ("cpu_type", "str", "0.1"),
            ("description", "str", "0.1"),
            ("interconnect", "str", "0.1"),
            ("memory_per_node", "platform.storage_volume", "0.1"),
            ("model_number", "str", "0.1"),
            ("name", "str", "0.1"),
            ("number_of_nodes", "int", "0.1"),
            ("operating_system", "str", "0.1")
        ],
        "doc_strings": {
			"accelerator_type": "Type of accelerator",
			"accelerators_per_node": "Number of accelerator units on a node",
			"compute_cores_per_node": "Number of CPU cores per node",
			"cpu_type": "CPU type",
			"description": "Textural description of pool",
			"interconnect": "Interconnect used",
			"memory_per_node": "Memory per node",
			"model_number": "Model/Board number/type",
			"name": "Name of compute pool within a machine",
			"number_of_nodes": "Number of nodes",
			"operating_system": "Operating system"
        }
    }


def machine():
    """A computer/system/platform/machine which is used for simulation.

    """
    return {
        "type": "class",
        "base": "platform.partition",
        "is_abstract": False,
        "properties": [
            ("meta", "shared.doc_meta_info", "1.1")
        ],
        "doc_strings": {
			"meta": "Document description"
        }
    }


def partition():
    """A major partition (component) of a computing system (aka machine).

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("institution_reference", "shared.doc_reference", "1.1"),
			("vendor_reference", "shared.doc_reference", "0.1"),
            ("compute_pools", "platform.compute_pool", "1.N"),
            ("description", "str", "0.1"),
            ("institution", "shared.party", "1.1"),
            ("model_number", "str", "0.1"),
            ("name", "str", "1.1"),
            ("online_documentation", "shared.online_resource", "0.N"),
            ("partition", "platform.partition", "0.N"),
            ("storage_pools", "platform.storage_pool", "0.N"),
            ("vendor", "shared.party", "0.1"),
            ("when_used", "shared.time_period", "0.1")
        ],
        "doc_strings": {
			"compute_pools": "Layout of compute nodes",
			"description": "Textural description of machine",
			"institution": "Institutional location",
			"model_number": "Vendor's model number/name - if it exists",
			"name": "Name of partition (or machine)",
			"online_documentation": "Links to documentation",
			"partition": "If machine is partitioned, treat subpartitions as machines",
			"storage_pools": "Storage resource available",
			"vendor": "The system integrator or vendor",
			"when_used": "If no longer in use, the time period it was in use"
        }
    }


def performance():
    """Describes the properties of a performance of a configured model on a particular system/machine.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("model_reference", "shared.doc_reference", "1.1"),
			("platform_reference", "shared.doc_reference", "1.1"),
            ("asypd", "float", "0.1"),
            ("chsy", "float", "0.1"),
            ("compiler", "str", "0.1"),
            ("coupler_load", "float", "0.1"),
            ("io_load", "float", "0.1"),
            ("load_imbalance", "float", "0.1"),
            ("memory_bloat", "float", "0.1"),
            ("meta", "shared.doc_meta_info", "1.1"),
            ("model", "science.model", "1.1"),
            ("name", "str", "0.1"),
            ("platform", "platform.machine", "1.1"),
            ("subcomponent_performance", "platform.component_performance", "0.1"),
            ("sypd", "float", "0.1"),
            ("total_nodes_used", "int", "0.1")
        ],
        "doc_strings": {
			"asypd": "Actual simulated years per wall-clock day, all-in",
			"chsy": "Core-Hours per simulated year",
			"compiler": "Compiler used",
			"coupler_load": "Percentage of time spent in coupler",
			"io_load": "Percentage of time spent in I/O",
			"load_imbalance": "Load imbalance",
			"memory_bloat": "Percentage of extra memory needed",
			"meta": "Document metadata",
			"model": "Model for which performance was tested",
			"name": "Short name for performance (experiment/test/whatever)",
			"platform": "Platform on which performance was tested",
			"subcomponent_performance": "Describes the performance of each subcomponent",
			"sypd": "Simulated years per wall-clock day",
			"total_nodes_used": "Number of nodes used"
        }
    }


def storage_pool():
    """Homogeneous storage pool on a computing machine.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("vendor_reference", "shared.doc_reference", "0.1"),
            ("description", "str", "0.1"),
            ("name", "str", "1.1"),
            ("type", "platform.storage_systems", "0.1"),
            ("vendor", "shared.party", "0.1"),
            ("volume_available", "platform.storage_volume", "1.1")
        ],
        "doc_strings": {
			"description": "Description of the technology used",
			"name": "Name of storage pool",
			"type": "Type of storage",
			"vendor": "Vendor of the storage unit",
			"volume_available": "Storage capacity"
        }
    }


def storage_systems():
    """Controlled vocabulary for storage  types (including filesystems).

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
			("Lustre", "None"),
			("GPFS", "None"),
			("isilon", "None"),
			("NFS", "None"),
			("Panasas", "None"),
			("Other Disk", "None"),
			("Tape - MARS", "None"),
			("Tape - MASS", "None"),
			("Tape - Castor", "None"),
			("Tape - Other", "None"),
			("Unknown", "None")
		]
    }


def storage_volume():
    """Volume and units.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("units", "platform.volume_units", "1.1"),
            ("volume", "int", "1.1")
        ],
        "doc_strings": {
			"units": "Volume units",
			"volume": "Numeric value"
        }
    }


def volume_units():
    """Appropriate storage volume units.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
			("GB", "Gigabytes (1000^3)"),
			("TB", "Terabytes (1000^4)"),
			("PB", "Petabytes (1000^5)"),
			("EB", "Exabytes (1000^6)"),
			("TiB", "Tebibytes (1024^4)"),
			("PiB", "Pebibytes (1024^5)"),
			("EiB", "Exbibytes (1024^6)")
		]
    }
