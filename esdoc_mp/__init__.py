"""
.. module:: esdoc_mp.generate.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp code generator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from . import exceptions
from . import vocabs
from esdoc_mp.ontologies.core import create_ontology as get_ontology
from esdoc_mp.ontologies.schemas import get_schema
from esdoc_mp.ontologies.schemas import validate
from esdoc_mp.ontologies.generators import generate



# Package version identifier.
__version__ = '0.6.0.0'

