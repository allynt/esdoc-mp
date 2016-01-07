# -*- coding: utf-8 -*-

"""
.. module:: cmip6.atmosphere.dynamical_core.lateral_boundary.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: List of the model prognostic variables.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""


def prognostic_variables():
    """List of the model prognostic variables.

    """
    return {
        "cardinality": "1.N",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("surface pressure", None),
            ("wind components", None),
            ("divergence/curl", None),
            ("temperature", None),
            ("potential temperature", None),
            ("total water", None),
            ("water vapour", None),
            ("water liquid", None),
            ("water ice", None),
            ("total water moments", None),
            ("clouds", None),
            ("radiation", None),
            ("other", None)
        ]
    }
