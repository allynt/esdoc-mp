# -*- coding: utf-8 -*-

"""
.. module:: cmip6.atmosphere.dynamical_core.horizontal_discretion.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Horizontal discretisation scheme.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def type():
	"""Discretisation type.

	"""
	return {
        "cardinality": "1.1",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("spectral", None),
            ("fixed grid", None),
            ("other", None)
        ]
	}


def method():
	"""Discretisation method.

	"""
	return {
        "cardinality": "1.1",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("finite elements", None),
            ("finite volumes", None),
            ("finite difference", None),
            ("centered finte difference", None)
        ],
        "hint": """If the scheme type is fixed grid then describe the scheme method for the 
        		   horizontal discretisation scheme."""
	}


def order():
	"""Discretisation order.

	"""
	return {
        "cardinality": "1.1",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("First Order", None),
            ("Second Order", None)
        ],
        "hint": """If the scheme method is finite difference or centered finite difference describe the 
        		   scheme order of the finite difference method used by the horizontal discretisation scheme."""
	}


def pole():
	"""Method used to handle the pole singularities.

	"""
	return {
        "cardinality": "1.1",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("Artificial Island", None),
            ("Filter", None),
            ("Pole Rotation", None),
            ("None", None),
            ("Other", None),
        ]
	}
