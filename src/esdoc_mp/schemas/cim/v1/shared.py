"""
The CIM v1 ontology - shared package.
"""

# Module imports.
from esdoc_mp.schemas.cim.v1.shared_classes import classes
from esdoc_mp.schemas.cim.v1.shared_classes_cim import classes as cim_classes
from esdoc_mp.schemas.cim.v1.shared_classes_time import classes as time_classes
from esdoc_mp.schemas.cim.v1.shared_enums import enums


# CIM v1 - shared package.
package = {
    'name' : 'shared',
    'doc' : 'TODO get package documentation',
    'classes' : classes + cim_classes + time_classes,
    'enums' : enums,
}
