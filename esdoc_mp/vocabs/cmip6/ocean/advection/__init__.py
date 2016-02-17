"""Properties of ocean advection processes within the ocean component.

type: science.process

"""
from . import lateral_tracers
from . import momentum
from . import vertical_tracers


# Set of associated sub-processes.
sub_processes = {
	momentum,
	lateral_tracers,
	vertical_tracers
}
