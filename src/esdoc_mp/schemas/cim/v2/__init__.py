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



# Ontology name.
NAME = 'cim'

# Ontology version.
VERSION = '2'

# Ontology doc string.
DOC = 'Metafor CIM ontology schema - version 2'


def activity():
    """Types that describe context against which climate models are run.

    """
    return [
        activity_classes,
        activity_classes_ensemble,
        activity_classes_experiment,
        activity_enums
    ]


def data():
    """Types that describe output that climate models emit.

    """
    return [
        data_classes
    ]


def platform():
    """Types that describe hardware upon which climate models are run.

    """
    return [
        platform_classes,
        platform_enums
    ]


def shared():
    """Shared types that might be imported from other packages within the ontology.

    """
    return [
        shared_classes,
        shared_classes_doc,
        shared_classes_time,
        shared_enums,
        shared_enums_time
    ]

