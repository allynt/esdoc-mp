"""Properties of boundary forcing within the ocean component.

type: science.process

"""
from . import momentum
from . import tracers


# Set of associated sub-processes.
sub_processes = {
	momentum,
	tracers
}
