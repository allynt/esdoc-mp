"""Ocean realm.

type: science.scientific_domain

"""
from . import advection
from . import vertical_physics
from . import uplow_boundaries



# Set of domain processes.
processes = {
	advection,
	vertical_physics,
	uplow_boundaries
}
