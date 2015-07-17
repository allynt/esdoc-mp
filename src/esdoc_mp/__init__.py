"""
.. module:: esdoc_mp.generate.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp code generator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas import  DEFAULT_SCHEMAS
from esdoc_mp.schemas import get_schema
from esdoc_mp.schemas import register_schema
from esdoc_mp.schemas import validate_schema
from esdoc_mp.generators import generate



# Package version identifier.
__version__ = '0.5.1.0'

