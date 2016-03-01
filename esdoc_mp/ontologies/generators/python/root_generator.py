# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.ontologies.generators.python.root_generator.py
   :platform: Unix, Windows
   :synopsis: Generates root package initialisation code.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.ontologies.generators import generator_utils as gu
from esdoc_mp.ontologies.generators.generator import Generator
from esdoc_mp.ontologies.generators.python import utils as pgu



# Generator language.
_LANG = 'python'

# Template for package.
_TEMPLATE_PACKAGE = 'root_package.txt'

# Loaded templates.
_TEMPLATES = gu.load_templates(_LANG, (
    _TEMPLATE_PACKAGE,
))



class RootGenerator(Generator):
    """Generates root level packages.

    """
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        return [
            (
                _TEMPLATES[_TEMPLATE_PACKAGE],
                pgu.get_ontology_directory(ctx),
                pgu.get_package_init_file_name()
            )
        ]

