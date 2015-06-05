"""
.. module:: esdoc_mp.generate.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp code generator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas import get_schema
from esdoc_mp.schemas import register_schema
from esdoc_mp.generators import generate
from esdoc_mp.generators import can_generate



# Package version identifier.
__version__ = '0.5'



# def get_ontology(name, version):
#     """Returns ontology definitions for the passed ontology name/version reference.

#     """
#     schema = create_ontology_schema(name, version)



