"""
.. module:: esdoc_mp.schemas.cim.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
import v1
import v2



# Set of supported Metafor CIM schemas.
schemas = [
    v1.schema,
    v2.schema,
]

