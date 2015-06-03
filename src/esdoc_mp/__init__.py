"""
.. module:: esdoc_mp.generate.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp code generator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

import optparse
import os

from esdoc_mp.core.factory import create_ontology
from esdoc_mp.generators.factory import create_generators
from esdoc_mp.generators.generator_options import GeneratorOptions
from esdoc_mp.generators.python.utils import format as format_python
from esdoc_mp.utils.validation import validate_language
from esdoc_mp.utils.validation import validate_ontology_schema
from esdoc_mp.utils.validation import validate_output_dir
import esdoc_mp.utils.runtime as rt



# Set of formatters keyed by programming language.
_formatters = {
    'python' : format_python
}


# Package version identifier.
__version__ = '0.5'



def generate(ontology_schema, language, output_dir):
    """Generates code.

    :param dict ontology_schema: Ontology schema definition.
    :param str language: Target programming language.
    :param str output_dir: Target output directory.

    """
    print("ES-DOC :: MP :: Welcome to the ES-DOC meta-programming code generator !")

    # Defensive programming.
    if can_generate(ontology_schema, language, output_dir):
        # Notify pre-generation.
        print("ES-DOC :: MP :: GENERATION OPTION : schema = {0}".format(ontology_schema['name']))
        print("ES-DOC :: MP :: GENERATION OPTION : schema version = {0}".format(ontology_schema['version']))
        print("ES-DOC :: MP :: GENERATION OPTION : language = {0}".format(language))
        print("ES-DOC :: MP :: GENERATION OPTION : output directory = {0}".format(output_dir))

        # Initialise ontology.
        ontology = create_ontology(ontology_schema)
        print("ES-DOC :: MP :: ONTOLOGY :: {0} (packages={1}, classes={2}, enums={3})".format(
            ontology, len(ontology.packages), len(ontology.classes), len(ontology.enums)))

        # Format ontology.
        if language in _formatters:
            _formatters[language](ontology)
            print("ES-DOC :: MP :: ONTOLOGY :: formatted for {0}".format(language))

        # Invoke generators.
        generators = create_generators(language)
        for key, factory in generators.items():
            print("ES-DOC :: MP :: GENERATOR = {0} :: generation begins".format(key))
            options = GeneratorOptions(key, language, output_dir)
            generator = factory()
            generator.execute(ontology, options)
            print("ES-DOC :: MP :: GENERATOR = {0} :: generation complete".format(key))

    print("ES-DOC :: MP :: Thank you for using the ES-DOC code generator")


def can_generate(ontology_schema, language, output_dir):
    """Verifies whether the generation options are in a state such that generation can occur.

    :param dict ontology_schema: Ontology schema definition.
    :param str language: Target programming language.
    :param str output_dir: Target output directory.

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
