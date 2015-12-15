"""
.. module:: esdoc_mp.generate.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp code generator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp import exceptions
from esdoc_mp.schemas import get_schema
from esdoc_mp.schemas import validate
from esdoc_mp.generators import generate



# Package version identifier.
__version__ = '0.5.1.0'

