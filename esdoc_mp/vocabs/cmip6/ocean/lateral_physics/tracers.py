"""Ocean lateral physics tracers.

type: science.sub_process

"""

def general():
    """General properties of lateral physics tracers scheme in the ocean.

    type: science.process_detail

    """
    return {
        "mesoscale_closure": {
            "description": "Is there a mesoscale closure in the lateral physics tracers scheme ?",
            "type": "bool",
            "cardinality": "1.1"
        }
    }


def operator():
    """Operator properties of lateral physics tracers scheme in the ocean.

    type: science.process_detail

    """
    return {
        "direction": {
            "description": "Direction of lateral physics momemtum scheme in the ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Horizontal', 'tbd'),
                ('Isopycnal', 'tbd'),
                ('Isoneutral', 'tbd'),
                ('Geopotential', 'tbd'),
                ('Iso-level', 'tbd'),
                ('Other', 'tbd'),
            ]
        },
        "order": {
            "description": "Order of lateral physics tracers scheme in the ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Harmonic', 'Second order'),
                ('Bi-harmonic', 'Fourth order'),
                ('Other', 'tbd')
            ]
        },
        "discretisation": {
            "description": "Discretisation of lateral physics tracers scheme in the ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Second order', 'Second order'),
                ('Fourth order', 'Fourth order'),
                ('Flux limiter', 'tbd'),
            ]
        }
    }


def eddy_viscosity_coefficient():
    """Properties of eddy viscosity coeff in lateral physics tracers scheme in the ocean.

    type: science.process_detail

    """
    return {
        "background": {
            "description": "Background value of eddy viscosity coeff in lateral physics tracers scheme (in m2/s)",
            "type": "int",
            "cardinality": "1.1"
        },
        "backscatter": {
            "description": "Is there backscatter in eddy viscosity coeff in lateral physics tracers scheme ?",
            "type": "bool",
            "cardinality": "1.1"
        },
        "constant": {
            "description": "If constant, value of eddy viscosity coeff in lateral physics tracers scheme (in m2/s)",
            "type": "int",
            "cardinality": "0.1"
        },
        "scheme": {
            "description": "Ocean lateral physics tracers eddy viscosity coefficient",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Constant', 'tbd'),
                ('Space varying', 'tbd'),
                ('Time + space varying (Smagorinsky)', 'tbd'),
                ('Other', 'tbd'),
            ]
        },
        "variations": {
            "description": "If space-varying, describe variations of eddy viscosity coeff in lateral physics tracers scheme",
            "type": "str",
            "cardinality": "0.1"
        }
    }


def eddy_induced_velocity():
    """Properties of eddy induced velocity in lateral physics tracers scheme in the ocean.

    type: science.process_detail

    """
    return {
        "added_diffusivity": {
            "description": "Type of EIV added diffusivity (constant, flow dependent or none)",
            "type": "str",
            "cardinality": "1.1"
        },
        "flux_type": {
            "description": "Type of EIV flux (advective or skew)",
            "type": "str",
            "cardinality": "1.1"
        },
        "constant": {
            "description": "If eddy induced velocity scheme for tracers is constant, specify coefficient value (M2/s)",
            "type": "int",
            "cardinality": "0.1"
        },
        "scheme": {
            "description": "Ocean lateral physics tracers eddy induced velocity scheme",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('GM', 'Gent and McWilliams'),
                ('Other', 'tbd'),
            ]
        }
    }
