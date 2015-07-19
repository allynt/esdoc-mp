# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.schemas.validation.__init__.py
   :platform: Unix, Windows
   :synopsis: Validates an ontology schema definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect
import re

from esdoc_mp.schemas.validation.context import ValidationContext
from esdoc_mp.schemas.validation import class_validator
from esdoc_mp.schemas.validation import enum_validator
from esdoc_mp.schemas.validation import package_validator
from esdoc_mp.schemas.validation import schema_validator
from esdoc_mp.schemas.validation import type_validator



def validate(schema):
    """Validates ontology schema.

    :param module schema: Ontology schema definition.

    :returns: Set of validation errors (if any).
    :rtype: set

    """
    ctx = ValidationContext(schema)
    for validator in (
        schema_validator.validate,
        package_validator.validate,
        type_validator.validate
        ):
        validator(ctx)
        if ctx.report:
            break

    return ctx.report
