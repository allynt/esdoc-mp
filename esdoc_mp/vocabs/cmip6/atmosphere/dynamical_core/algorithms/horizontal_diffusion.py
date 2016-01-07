# -*- coding: utf-8 -*-

"""
.. module:: cmip6.atmosphere.dynamical_core.horizontal_diffusion.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Horizontal diffusion scheme.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def name():
	"""Scheme name.

	"""
	return {
        "cardinality": "1.N",
        "type": str
	}


def method():
	"""Scheme method.

	"""
	return {
        "cardinality": "1.N",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("Iterated Laplacian", None),
            ("other", None),
        ]
	}