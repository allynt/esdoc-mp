# -*- coding: utf-8 -*-

"""
.. module:: cmip6.atmosphere.dynamical_core.advection_tracers.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tracer advection scheme.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def name():
	"""Scheme name.

	"""
	return {
        "cardinality": "1.1",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("Heun", None),
            ("Roe and VanLeer", None),
            ("Roe and Superbee", None),
            ("Prather", None),
            ("UTOPIA", None),
            ("other", None)
        ]
	}


def characteristics():
	"""Scheme characteristics.

	"""
	return {
        "cardinality": "1.N",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("Eulerian", None),
            ("modified Euler", None),
            ("Lagrangian", None),
            ("semi-Lagrangian", None),
            ("cubic semi-Lagrangian", None),
            ("quintic semi-Lagrangian", None),
            ("mass-conserving", None),
            ("finite volume", None),
            ("flux-corrected", None),
            ("linear", None),
            ("quadratic", None),
            ("quartic", None),
            ("other", None)
        ]
	}


def conserved_quantities():
	"""Scheme conserved quantities.

	"""
	return {
        "cardinality": "1.N",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("Cubic semi-Lagrangian", None),
            ("Eulerian", None),
            ("Finite volume", None),
            ("Mass-conserving", None),
            ("Quadratic", None),
            ("Quintic semi-Lagrangian", None),
            ("Semi-Lagrangian", None),
            ("Other", None)
        ]
	}


def conservation_method():
	"""Scheme conservation method.

	"""
	return {
        "cardinality": "1.1",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
        	("Conservation Fixer", None),
            ("Other", None)
        ]
	}