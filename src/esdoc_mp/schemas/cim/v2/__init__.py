"""
.. module:: esdoc_mp.schemas.cim.v2.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas.cim.v2 import activity_classes
from esdoc_mp.schemas.cim.v2 import activity_classes_ensemble
from esdoc_mp.schemas.cim.v2 import activity_classes_experiment
from esdoc_mp.schemas.cim.v2 import activity_enums
from esdoc_mp.schemas.cim.v2 import data_classes
from esdoc_mp.schemas.cim.v2 import platform_classes
from esdoc_mp.schemas.cim.v2 import platform_enums
from esdoc_mp.schemas.cim.v2 import shared_classes
from esdoc_mp.schemas.cim.v2 import shared_classes_doc
from esdoc_mp.schemas.cim.v2 import shared_classes_time
from esdoc_mp.schemas.cim.v2 import shared_enums
from esdoc_mp.schemas.cim.v2 import shared_enums_time
from esdoc_mp.utils.factory import get_type_definitions


# Schema :: CIM v2.
schema = {
    'name': 'cim',
    'version': '2',
    'is_latest': True,
    'doc': 'Metafor CIM ontology schema - version 2',
    'packages': [
        {
            'name': 'activity',
            'doc': 'Types that describe context against which climate models are run.',
            'classes': get_type_definitions(activity_classes) +
                       get_type_definitions(activity_classes_ensemble) +
                       get_type_definitions(activity_classes_experiment),
            'enums': get_type_definitions(activity_enums)
        },
        {
            'name': 'data',
            'doc': 'Types that describe output that climate models emit.',
            'classes': get_type_definitions(data_classes),
            'enums': []
        },
        {
            'name': 'platform',
            'doc': 'Types that describe hardware upon which climate models are run.',
            'classes': get_type_definitions(platform_classes),
            'enums': get_type_definitions(platform_enums)
        },
        {
            'name': 'shared',
            'doc': 'Shared types that might be imported from other packages within the ontology.',
            'classes': get_type_definitions(shared_classes) +
                       get_type_definitions(shared_classes_doc) +
                       get_type_definitions(shared_classes_time),
            'enums': get_type_definitions(shared_enums) +
                     get_type_definitions(shared_enums_time),
        }
    ]
}
