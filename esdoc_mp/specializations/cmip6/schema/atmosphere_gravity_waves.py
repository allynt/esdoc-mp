CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>', e.g. 'cmip6.atmosphere.radiation'
# --------------------------------------------------------------------
ID = 'cmip6.atmosphere.gravity_waves'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.process'

from collections import OrderedDict

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the parameterised gravity waves in the atmosphere, whether from orography or other sources.',

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['attributes'] = {
    'properties': [
        ('sponge_layer','ENUM:sponge_layer_attributes', '1.1', 
         'Sponge layer in the upper levels in order to avoid gravity wave reflection at the top.'),
        ('background', 'ENUM:background_attributes', '1.1',
         'Background wave distribution'),
        ('subgrid_scale_orography', 'ENUM:subgrid_scale_orography_attributes', '1.N',
         'Subgrid scale orography effects taken into account.'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['orographic_gravity_waves'] = {
    'description': 'Gravity waves generated due to the presence of orography',
    'details': ['orographic_gravity_waves_details']
}

SUB_PROCESSES['non_orographic_gravity_waves'] = {
    'description': 'Gravity waves generated by non-orographic processes.',
    'details': ['non_orographic_gravity_waves_details']
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['orographic_gravity_waves_details'] = {
    'properties': [
        ('source_mechanisms', 'ENUM:orographic_gravity_waves_source_mechanisms', '1.N',
         'Orographic gravity wave source mechanisms'),
        ('calculation_method', 'ENUM:orographic_gravity_waves_calculation_method', '1.N',
         'Orographic gravity wave calculation method'),
        ('propagation_scheme', 'ENUM:orographic_gravity_waves_propagation_scheme', '1.1',
         'Orographic gravity wave propogation scheme'),
        ('dissipation_scheme', 'ENUM:orographic_gravity_waves_dissipation_scheme', '1.1',
         'Orographic gravity wave dissipation scheme'),
    ]
}

SUB_PROCESS_DETAILS['non_orographic_gravity_waves_details'] = {
    'properties': [
        ('source_mechanisms', 'ENUM:non_orographic_gravity_waves_source_mechanisms', '1.N',
         'Non-orographic gravity wave source mechanisms'),
        ('calculation_method', 'ENUM:non_orographic_gravity_waves_calculation_method', '1.N',
         'Non-orographic gravity wave calculation method'),
        ('propagation_scheme', 'ENUM:non_orographic_gravity_waves_propagation_scheme', '1.1',
         'Non-orographic gravity wave propogation scheme'),
        ('dissipation_scheme', 'ENUM:non_orographic_gravity_waves_dissipation_scheme', '1.1',
         'Non-orographic gravity wave dissipation scheme'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['sponge_layer_attributes'] = {
    'description': 'Gravity waves sponge layer attributes',
    'members': [
        ('None', None),
        ('Other', None),
    ]
}

ENUMERATIONS['background_attributes'] = {
    'description': 'Gravity waves background attributes',
    'members': [
        ('None', None),
            ('Other', None),
    ]
}

ENUMERATIONS['subgrid_scale_orography_attributes'] = {
    'description': 'Gravity waves subgrid scale orography attributes',
    'members': [
        ('effect on drag', None),
        ('effect on lifting', None),
        ('Other', None),
        ]
}

ENUMERATIONS['orographic_gravity_wave_source_mechanisms'] = {
    'description': 'Physical mechanisms generatic orographic gravity waves.',
    'members': [
        ('linear mountain waves', None),
        ('hydraulic jump', None),
        ('envelope orography', None),
        ('statistical sub-grid scale variance', None),
        ('other', None),
    ]
}

ENUMERATIONS['orographic_gravity_wave_calculation_method'] = {
    'description': 'Calculation method for orographic gravity waves.',
    'members': [
        ('non-linear calculation', None),
        ('more than two cardinal directions', None),
    ]
}

ENUMERATIONS['orographic_gravity_wave_propagation_scheme'] = {
    'description': 'Type of propagation scheme for orgraphic gravity waves',
    'members': [
        ('linear theory', None),
        ('non-linear theory', None),
        ('other', None),
    ]
}

ENUMERATIONS['orographic_gravity_wave_dissipation_scheme'] = {
    'description': 'Type of dissipation scheme for orographic gravity waves.',
    'members': [
        ('total wave', None),
        ('single wave', None),
        ('spectral', None),
        ('linear', None), 
        ('other', None),
    ]
}

ENUMERATIONS['non_orographic_gravity_wave_source_mechanisms'] = {
    'description': 'Physical mechanisms generating non-orographic gravity waves',
    'members': [
        ('convection', None),
        ('precipitation', None),
        ('background spectrum', None),
        ('other', None),
    ]
}

ENUMERATIONS['non_orographic_gravity_wave_calculation_method'] = {
    'description': 'Calculation method for non-orographic gravity waves',
    'members': [
        ('spatially dependent', None),
        ('temporally dependent', None),
    ]
}

ENUMERATIONS['non_orographic_gravity_wave_propagation_scheme'] = {
    'description': 'Type of propagation scheme for non-orographic gravity waves.',
    'members': [
        ('linear theory', None),
        ('non-linear theory', None),
        ('other', None),
    ]
}

ENUMERATIONS['non_orographic_gravity_wave_dissipation_scheme'] = {
    'description': 'Type of dissipation scheme for non-orographic gravity waves.',
    'members': [
    ('total wave', None),
        ('single wave', None),
        ('spectral', None),
        ('linear', None), 
        ('other', None),
    ]
}
