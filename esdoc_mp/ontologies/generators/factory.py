# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.utils.factory
   :platform: Unix, Windows
   :synopsis: Encapsulates process of instantiating objects, i.e. generators, schemas and ontologies.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.ontologies.generators.python import ConstraintsGenerator
from esdoc_mp.ontologies.generators.python import RootGenerator
from esdoc_mp.ontologies.generators.python import DecoderGenerator
from esdoc_mp.ontologies.generators.python import TypeKeyGenerator
from esdoc_mp.ontologies.generators.python import TypeSetGenerator
from esdoc_mp.ontologies.generators.qxml import QRootGenerator



def _get_generators_for_python():
    """Returns set of supported python code generators.

    """

    return {
        'constraints' : ConstraintsGenerator,
        'root' : RootGenerator,
        'typekey' : TypeKeyGenerator,
        'typeset' : TypeSetGenerator,
        'decoder' : DecoderGenerator
    }


def _get_generators_for_qxml():
    """Returns set of supported qxml generators.

    """

    return {
        'root' : QRootGenerator,
    }


# Set of supported generators grouped by programming language.
_generators = {
    'python' : _get_generators_for_python,
    'qxml' : _get_generators_for_qxml,
}


def create_generators(language):
    """Factory method to instantiate a set of generators filtered by programming language.

    :param str language: A supported programming language.

    :returns: A set of generators.
    :rtype: dict

    """
    return {} if language not in _generators else _generators[language]()
