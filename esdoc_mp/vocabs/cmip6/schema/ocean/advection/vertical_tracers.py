"""Key properties of vertical tracer advection in the ocean'.

type: science.sub_process

"""

enum_scheme_types = [
    ('Centred 2nd order','tbd'),
    ('Centred 4th order','tbd'),
    ('Total Variance Dissipation (TVD)', 'tbd'),
    ('MUSCL', 'tbd'),
    ('QUICKEST', 'tbd'),
    ('Piecewise Parabolic method', 'tbd'),
    ('Sweby', 'tbd'),
    ('Prather 2nd moment (PSOM)', 'tbd'),
    ('Other', 'tbd'),
]



def scheme():
    """Properties of vertical tracer advection scheme in ocean.

    type: science.process_detail

    """
    return {
        "type": {
            "description": "Type of tracer advection scheme in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": enum_scheme_types
        },
        "flux_limiter": {
            "description": "Monotonic flux limiter for vertical tracer advection scheme in ocean ?",
            "type": "bool",
            "cardinality": "1.1"
        }
    }