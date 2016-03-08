"""Properties of upper and lower boundaries within the ocean component.

type: science.process

"""
from . import bottom_boundary_layer
from . import free_surface



# Set of associated sub-processes.
sub_processes = {
	bottom_boundary_layer,
	free_surface
}
