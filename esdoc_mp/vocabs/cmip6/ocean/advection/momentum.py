"""Key properties of momentum advection in the ocean'.

type: science.sub_process

"""


def scheme():
    """Properties of bottom boundary layer in ocean.

    type: science.process_detail

    """
    return {
        "type": {
            "description": "Type of lateral momentum advection scheme in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Flux form', 'tbd'),
                ('Vector form', 'tbd')
            ]
        },
        "name": {
            "description": "Name of ocean momemtum advection scheme",
            "type": "str",
            "cardinality": "1.1"
        },
        "ALE": {
            "description": "Using ALE for vertical advection ? (if vertical coordinates are sigma)",
            "type": "bool",
            "cardinality": "1.1"
        }
    }
