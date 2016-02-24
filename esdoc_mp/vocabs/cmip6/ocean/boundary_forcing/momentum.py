"""Momentum boundary forcing in the ocean.

type: science.sub_process

"""


def props():
    """Key properties of momentum boundary forcing in the ocean.

    type: science.process_detail

    """
    return {
        "bottom_friction_scheme": {
            "description": "Type of momentum bottom friction in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Linear', 'tbd'),
                ('Non-linear', 'tbd'),
                ('Non-linear (drag function of speed of tides)', 'tbd'),
                ('Constant drag coefficient', 'tbd'),
                ('None', 'tbd'),
                ('Other', 'tbd')
            ]
        },
        "lateral_friction_scheme": {
            "description": "Type of momentum lateral friction in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('None', 'tbd'),
                ('Free-slip', 'tbd'),
                ('No-slip', 'tbd'),
                ('Other', 'tbd'),
            ]
        }
    }
