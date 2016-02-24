"""Ocean realm.

type: science.scientific_domain

"""
from . import advection
from . import boundary_forcing
from . import lateral_physics
from . import timestepping_framework
from . import uplow_boundaries
from . import vertical_physics



# Set of domain processes.
processes = {
	advection,
	boundary_forcing,
	lateral_physics,
	timestepping_framework,
	uplow_boundaries,
	vertical_physics
}
