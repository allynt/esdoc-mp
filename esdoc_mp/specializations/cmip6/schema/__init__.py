# -*- coding: utf-8 -*-

"""CMIP6 specialization.

"""
from . import ocean
from . import ocean_advection
from . import ocean_boundary_forcing
from . import ocean_grid
from . import ocean_key_properties
from . import ocean_lateral_physics
from . import ocean_timestepping_framework
from . import ocean_uplow_boundaries
from . import ocean_vertical_physics



# Set of realms with associated modules.
REALMS = [
	{
		'main': ocean,
		'grid': ocean_grid,
		'key_properties': ocean_key_properties,
		'processes': (
			ocean_advection,
			ocean_boundary_forcing,
			ocean_lateral_physics,
			ocean_timestepping_framework,
			ocean_uplow_boundaries,
			ocean_vertical_physics
			)
	}
]
