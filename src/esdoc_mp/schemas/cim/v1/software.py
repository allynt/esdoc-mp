"""The CIM v1 ontology - software package.

"""

# Module imports.
from esdoc_mp.schemas.cim.v1.software_classes import classes
from esdoc_mp.schemas.cim.v1.software_enums import enums



# CIM v1 - software package.
package = {
    'name' : 'software',
    'doc' : 'TODO get package documentation',
    'classes' : classes,
    'enums' : enums,
}
