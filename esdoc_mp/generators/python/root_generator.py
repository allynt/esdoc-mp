# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.generators.python.root_generator.py
   :platform: Unix, Windows
   :synopsis: Generates root package initialisation code.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.generators import generator_utils as gu
from esdoc_mp.generators.generator import Generator
from esdoc_mp.generators.python import utils as pgu



# Generator language.
_LANG = 'python'

# Template for package.
_TEMPLATE_PACKAGE_1 = 'root_package_1.txt'

# Template for package.
_TEMPLATE_PACKAGE_2 = 'root_package_2.txt'

# Set of template files.
_TEMPLATE_FILES = (
    _TEMPLATE_PACKAGE_1,
    _TEMPLATE_PACKAGE_2,
)

# Loaded templates.
_TEMPLATES = gu.load_templates(_LANG, _TEMPLATE_FILES)



class RootGenerator(Generator):
    """Generates root level packages.

    """
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        return [
            (
                _TEMPLATES[_TEMPLATE_PACKAGE_1],
                pgu.get_ontology_directory(ctx, include_version=False),
                pgu.get_package_init_file_name()
            ),
            (
                _TEMPLATES[_TEMPLATE_PACKAGE_2],
                pgu.get_ontology_directory(ctx),
                pgu.get_package_init_file_name()
            )
        ]

