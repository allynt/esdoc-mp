"""
.. module:: esdoc_mp.generators.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp generators sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.core.factory import create_ontology
from esdoc_mp.generators.factory import create_generators
from esdoc_mp.generators.generator_options import GeneratorOptions
from esdoc_mp.generators.python.utils import format as format_python
from esdoc_mp.utils.validation import validate_language
from esdoc_mp.utils.validation import validate_schema
from esdoc_mp.utils.validation import validate_output_dir




# Set of formatters keyed by programming language.
_formatters = {
    'python' : format_python
}


def _log(msg):
    """Logging helper function.

    """
    if msg.startswith('-'):
        print(msg)
    else:
        print("ES-DOC :: MP :: {}".format(msg))


def generate(schema, language, io_dir):
    """Generates code.

    :param module schema: Ontology schema definition.
    :param str language: Target programming language.
    :param str io_dir: Target I/O directory.

    """
    if can_generate(schema, language, io_dir) == False:
        return

    _log("Welcome to the ES-DOC meta-programming code generator !")
    _log("GENERATION OPTION : schema = {0}".format(schema.NAME))
    _log("GENERATION OPTION : schema version = {0}".format(schema.VERSION))
    _log("GENERATION OPTION : language = {0}".format(language))
    _log("GENERATION OPTION : output directory = {0}".format(io_dir))

    # Initialise ontology.
    ontology = create_ontology(schema)
    _log("ONTOLOGY :: {0} (packages={1}, classes={2}, enums={3})".format(
        ontology, len(ontology.packages), len(ontology.classes), len(ontology.enums)))

    # Apply language specific pre-generator formatter.
    if language in _formatters:
        _formatters[language](ontology)
        _log("ONTOLOGY :: formatted for {0}".format(language))

    # Invoke language specific generators.
    generators = create_generators(language)
    for key, factory in generators.items():
        _log("GENERATOR = {0} :: generation begins".format(key))
        options = GeneratorOptions(key, language, io_dir)
        generator = factory()
        generator.execute(ontology, options)
        _log("GENERATOR = {0} :: generation complete".format(key))

    _log("Thank you for using the ES-DOC code generator")


def can_generate(schema, language, output_dir):
    """Verifies whether the generation options are in a state such that generation can occur.

    :param module schema: Ontology schema definition.
    :param str language: Target programming language.
    :param str io_dir: Target I/O directory.

    :returns: True if generation can occur, False otherwise.
    :rtype: bool

    """
    errors = validate_language(language)
    errors += validate_schema(schema)
    errors += validate_output_dir(output_dir)
    if errors:
        _log("-------------------------------------------------------------------")
        _log("INVALID GENERATOR OPTIONS !!!")
        for error in errors:
            _log("GENERATOR OPTION ERROR :: {0}".format(error))

    return len(errors) == 0
