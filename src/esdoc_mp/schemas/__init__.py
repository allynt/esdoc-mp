"""
.. module:: esdoc_mp.generators.python.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas import cim
from esdoc_mp.schemas import validator



# Set of schemas supported 'out of the box'.
SCHEMAS = set()
SCHEMAS.update(cim.SCHEMAS)


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
    if not is_valid_schema(schema):
        raise ValueError("Invalid schema definition.")
    SCHEMAS.add(schema)


def validate_schema(schema):
    """Validates a schema to determine whether it canb be registered.

    :param module schema: An ontology schema definition.

    :returns: A validation report.
    :rtype: dict

    """
    return validator.validate(schema)


def is_valid_schema(schema):
    """Returns flag indicating whether the passed schema is deemed to be valid or not.

    :param module schema: An ontology schema definition.

    :returns: True if valid false otherwise.
    :rtype: bool

    """
    return len(validator.validate(schema)) == 0

