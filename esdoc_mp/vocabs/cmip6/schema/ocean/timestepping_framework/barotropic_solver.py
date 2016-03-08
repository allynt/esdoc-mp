"""Ocean barotropic solver.

type: science.sub_process

"""


def props():
    """Key properties of barotropic solver in the ocean.

    type: science.process_detail

    """
    return {
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
