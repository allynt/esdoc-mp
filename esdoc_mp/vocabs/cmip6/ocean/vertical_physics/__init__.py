"""Properties of vertical physics within the ocean component.

type: science.process

"""
from . import attributes
from . import boundary_layer_mixing
from . import interior_mixing


# Set of associated sub-processes.
sub_processes = {
	attributes,
	boundary_layer_mixing,
	interior_mixing
}


