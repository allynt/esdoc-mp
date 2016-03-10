__author__ = 'eguil'
version = '0.0.1'

#
# CMIP6 ocean vertical physics CV
#

PROPERTIES = {

    'type' : 'science.process',

    ## NOTE: This is only time in this file when a CIM2 type is
    ##       mentioned ('science.process'). I think we need to mention
    ##       it somewhere - what if, sometime, we wanted to have
    ##       sub-processes in a different file? We'd be glad of the
    ##       'type' key ...

    # Scientific context and properties
    'short_name': 'Ocean vertical physics',
    'description': 'Properties of vertical physics within the ocean component',
    'implementation_overview': 'Overview of implementation',

    ## NOTE: 'short_name' <=> 'name'
    ##       'description' <=> 'context'
    
    # References
    'references': [],
    
    # Detail collections
    'detail_collections': ['vertphys_attributes']
    
    # Sub-processes
    'sub_processes' : ['ocean_bndlayer_mixing'
                       'ocean_interior_mixing'],
    
    # Algorithms
    'algorithms': [],
    
    # ----------------------------------------------------------------
    # TOP-LEVEL DETAIL COLLECTIONS
    # ----------------------------------------------------------------
  
    # Detail collection of process
    'vertphys_attributes': {
        'description': 'Properties of vertical physics in ocean',
        'short_name': 'Properties of vertical physics in ocean',
        'convection_type': ('ENUM:vertphys_convection_types', '1.1')
        
        ## NOTE: The 'convection_type' property takes its value from
        ##       an enum and doesn't need a description (3rd element
        ##       of tuple) because the description is in the enum in
        ##       the ENUMS dictionary below

        'tide_induced_mixing': ('str', '1.1',
                                'Describe how tide induced mixing is modelled (barotropic, baroclinic, none)'),
        'langmuir_cells_mixing': ('bool', '1.1',
                                  'Is there Langmuir cells mixing in upper ocean ?'),
    },
    
    ## NOTE: The type of the detail collection 'vertphys_attributes'
    ##       does not need to be spelled out in this nested dictionary
    ##       - it is specified in 'science.process', How?
    ##       'vertphys_attributes' is in the 'detail_collections' list
    ##       above and a 'science.process' object knows that its
    ##       'detail_collections' property contains a list of
    ##       'science.detail_collection' objects. Validation will
    ##       check that the content of 'vertphys_attributes' is
    ##       appropriate to a 'science.detail_collection'.
    
    # ----------------------------------------------------------------
    # TOP-LEVEL SUB-PROCESSES
    # ----------------------------------------------------------------
    
    # Sub-process
    'bndlayer_mixing': {
        # Scientific context and properties
        'short_name': 'Ocean boundary layer mixing',
        'description': 'Key properties of boundary layer mixing in the ocean (aka mixed layer)',
        
        'detail_collections': ['bndlayer_mixing_tracers',
                               'bndlayer_mixing_momentum'],
        
        # Detail collection of sub-process
        'bndlayer_mixing_tracers': {           
            'description': 'Properties of boundary layer mixing on tracers in ocean',
            'short_name': 'Properties of boundary layer mixing on tracers in ocean',
            'boundary_layer_mixing_type': ('ENUM:vertphys_bndlayer_mixing_types', '1.1')
            'OML_tracers_turbulent_closure_order': ('float','0.1',
                                                    'If turbulent BL mixing of tracers, specific order of closure (0, 1, 2.5, 3)'),
            'OML_tracers_constant': ('int','0.1',
                                     'If constant BL mixing of tracers, specific coefficient (m2/s)'),
            'OML_tracers_background': ('str','1.1',
                                       'Background BL mixing of tracers coefficient, (schema and value in m2/s - may by none)'),
        },
        
        # Detail collection of sub-process
        'bndlayer_mixing_momentum': {
            'description', 'Properties of boundary layer mixing on momentum in ocean',
            'short_name', 'Properties of boundary layer mixing on momentum in ocean',
            'boundary_layer_mixing_type': ('ENUM:vertphys_bndlayer_mixing_types', '1.1'),
            'OML_momentum_turbulent_closure_order': ('float','0.1',
                                                     'If turbulent BL mixing of momentum, specific order of closure (0, 1, 2.5, 3)'),
            'OML_momentum_constant': ('int','0.1',
                                      'If constant BL mixing of momentum, specific coefficient (m2/s)'),
            'OML_momentum_background': ('str', '1.1',
                                        'Background BL mixing of momentum coefficient, (schema and value in m2/s - may by none)'),
        },
    },
    
    ## NOTE: The type of the 'bndlayer_mixing' sub-process does not
    ##       need to be spelled out here - it is specified in
    ##       'science.process', How? 'bndlayer_mixing' is in the
    ##       'sub_processes' list above and a 'science.process' object
    ##       knows that its 'sub_processes' property contains a list
    ##       of 'science.sub_process' objects. Validation will check
    ##       that the content of 'bndlayer_mixing' is appropriate to a
    ##       'science.sub_process'.
        
    # Sub-process
    'sub_process:ocean_interior_mixing' : {
        'short_name': 'Ocean interior mixing',
        'description': 'Key properties of interior mixing in the ocean',
        
        'detail_collections': ['interior_mixing_tracers',
                               'ocean_interior_mixing_momentum'],
        
        # Detail collection of sub-process
        'interior_mixing_tracers': {
            'description': 'Properties of interior mixing on tracers in ocean',
            'short_name': 'Properties of interior mixing on tracers in ocean',
            'boundary_layer_mixing_type': ('ENUM:interior_mixing_types', '1.1'),
            'interior_tracers_constant': ('int','0.1',
                                          'If constant interior mixing of tracers, specific coefficient (m2/s)'),
            'interior_tracers_profile': ('char','1.1',
                                         'Is the background interior mixing using a vertical profile for tracers (i.e is NOT constant) ?'),
            'interior_tracers_background': ('str','1.1',
                                            'Background interior mixing of tra,cers, (schema and coeff. value in m2/s - may by none)'),
        },

        ## NOTE: The type of the detail collection
        ##       'interior_mixing_tracers' does not need to be spelled
        ##       out in this nested dictionary - it is specified in
        ##       'science.sub_process', How? 'interior_mixing_tracers'
        ##       is in the 'detail_collections' list above and a
        ##       'science.sub_process' object knows that its
        ##       'detail_collections' property contains a list of
        ##       'science.detail_collection' objects. Validation will
        ##       check that the content of 'interior_mixing_tracers'
        ##       is appropriate to a 'science.detail_collection'.
        
        # Detail collection of sub-process
        'interior_mixing_momentum': {
            'description': 'Properties of interior mixing on momentum in ocean',
            'short_name': 'Properties of interior mixing on momentum in ocean',
            'boundary_layer_mixing_type': ('ENUM:interior_mixing_types', '1.1'),
            'interior_momentum_constant': ('int','0.1',
                                           'If constant interior mixing of momentum, specific coefficient (m2/s)'),
            'interior_momentum_profile': ('str','1.1',
                                          'Is the background interior mixing using a vertical profile for momentum (i.e is NOT constant) ?'),
            'interior_momentum_background': ('str','1.1',
                                             'Background interior mixing of momentum, (schema and coeff. value in m2/s - may by none)'),
        },
    },
}

