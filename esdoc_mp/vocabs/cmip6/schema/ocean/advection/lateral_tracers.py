"""Key properties of lateral tracer advection in the ocean'.

type: science.sub_process

"""
from .vertical_tracers import enum_scheme_types


def scheme():
    """Properties of lateral tracer advection scheme in ocean.

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
            "description": "Monotonic flux limiter for lateral tracer advection scheme in ocean ?",
            "type": "bool",
            "cardinality": "1.1"
        }
    }

