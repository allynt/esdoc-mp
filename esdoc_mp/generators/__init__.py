"""
.. module:: esdoc_mp.generators.__init__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp generators sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

from esdoc_mp import utils
from esdoc_mp import schemas

from esdoc_mp.core.factory import create_ontology
from esdoc_mp.generators.factory import create_generators
from esdoc_mp.generators.generator_options import GeneratorOptions
from esdoc_mp.generators.python.utils import format as format_python



# Set of formatters keyed by programming language.
_formatters = {
    'python' : format_python
}


# Set of supported programming languages.
_LANGUAGES = {
    'c++',
    'fortran',
    'java',
    'javascript',
    'python',
}


def _validate_language(language):
    """Returns list of target programming language validation errors.

    """
    if not language in _LANGUAGES:
        return ['Programming language is unsupported [{0}].  Supported languages are {1}.'.format(language, _LANGUAGES)]

    return []


def _validate_output_dir(output_dir):
    """Returns list of target output directory validation errors.

    """
    if not os.path.exists(output_dir):
        return ['Output directory does not exist [{0}].'.format(output_dir)]

    return []


def generate(schema, language, io_dir):
    """Generates code.

    :param module schema: Ontology schema definition.
    :param str language: Target programming language.
    :param str io_dir: Target I/O directory.

    """
    if not can_generate(schema, language, io_dir):
        return

    utils.log("Welcome to the ES-DOC meta-programming code generator !")
    utils.log("GENERATION OPTION : ontology schema = {0} v{1}".format(schema.NAME, schema.VERSION))
    utils.log("GENERATION OPTION : programming language = {0}".format(language))
    utils.log("GENERATION OPTION : output directory = {0}".format(io_dir))

    # Initialise ontology.
    ontology = create_ontology(schema)
    utils.log("ONTOLOGY :: {0} (packages={1}, classes={2}, enums={3})".format(
        ontology, len(ontology.packages), len(ontology.classes), len(ontology.enums)))

    # Apply language specific pre-generator formatter.
    if language in _formatters:
        _formatters[language](ontology)
        utils.log("ONTOLOGY :: formatted for {0}".format(language))

    # Invoke language specific generators.
    generators = create_generators(language)
    for key, factory in generators.items():
        utils.log("GENERATOR = {0} :: generation begins".format(key))
        options = GeneratorOptions(key, language, io_dir)
        generator = factory()
        generator.execute(ontology, options)
        utils.log("GENERATOR = {0} :: generation complete".format(key))

    utils.log("Thank you for using the ES-DOC code generator")


def can_generate(schema, language, output_dir):
    """Verifies whether the generation options are in a state such that generation can occur.

    :param module schema: Ontology schema definition.
    :param str language: Target programming language.
    :param str io_dir: Target I/O directory.

    :returns: True if generation can occur, False otherwise.
    :rtype: bool

    """
    errors = _validate_language(language)
    errors += schemas.validate(schema)
    errors += _validate_output_dir(output_dir)
    if errors:
        utils.log("-------------------------------------------------------------------")
        for error in errors:
            utils.log("VALIDATION ERROR :: {0}".format(error))

    return len(errors) == 0
