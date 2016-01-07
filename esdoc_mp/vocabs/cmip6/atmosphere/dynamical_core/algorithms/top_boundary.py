# -*- coding: utf-8 -*-

"""
.. module:: cmip6.atmosphere.dynamical_core.top_boundary.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: ype of boundary layer at the top of the model.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def condition():
	"""Boundary condition.

	"""
	return {
        "cardinality": "1.1",
        "type": "enum",
        "vocab_status": "initial",
        "members": [
            ("sponge layer", None),
            ("radiation boundary condition", None),
            ("other", None),
        ]
	}


def heat_treatment():
	"""Boundary heat treatment.

	"""
	return {
        "cardinality": "1.1",
        "type": str
	}


def wind_treatment():
    """Boundary wind treatment.

    """
    return {
        "cardinality": "1.1",
        "type": str
    }
