"""
.. module:: esdoc_mp.generators.python.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas import cim
from esdoc_mp.schemas.validation import validate as validate_schema


# Set of supported schemas.
SCHEMAS = set()

# Set of default schemas supported 'out of the box'.
DEFAULT_SCHEMAS = cim.SCHEMAS


def get_schema(name, version):
    """Returns a supported ontology schema module.

    :param str name: Schema name.
    :param str version: Schema version.

    :returns: An ontology schema.
    :rtype: module

    """
    for schema in SCHEMAS:
        if schema.NAME.lower() == name.lower() and \
           schema.VERSION.lower() == version.lower():
            return schema


def register_schema(schema):
    """Registers a schema with set of supported schemas.

    :param module schema: An ontology schema definition.

    """
    report = validate_schema(schema)
    if report:
        for error in validate_schema(schema):
            print(error)
        raise ValueError("Invalid schemas cannot be registered")

    SCHEMAS.add(schema)


def is_valid_schema(schema):
    """Returns flag indicating whether the passed schema is deemed to be valid or not.

    :param module schema: An ontology schema definition.

    :returns: True if valid false otherwise.
    :rtype: bool

    """
    return len(validate_schema(schema)) == 0


# Auto register default schemas.
for schema in DEFAULT_SCHEMAS:
    register_schema(schema)
