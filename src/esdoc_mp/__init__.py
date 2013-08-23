"""
.. module:: esdoc_mp.generate.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp code generator.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

import optparse
import os

from esdoc_mp.generators.generator_options import GeneratorOptions
from esdoc_mp.generators.python.utils import format as format_python
from esdoc_mp.utils.validation import (
    validate_language,
    validate_ontology_schema,
    validate_output_dir
    )
import esdoc_mp.utils.factory as factory
import esdoc_mp.utils.runtime as rt



# Set of formatters keyed by programming language.
_formatters = {
    'python' : format_python
}


# Package version identifier.
__version__ = '0.3'



def generate(ontology_schema, language, output_dir):
    """Generates code.

    :param ontology_schema: Ontology schema definition.
    :param language: Target programming language.
    :param output_dir: Target output directory.
    :type ontology_schema: dict
    :type language: str
    :type output_dir: str

    """
    print("-------------------------------------------------------------------")
    print("ES-DOC :: Welcome to the ES-DOC code generator")

    # Defensive programming.
    if can_generate(ontology_schema, language, output_dir):
        # Notify pre-generation.
        print("-------------------------------------------------------------------")
        print("ES-DOC :: GENERATION OPTION : schema = {0}".format(ontology_schema['name']))
        print("ES-DOC :: GENERATION OPTION : schema version = {0}".format(ontology_schema['version']))
        print("ES-DOC :: GENERATION OPTION : language = {0}".format(language))
        print("ES-DOC :: GENERATION OPTION : output directory = {0}".format(output_dir))
        
        # Initialise ontology.
        ontology = factory.create_ontology(ontology_schema)
        print("-------------------------------------------------------------------")
        print("ES-DOC :: ONTOLOGY :: {0} (packages={1}, classes={2}, enums={3})".format(
            ontology, len(ontology.packages), len(ontology.classes), len(ontology.enums)))
            
        # Format ontology.
        if language in _formatters:
            _formatters[language](ontology)
            print("ES-DOC :: ONTOLOGY :: formatted for {0}".format(language))

        # Invoke generators.
        generators = factory.create_generators(language)
        for generator_key in factory.create_generators(language):
            print("-------------------------------------------------------------------")
            print("ES-DOC :: GENERATOR = {0} :: generation begins".format(generator_key))

            options = GeneratorOptions(generator_key, language, output_dir)
            generator = generators[generator_key]()
            generator.execute(ontology, options)
            
            print("ES-DOC :: GENERATOR = {0} :: generation complete".format(generator_key))

    print("-------------------------------------------------------------------")
    print("ES-DOC :: Thank you for using the ES-DOC code generator")
    print("-------------------------------------------------------------------")


def can_generate(ontology_schema, language, output_dir):
    """Verifies whether the generation options are in a state such that generation can occur.

    :param ontology_schema: Ontology schema definition.
    :param language: Target programming language.
    :param output_dir: Target output directory.
    :type ontology_schema: dict
    :type language: str
    :type output_dir: str
    :returns: True if generation can occur, False otherwise.
    :rtype: bool

    """
    # Validate.
    errors = validate_language(language)
    errors += validate_output_dir(output_dir)
    errors += validate_ontology_schema(ontology_schema)
    
    # Report errors.
    if errors:
        print("-------------------------------------------------------------------")
        print("ES-DOC :: INVALID GENERATOR OPTIONS !!!")
        for error in errors:
            print("ES-DOC :: GENERATOR OPTION ERROR :: {0}".format(error))

    return len(errors) == 0
