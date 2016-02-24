"""Ocean lateral physics properties.

type: science.sub_process

"""


def props():
    """Key properties of lateral physics in the ocean.

    type: science.process_detail

    """
    return {
        "transient_eddy_representation": {
            "description": "Type of transient eddy representation in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('None', 'No transient eddies in ocean'),
                ('Eddy active', 'Full resolution of eddies'),
                ('Eddy admitting', 'Some eddy activity permitted by resolution')
            ]
        }
    }
