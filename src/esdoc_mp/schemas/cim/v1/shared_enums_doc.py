# -*- coding: utf-8 -*-

"""
CIM v1 shared package enums.
"""

def doc_relationship_direction_type():
    """Creates and returns instance of relationship_direction_type enum."""
    return {
        'type' : 'enum',
        'name' : 'doc_relationship_direction_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('toTarget', None),
            ('fromTarget', None),
        ],
    }


def doc_relationship_type():
    """Creates and returns instance of document_relationship_type enum."""
    return {
        'type' : 'enum',
        'name' : 'doc_relationship_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('similarTo', None),
            ('other', None),
            ('laterVersionOf', None),
            ('previousVersionOf', None),
            ('fixedVersionOf', None),
        ],
    }


def doc_status_type():
    """Creates and returns instance of doc_status_type enum."""
    return {
        'type' : 'enum',
        'name' : 'doc_status_type',
        'is_open' : False,
        'doc' : 'Status of cim document.',
        'members' : [
            ('complete', None),
            ('incomplete', None),
            ('in-progress', None),
        ],
    }


def doc_type():
    """Creates and returns instance of doc_type enum."""
    return {
        'type' : 'enum',
        'name' : 'doc_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('downscalingSimulation', None),
            ('statisticalModelComponent', None),
            ('simulationRun', None),
            ('assimilation', None),
            ('simulationComposite', None),
            ('numericalExperiment', None),
            ('dataProcessing', None),
            ('ensemble', None),
            ('dataObject', None),
            ('gridSpec', None),
            ('cimQuality', None),
            ('platform', None),
            ('processorComponent', None),
            ('modelComponent', None),
        ],
    }



