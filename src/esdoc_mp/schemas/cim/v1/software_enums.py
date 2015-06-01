# -*- coding: utf-8 -*-

"""
CIM v1 software package enums.
"""



def component_property_intent_type():
    """Creates and returns instance of component_property_intent_type enum."""
    return {
        'name' : 'component_property_intent_type',
        'is_open' : False,
        'doc' : 'The direction that the associated component property is intended to be coupled: in, out, or inout..',
        'members' : [
            ('in', None),
            ('out', None),
            ('inout', None),
        ],
    }


def connection_type():
    """Creates and returns instance of connection_type enum."""
    return {
        'name' : 'connection_type',
        'is_open' : True,
        'doc' : 'The ConnectionType enumeration describes the mechanism of transport for a connection.',
        'members' : [ ],
    }


def coupling_framework_type():
    """Creates and returns instance of coupling_framework_type enum."""
    return {
        'name' : 'coupling_framework_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('BFG', None),
            ('ESMF', None),
            ('OASIS', None),
        ],
    }


def model_component_type():
    """Creates and returns instance of model_component_type enum."""
    return {
        'name' : 'model_component_type',
        'is_open' : True,
        'doc' : 'An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with "realm" for the purposes of CMIP5.',
        'members' : [ ],
    }


def spatial_regridding_dimension_type():
    """Creates and returns instance of spatial_regridding_dimension_type enum."""
    return {
        'name' : 'spatial_regridding_dimension_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('1D', None),
            ('2D', None),
            ('3D', None),
        ],
    }


def spatial_regridding_standard_method_type():
    """Creates and returns instance of spatial_regridding_standard_method_type enum."""
    return {
        'name' : 'spatial_regridding_standard_method_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('linear', None),
            ('near-neighbour', None),
            ('cubic', None),
            ('conservative-first-order', None),
            ('conservative-second-order', None),
            ('conservative', None),
            ('non-conservative', None),
        ],
    }


def statistical_model_component_type():
    """Creates and returns instance of statistical_model_component_type enum."""
    return {
        'name' : 'statistical_model_component_type',
        'is_open' : True,
        'doc' : 'An enumeration of types of ProcessorComponent.  This includes things like transformers and post-processors.',
        'members' : [ ],
    }


def time_mapping_type():
    """Creates and returns instance of time_mapping_type enum."""
    return {
        'name' : 'time_mapping_type',
        'is_open' : True,
        'doc' : 'Enumerates the different ways that time can be mapped when transforming from one field to another.',
        'members' : [ ],
    }
    

def timing_units():
    """Creates and returns instance of timing_units enum."""
    return {
        'name' : 'timing_units',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('seconds', None),
            ('minutes', None),
            ('hours', None),
            ('days', None),
            ('months', None),
            ('years', None),
            ('decades', None),
            ('centuries', None),
        ],
    }



