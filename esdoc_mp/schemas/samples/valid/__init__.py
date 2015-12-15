# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.schemas.samples.valid.__init__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Valid sample schema.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas.samples.valid import fruit_classes
from esdoc_mp.schemas.samples.valid import fruit_enums
from esdoc_mp.schemas.samples.valid import vegetable_classes
from esdoc_mp.schemas.samples.valid import vegetable_enums


# Ontology name.
NAME = 'valid'

# Ontology version.
VERSION = '1'

# Ontology doc string.
DOC = 'A valid sample schema'


def fruit():
    """Fruits that provide sweetness.

    """
    return {
        fruit_classes,
        fruit_enums
    }


def vegetables():
    """Vegetables that provide fibre.

    """
    return {
        vegetable_classes,
        vegetable_enums
    }
