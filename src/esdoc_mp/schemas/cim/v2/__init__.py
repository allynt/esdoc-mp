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
            'classes': [
                activity_classes,
                activity_classes_ensemble,
                activity_classes_experiment
            ],
            'enums': activity_enums
        },
        {
            'name': 'activity',
            'doc': 'Types that describe context against which climate models are run.',
            'classes': [
                activity_classes,
                activity_classes_ensemble,
                activity_classes_experiment
            ],
            'enums': activity_enums
        },
        {
            'name': 'data',
            'doc': 'Types that describe output that climate models emit.',
            'classes': data_classes,
            'enums': []
        },
        {
            'name': 'platform',
            'doc': 'Types that describe hardware upon which climate models are run.',
            'classes': platform_classes,
            'enums': platform_enums
        },
        {
            'name': 'shared',
            'doc': 'Shared types that might be imported from other packages within the ontology.',
            'classes': [
                shared_classes,
                shared_classes_doc,
                shared_classes_time
            ],
            'enums': [
                shared_enums,
                shared_enums_time
            ],
        }
    ]
}
