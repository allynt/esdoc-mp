"""Overview of key properties of ocean component.

"""

# Set of grid related properties.
GRID = {
    # General grid properties.
    ('name', 'a name'),     # necessary ?
    ('context', 'a context'),       # necessary ?
    ('vertical_grid_type:', 'ENUM:ocean_vertical_coord_types', '0.1'),
    ('partial_steps', 'bool', '1.1',
       'Using partial steps with Z or Z* vertical coordinate in ocean ?'),

    # Resolution
    ('resolution:surface_layer_thickness', 'float', '0.1',
        'Thickness (in metres) of surface layer of ocean (e.g. 0.1)'),

    # Discretisation
    ('discretisation:horizontal_scheme', 'ENUM:ocean_horiz_scheme_types', '1.1'),
    ('discretisation:ocean_pole_singularity_treatment', 'str', '0.1',
           'Describe how the North Pole singularity is treated (filter, pole rotation/displacement, artificial island, ...)'),
}

# Set of conservation related properties.
CONSERVATION = {
    ('props', 'str', '0.1',
       'Describe any type of ocean nudging (tracers or momemtum) and region(s) where applied (surface, depth, basins)'),
    ('method', 'str', '1.1',
       'Describe how conservation properties are ensured in ocean'),
    ('conserved_properties', 'ENUM:ocean_conservation_props_types', '1.N',
       'List of conserved properties in the ocean component'),
}

# Set of grouped properties.
PROPERTIES = {
    # General.
    ('basic_approximations', 'ENUM:ocean_basic_approx_types', '1.N',
       'List of basic approximations in the ocean component'),
    ('prognostic_varibles', 'ENUM:ocean_prognostic_vars_types', '1.N',
       'List of prognostic variables in the ocean component'),
    ('nonoceanic_waters', 'str', '0.1',
       'Describe if/how isolated seas and river mouth mixing or other specific treatment is performed'),

    # Seawater.
    ('seawater:eos_types', 'ENUM:ocean_seawater_eos_types', '1.1',
       'Physical properties of seawater in ocean'),
    ('seawater:freezing_point', 'str', '1.1',
       'Describe freezing point in ocean (fixed or varying)'),
    ('seawater:specific_heat', 'str', '1.1',
       'Describe specific heat in ocean (fixed or varying)'),

    # Bathymetry.
    ('bathymetry:reference_dates', 'ENUM:ocean_bathymetry_ref_dates' , '1.1',
       'Properties of bathymetry in ocean'),
    ('bathymetry:type', 'bool', '1.1',
       'Is the bathymetry fixed in time in the ocean ?'),
    ('bathymetry:smoothing', 'str', '1.1',
       'Describe any smoothing or hand editing of bathymetry in ocean'),
    ('bathymetry:source', 'str', '1.1',
       'Describe source of bathymetry in ocean'),
}

# Set of enums.
ENUMS = {
   "basic_approximation_types": {
        ('Primitive equations','tbd'),
        ('Non-hydrostatic', 'tbd'),
        ('Boussinesq', 'tbd'),
        ('Other', 'tbd')
    },
    "bathymetry_reference_dates": {
        ('Present day','tbd'),
        ('21000 years BP', 'tbd'),
        ('6000 years BP', 'tbd'),
        ('LGM', 'Last Glacial Maximum'),
        ('Pliocene', 'tbd'),
        ('Other', 'tbd')
    },
    "conserved_property_types": {
        ('Energy','tbd'),
        ('Enstrophy','tbd'),
        ('Salt', 'tbd'),
        ('Volume of ocean', 'tbd'),
        ('Other', 'tbd')
    },
    "horizontal_scheme_types": {
        ('Finite difference / Arakawa B-grid','tbd'),
        ('Finite difference / Arakawa C-grid','tbd'),
        ('Finite difference / Arakawa E-grid','tbd'),
        ('Finite volumes', 'tbd'),
        ('Finite elements', 'tbd'),
        ('Other', 'tbd')
    },
    "prognostic_varible_types": {
        ('Potential temperature','tbd'),
        ('Conservative temperature','tbd'),
        ('Salinity','tbd'),
        ('U-velocity','tbd'),
        ('V-velocity','tbd'),
        ('W-velocity','tbd'),
        ('SSH','Sea Surface Height'),
        ('Other', 'Other prognostic variables')
    },
    "seawater_eos_types": {
        ('Linear','tbd'),
        ('Mc Dougall et al.', 'tbd'),
        ('Jackett et al. 2006', 'tbd'),
        ('TEOS 2010', 'tbd'),
        ('Other', 'tbd')
    }
    'members': [
        ('Present day','tbd'),
        ('21000 years BP', 'tbd'),
        ('6000 years BP', 'tbd'),
        ('LGM', 'Last Glacial Maximum'),
        ('Pliocene', 'tbd'),
        ('Other', 'tbd')
        ]
    }
}
