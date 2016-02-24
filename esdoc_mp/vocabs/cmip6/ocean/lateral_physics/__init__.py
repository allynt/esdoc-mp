"""Properties of ocean lateral physics within the ocean component.

type: science.process

"""
from . import momentum
from . import properties
from . import tracers


# Set of associated sub-processes.
sub_processes = {
	momentum,
	properties,
	tracers
}