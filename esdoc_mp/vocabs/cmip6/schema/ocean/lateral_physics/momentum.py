"""Ocean lateral physics momentum.

type: science.sub_process

"""


def props():
    """Key properties of lateral physics momentum scheme in the ocean.

    type: science.process_detail

    """
    return {
        "operator_direction": {
            "description": "Direction of lateral physics momentum scheme in the ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Horizontal', 'tbd'),
                ('Isopycnal', 'tbd'),
                ('Isoneutral', 'tbd'),
                ('Geopotential', 'tbd'),
                ('Iso-level', 'tbd'),
                ('Other', 'tbd')
            ]
        },
        "operator_order": {
            "description": "Order of lateral physics momentum scheme in the ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Harmonic', 'Second order'),
                ('Bi-harmonic', 'Fourth order'),
                ('Other', 'tbd')
            ]
        },
        "operator_discretisation": {
            "description": "Discretisation of lateral physics momentum scheme in the ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Second order', 'Second order'),
                ('Fourth order', 'Fourth order'),
                ('Flux limiter', 'tbd')
            ]
        },
        "eddy_viscosity_coefficient": {
            "description": "Discretisation of lateral physics momentum scheme in the ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Second order', 'Second order'),
                ('Fourth order', 'Fourth order'),
                ('Flux limiter', 'tbd')
            ]
        }
    }
