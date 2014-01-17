"""
.. module:: esdoc_mp.schemas.cim.v1.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
from esdoc_mp.schemas.cim.v1.activity_classes import classes as activity_classes
from esdoc_mp.schemas.cim.v1.activity_enums import enums as activity_enums
from esdoc_mp.schemas.cim.v1.data_classes import classes as data_classes
from esdoc_mp.schemas.cim.v1.data_enums import enums as data_enums
from esdoc_mp.schemas.cim.v1.grids_classes import classes as grids_classes
from esdoc_mp.schemas.cim.v1.grids_enums import enums as grids_enums
from esdoc_mp.schemas.cim.v1.quality_classes import classes as quality_classes
from esdoc_mp.schemas.cim.v1.quality_enums import enums as quality_enums
from esdoc_mp.schemas.cim.v1.shared_classes import classes as shared_classes
from esdoc_mp.schemas.cim.v1.shared_classes_doc import classes as shared_classes_doc
from esdoc_mp.schemas.cim.v1.shared_classes_time import classes as shared_classes_time
from esdoc_mp.schemas.cim.v1.shared_enums import enums as shared_enums
from esdoc_mp.schemas.cim.v1.shared_enums_doc import enums as shared_enums_doc
from esdoc_mp.schemas.cim.v1.software_classes import classes as software_classes
from esdoc_mp.schemas.cim.v1.software_enums import enums as software_enums
from esdoc_mp.schemas.cim.v1.misc_classes import classes as misc_classes



# Schema :: CIM v1.
schema = {
    'name' : 'cim',
    'version' : '1',
    'is_latest' : True,
    'doc' : 'Metafor CIM ontology schema - version 1',
    'packages' : [
        {
            'name' : 'activity',
            'doc' : 'TODO get package documentation',
            'classes' : activity_classes,
            'enums' : activity_enums,
        },
        {
            'name' : 'data',
            'doc' : 'TODO get package documentation',
            'classes' : data_classes,
            'enums' : data_enums,
        },
        {
            'name' : 'grids',
            'doc' : 'TODO get package documentation',
            'classes' : grids_classes,
            'enums' : grids_enums,
        },
        {
            'name' : 'quality',
            'doc' : 'TODO get package documentation',
            'classes' : quality_classes,
            'enums' : quality_enums,
        },
        {
            'name' : 'shared',
            'doc' : 'TODO get package documentation',
            'classes' : shared_classes + shared_classes_doc + shared_classes_time,
            'enums' : shared_enums + shared_enums_doc,
        },
        {
            'name' : 'software',
            'doc' : 'TODO get package documentation',
            'classes' : software_classes,
            'enums' : software_enums,
        },
        {
            'name' : 'misc',
            'doc' : 'TODO get package documentation',
            'classes' : misc_classes,
            'enums' : [],
        },
    ]
}
