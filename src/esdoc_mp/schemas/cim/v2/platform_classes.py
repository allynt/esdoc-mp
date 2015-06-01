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
            ('component', 'software.software_component', '0.1', 'Link to a CIM software component description'),
            ('component_name', 'str', '1.1', 'Short name of component'),
            ('speed', 'float', '1.1', 'Time taken to simulate one real day (s)'),
            # one of these  is needed:
            ('cores_used', 'int', '0.1', 'Number of cores used for this component'),
            ('nodes_used', 'int', '0.1', 'Number of nodes used for this component'),
        ],
    }


def compute_pool():
    """Homogeneous pool of nodes within a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('accelerators_per_node', 'int', '0.1', 'Number of accelerator units on a node'),
            ('accelerator_type', 'str', '0.1', 'Type of accelerator'),
            ('compute_cores_per_node', 'int', '0.1', 'Number of CPU cores per node'),
            ('CPU_type', 'str', '0.1', 'CPU type'),
            ('description', 'shared.cim_text', '0.1', 'Textural description of pool'),
            ('interconnect', 'str', '0.1', 'Interconnect used'),
            ('name', 'str', '0.1', None),
            ('number_of_nodes', 'int', '0.1', 'Number of nodes'),
            ('operating_system', 'str', '0.1', 'Operating system'),
            ('memory_per_node', 'platform.storage_volume', '0.1', 'Memory per node'),
            ('model_number', 'str', '0.1', 'Model/Board number/type'),
        ],
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
            ('meta', 'shared.meta', '1.1', 'Document description'),
        ]
    }


def partition():
    """A description of a partition in a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('compute_pool', 'platform.computePool', '1.N', 'Layout of compute nodes'),
            ('description', 'shared.cim_text', '0.1', 'Textural description of machine'),
            ('institution', 'linked_to(shared.party)', '1.1', 'Institutional location'),
            ('model_number', 'str', '0.1',"Vendor's model number/name - if it exists"),
            ('name', 'str', '1.1', None),
            ('online_documentation', 'shared.onlineResource', '0.N', 'Links to documenation'),
            ('partition', 'platform.partition', '0.N', 'If machine is partitioned, treat subpartitions as machines'),
            ('storage_pool', 'platform.storagePool', '0.N', 'Storage resource available'),
            ('vendor', 'linked_to(shared.party)', '0.1', 'The system integrator or vendor'),
            ('when_used', 'time.time_period', '0.1', 'If no longer in use, the time period it was in use'),
        ]
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
            ('asypd', 'float', '0.1', 'Actual simulated years per wall-clock day, all-in'),
            ('chsy', 'float', '0.1', 'Core-Hours per simulated year'),
            ('coupler_load', 'float', '0.1', 'Percentage of time spent in coupler'),
            ('compiler', 'str', '0.1', 'Compiler used'),
            ('io_load', 'float', '0.1', 'Percentage of time spent in I/O'),
            ('load_imbalance', 'float', '0.1', 'Load imbalance'),
            ('meta', 'shared.meta', '1.1', 'Document metadata'),
            ('name', 'str', '0.1', 'Short name for performance (experiment/test/whatever)'),
            ('memory_bloat', 'float', '0.1', 'Percentage of extra memory needed'),
            ('model', 'linked_to(software.configured_model)', '1.1', 'Model for which performance was tested'),
            ('platform', 'linked_to(platform.machine)', '1.1', 'Platform on which performance was tested'),
            ('subcomponent_performance', 'platform.component_performance', '0.1', 'Describes the performance of each subcomponent'),
            ('sypd', 'float', '0.1', 'Simulated years per wall-clock day'),
            ('total_nodes_used', 'int', '0.1', 'Number of nodes used'),
        ]
    }


def storage_pool():
    """Homogeneous storage pool on a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'shared.cim_text', '0.1', 'Description of the technology used'),
            ('name', 'str', '1.1', 'Name of storage pool'),
            ('type', 'platform.storage_systems', '0.1', 'Type of storage'),
            ('vendor', 'linked_to(shared.party)', '0.1', 'Vendor of the storage unit'),
            ('volume_available', 'platform.storage_volume', '1.1', 'Storage capacity'),
        ]
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
            ('units', 'platform.volume_units', '1.1', 'Volume units'),
            ('volume', 'int', '1.1', 'Numeric value'),
        ]
    }
