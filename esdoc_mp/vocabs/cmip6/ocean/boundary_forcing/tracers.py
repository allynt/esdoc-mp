"""Ocean barotropic solver.

type: science.sub_process

"""


def sunlight_penetration():
    """Properties of sunlight penetration scheme in ocean.

    type: science.process_detail

    """
    return {
        "extinct_depth": {
            "description": "Describe and list extinctions depths for sunlight penetration scheme (if applicable).",
            "type": "str",
            "cardinality": "1.1"
        },
        "ocean_colour": {
            "description": "Is the ocean sunlight penetration scheme ocean colour dependent ?",
            "type": "bool",
            "cardinality": "1.1"
        },
        "scheme": {
            "description": "Type of timestepping scheme in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Leap-frog + Asselin filter', 'tbd'),
                ('Leap-frog + Periodic Euler backward solver', 'tbd'),
                ('Predictor-corrector', 'tbd'),
                ('AM3-LF (ROMS)', 'tbd'),
                ('Forward-backward', 'tbd'),
                ('Other', 'tbd'),
            ]
        }
    }


def surface_salinity():
    """Properties of surface salinity forcing in ocean.

    type: science.process_detail

    """
    return {
        "atmosphere": {
            "description": "Surface salinity forcing from atmosphere in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Freshwater flux', 'tbd'),
                ('Virtual salt flux', 'tbd'),
                ('Other', 'tbd'),
            ]
        },
        "sea_ice": {
            "description": "Surface salinity forcing from sea ice in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Freshwater flux', 'tbd'),
                ('Virtual salt flux', 'tbd'),
                ('Other', 'tbd'),
            ]
        }

    }

