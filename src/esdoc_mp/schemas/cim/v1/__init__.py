"""
.. module:: esdoc_mp.schemas.cim.v1.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

from esdoc_mp.schemas.cim.v1 import activity_classes
from esdoc_mp.schemas.cim.v1 import activity_enums
from esdoc_mp.schemas.cim.v1 import data_classes
from esdoc_mp.schemas.cim.v1 import data_enums
from esdoc_mp.schemas.cim.v1 import grids_classes
from esdoc_mp.schemas.cim.v1 import grids_enums
from esdoc_mp.schemas.cim.v1 import quality_classes
from esdoc_mp.schemas.cim.v1 import quality_enums
from esdoc_mp.schemas.cim.v1 import misc_classes
from esdoc_mp.schemas.cim.v1 import shared_classes
from esdoc_mp.schemas.cim.v1 import shared_classes_doc
from esdoc_mp.schemas.cim.v1 import shared_classes_time
from esdoc_mp.schemas.cim.v1 import shared_enums
from esdoc_mp.schemas.cim.v1 import shared_enums_doc
from esdoc_mp.schemas.cim.v1 import software_classes
from esdoc_mp.schemas.cim.v1 import software_enums
from esdoc_mp.utils.factory import get_type_definitions




# Schema :: CIM v1.
schema = {
    'name' : 'cim',
    'version' : '1',
    'is_latest' : False,
    'doc' : 'Metafor CIM ontology schema - version 1',
    'packages' : [
        {
            'name' : 'activity',
            'doc' : 'Types that describe context against which climate models are run.',
            'classes' : get_type_definitions(activity_classes),
            'enums' : get_type_definitions(activity_enums),
        },
        {
            'name' : 'data',
            'doc' : 'Types that describe output that climate models emit.',
            'classes' : get_type_definitions(data_classes),
            'enums' : get_type_definitions(data_enums),
        },
        {
            'name' : 'grids',
            'doc' : 'Types that describe the grids that climate models plot.',
            'classes' : get_type_definitions(grids_classes),
            'enums' : get_type_definitions(grids_enums),
        },
        {
            'name' : 'quality',
            'doc' : 'Types that describe the quailty of output that climate models emit.',
            'classes' : get_type_definitions(quality_classes),
            'enums' : get_type_definitions(quality_enums),
        },
        {
            'name' : 'shared',
            'doc' : 'Shared types that might be imported from other packages within the ontology.',
            'classes' : get_type_definitions(shared_classes) +
                        get_type_definitions(shared_classes_doc) +
                        get_type_definitions(shared_classes_time),
            'enums' : get_type_definitions(shared_enums) +
                      get_type_definitions(shared_enums_doc),
        },
        {
            'name' : 'software',
            'doc' : 'Types that describe the climate models software.',
            'classes' : get_type_definitions(software_classes),
            'enums' : get_type_definitions(software_enums),
        },
        {
            'name' : 'misc',
            'doc' : 'Miscellaneui',
            'classes' : get_type_definitions(misc_classes),
            'enums' : [],
        },
    ]
}
