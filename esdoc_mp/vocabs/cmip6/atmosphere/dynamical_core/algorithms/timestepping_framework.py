# -*- coding: utf-8 -*-

"""
.. module:: cmip6.atmosphere.dynamical_core.timestepping_framework.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Timestepping framework.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def scheme_type():
	"""Type of time stepping scheme.

	"""
	pass
	return {
        "cardinality": "1.N",
        "type": "enum",
        "members": [
            ("Adam Bashford", None),
            ("explicit", None),
            ("implicit", None),
            ("semi-implicit", None),
            ("leap frog", None),
            ("multi-step", None),
            ("Runge Kutta fifth order", None),
            ("Runge Kutta second order", None),
            ("Runge Kutta third order", None),
            ("other", None),
        ]
	}


def time_step():
	"""Time step (seconds).

	"""
	return {
        "cardinality": "1.N",
        "type": int
	}
