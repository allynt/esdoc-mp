"""
.. module:: esdoc_mp.generators.python.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.schemas import cim
from esdoc_mp.schemas.validation import validate



def get_schema(name, version):
    """Returns a supported ontology schema module.

    :param str name: Schema name.
    :param str version: Schema version.

    :returns: An ontology schema.
    :rtype: module

    """
    if name == 'cim':
        if version == '1':
            return cim.v1
        elif version == '2':
            return cim.v2


def is_valid(schema):
    """Returns flag indicating whether the passed schema is deemed to be valid or not.

    :param module schema: An ontology schema definition.

    :returns: True if valid false otherwise.
    :rtype: bool

    """
    return len(validate(schema)) == 0

