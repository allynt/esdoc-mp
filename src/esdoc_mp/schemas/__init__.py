"""
.. module:: esdoc_mp.generators.python.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas import cim



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
    # TODO - validate input
    SCHEMAS.add(schema)