ENUMS = {                                        
    'vertphys_convection_types': {
        'description': 'Types of convection scheme in ocean',

        ## NOTE: The enum contains its description

        'members': [
            ('Non-penetrative convective adjustment', 'tbd'),
            ('Enhanced vertical diffusion', 'tbd'),
            ('Included in turbulence closure', 'tbd'),
            ('Other', 'tbd'),
        ]
    },

    'bndayer_mixing_types': {
        'description': 'Types of boundary layer mixing in ocean',
        'members': [
            ('Constant value', 'tbd'),
            ('Turbulent closure - TKE', 'tbd'),
            ('Turbulent closure - KPP', 'tbd'),
            ('Turbulent closure - Mellor-Yamada', 'tbd'),
            ('Turbulent closure - Bulk Mixed Layer', 'tbd'),
            ('Richardson number dependent - PP', 'tbd'),
            ('Richardson number dependent - KT', 'tbd'),
            ('Imbeded as isopycnic vertical coordinate', 'tbd'),
            ('Other', 'tbd'),
        ]
    },

    'interior_mixing_types': {
        'description': 'Types of boundary layer mixing in ocean',
        'members': [
            ('Constant value', 'tbd'),
            ('Turbulent closure - TKE', 'tbd'),
            ('Turbulent closure - Mellor-Yamada', 'tbd'),
            ('Richardson number dependent - PP', 'tbd'),
            ('Richardson number dependent - KT', 'tbd'),
            ('Imbeded as isopycnic vertical coordinate', 'tbd'),
            ('Other', 'tbd'),
        ]
    },
}