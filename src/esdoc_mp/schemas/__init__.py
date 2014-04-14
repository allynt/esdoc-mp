"""
.. module:: esdoc_mp.generators.python.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas.cim import schemas as cim_schemas
from esdoc_mp.schemas.test import schemas as test_schemas


# Set of schemas supported 'out of the box'.
schemas = []
schemas.extend(cim_schemas)
schemas.extend(test_schemas)
