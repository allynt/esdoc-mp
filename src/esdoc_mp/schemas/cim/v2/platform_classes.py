# -*- coding: utf-8 -*-

"""
.. module:: platform_classes.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 platform package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""

def component_performance():
    """Describes the simulation rate of a component in seconds per model day.

    """
    return {
        'type': 'class',
        'is_abstract': False,
        'base': None,
        'pstr': ('speed %s s/day',('speed',)),
        'properties':[
            ('component', 'software.software_component', '0.1'),
            ('component_name', 'str', '1.1'),
            ('speed', 'float', '1.1'),
            # one of these  is needed:
            ('cores_used', 'int', '0.1'),
            ('nodes_used', 'int', '0.1')
        ],
        'doc_strings': {
            'component': 'Link to a CIM software component description',
            'component_name': 'Short name of component',
            'speed': 'Time taken to simulate one real day (s)',
            'cores_used': 'Number of cores used for this component',
            'nodes_used': 'Number of nodes used for this component'
        }
    }


def compute_pool():
    """Homogeneous pool of nodes within a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('accelerators_per_node', 'int', '0.1'),
            ('accelerator_type', 'str', '0.1'),
            ('compute_cores_per_node', 'int', '0.1'),
            ('CPU_type', 'str', '0.1'),
            ('description', 'shared.cim_text', '0.1'),
            ('interconnect', 'str', '0.1'),
            ('name', 'str', '0.1'),
            ('number_of_nodes', 'int', '0.1'),
            ('operating_system', 'str', '0.1'),
            ('memory_per_node', 'platform.storage_volume', '0.1'),
            ('model_number', 'str', '0.1')
        ],
        'doc_strings': {
            'accelerators_per_node': 'Number of accelerator units on a node',
            'accelerator_type': 'Type of accelerator',
            'compute_cores_per_node': 'Number of CPU cores per node',
            'CPU_type': 'CPU type',
            'description': 'Textural description of pool',
            'interconnect': 'Interconnect used',
            'number_of_nodes': 'Number of nodes',
            'operating_system': 'Operating system',
            'memory_per_node': 'Memory per node',
            'model_number': 'Model/Board number/type'
        },
        'derived': [
            ('total_cores', 'compute_cores_per_node * number_of_nodes'),
            ('total_memory', 'memory_per_node * number_of_nodes'),
        ]
    }


def machine():
    """A description of an independent computing machine.

    """
    return {
        'type': 'class',
        'base': 'platform.partition',
        'is_abstract': False,
        'properties': [
            ('meta', 'shared.meta', '1.1')
        ],
        'doc_strings': {
            'meta': 'Document description',
        }
    }


def partition():
    """A description of a partition in a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('compute_pool', 'platform.computePool', '1.N'),
            ('description', 'shared.cim_text', '0.1'),
            ('institution', 'linked_to(shared.party)', '1.1'),
            ('model_number', 'str', '0.1'),
            ('name', 'str', '1.1'),
            ('online_documentation', 'shared.onlineResource', '0.N'),
            ('partition', 'platform.partition', '0.N'),
            ('storage_pool', 'platform.storagePool', '0.N'),
            ('vendor', 'linked_to(shared.party)', '0.1'),
            ('when_used', 'time.time_period', '0.1')
        ],
        'doc_strings': {
            'compute_pool': 'Layout of compute nodes',
            'description': 'Textural description of machine',
            'institution': 'Institutional location',
            'model_number': 'Vendor"s model number/name - if it exists',
            'online_documentation': 'Links to documenation',
            'partition': 'If machine is partitioned, treat subpartitions as machines',
            'storage_pool': 'Storage resource available',
            'vendor': 'The system integrator or vendor',
            'when_used': 'If no longer in use, the time period it was in use'
        }
    }


def performance():
    """Describes the properties of a performance of a configured model on a machine.

    """
    return {
        'type':'class',
        'base':None,
        'is_abstract':False,
        'pstr':('%s (sypd:%s)',('name', 'sypd',)),
        'properties':[
            ('asypd', 'float', '0.1'),
            ('chsy', 'float', '0.1'),
            ('coupler_load', 'float', '0.1'),
            ('compiler', 'str', '0.1'),
            ('io_load', 'float', '0.1'),
            ('load_imbalance', 'float', '0.1'),
            ('meta', 'shared.meta', '1.1'),
            ('name', 'str', '0.1'),
            ('memory_bloat', 'float', '0.1'),
            ('model', 'linked_to(software.configured_model)', '1.1'),
            ('platform', 'linked_to(platform.machine)', '1.1'),
            ('subcomponent_performance', 'platform.component_performance', '0.1'),
            ('sypd', 'float', '0.1'),
            ('total_nodes_used', 'int', '0.1')
        ],
        'doc_strings': {
            'asypd': 'Actual simulated years per wall-clock day, all-in',
            'chsy': 'Core-Hours per simulated year',
            'coupler_load': 'Percentage of time spent in coupler',
            'compiler': 'Compiler used',
            'io_load': 'Percentage of time spent in I/O',
            'load_imbalance': 'Load imbalance',
            'meta': 'Document metadata',
            'name': 'Short name for performance (experiment/test/whatever)',
            'memory_bloat': 'Percentage of extra memory needed',
            'model': 'Model for which performance was tested',
            'platform': 'Platform on which performance was tested',
            'subcomponent_performance': 'Describes the performance of each subcomponent',
            'sypd': 'Simulated years per wall-clock day',
            'total_nodes_used': 'Number of nodes used'
        }
    }


def storage_pool():
    """Homogeneous storage pool on a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'shared.cim_text', '0.1'),
            ('name', 'str', '1.1'),
            ('type', 'platform.storage_systems', '0.1'),
            ('vendor', 'linked_to(shared.party)', '0.1'),
            ('volume_available', 'platform.storage_volume', '1.1')
        ],
        'doc_strings': {
            'description': 'Description of the technology used',
            'name': 'Name of storage pool',
            'type': 'Type of storage',
            'vendor': 'Vendor of the storage unit',
            'volume_available': 'Storage capacity'
        }
    }


def storage_volume():
    """Volume and units.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s %s',('volume', 'units')),
        'properties': [
            ('units', 'platform.volume_units', '1.1'),
            ('volume', 'int', '1.1'),
        ],
        'doc_strings': {
            'units': 'Volume units',
            'volume': 'Numeric value'
        }
    }
