# -*- coding: utf-8 -*-

"""
.. module:: cmip6.atmosphere.dynamical_core.advection_momentum.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Momentum advection scheme.

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
            ("VanLeer", None),
            ("Janjic", None),
            ("SUPG (Streamline Upwind Petrov-Galerkin)", None),
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
            ("2nd order", None),
            ("4th order", None),
            ("cell-centred", None),
            ("staggered grid", None),
            ("semi-staggered grid", None),
            ("other", None)
        ]
    }


def staggering_type():
    """Scheme staggering type.

    """
    return {
        "cardinality": "1.1",
        "type": "selection",
        "vocab_status": "initial",
        "choices": [
            ("Arakawa B-grid", None),
            ("Arakawa C-grid", None),
            ("Arakawa D-grid", None),
            ("Arakawa E-grid", None),
            ("other", None),
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
            ("Angular momentum", None),
            ("Horizontal momentum", None),
            ("Enstrophy", None),
            ("Mass", None),
            ("Total energy", None),
            ("Vorticity", None),
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
