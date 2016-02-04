"""Ocean realm.

type: science.scientific_domain

"""

from . import vertical_physics
from . import uplow_boundaries


# Set of domain processes.
processes = {
	vertical_physics,
	uplow_boundaries
}
