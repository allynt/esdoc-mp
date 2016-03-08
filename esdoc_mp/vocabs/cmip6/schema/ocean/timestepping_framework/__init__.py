"""Properties of ocean time stepping framework within the ocean component.

type: science.process

"""
from . import barotropic_momemtum
from . import barotropic_solver
from . import properties
from . import tracers


# Set of associated sub-processes.
sub_processes = {
	barotropic_momemtum,
	barotropic_solver,
	properties,
	tracers
}