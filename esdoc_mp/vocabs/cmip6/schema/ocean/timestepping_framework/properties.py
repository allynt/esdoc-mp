"""Ocean time stepping properties.

type: science.sub_process

"""


def props():
    """Key properties of time stepping framework in the ocean.

    type: science.process_detail

    """
    return {
        "diurnal_cycle": {
            "description": "Diurnal cycle resolution in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('None','No diurnal cycle in ocean'),
                ('Via coupling','Diurnal cycle via coupling frequency'),
                ('Specific treatment', 'Specific treament'),
            ]
        },
        "time_step": {
            "description": "Ocean time step in seconds",
            "type": "int",
            "cardinality": "1.1"
        }
    }
