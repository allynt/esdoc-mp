# -*- coding: utf-8 -*-

"""
.. module:: cmip6.atmosphere.dynamical_core.lateral_boundary.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Type of lateral boundary condition (if the model is a regional model).

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def lateral_boundary():
    """Type of lateral boundary condition (if the model is a regional model).

    """
    return {
        "cardinality": "1.1",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("sponge layer", None),
            ("radiation boundary condition", None),
            ("none", None),
            ("other", None)
        ]
    }
