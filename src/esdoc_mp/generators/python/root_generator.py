"""
.. module:: esdoc_mp.generators.python.root_generator.py
   :platform: Unix, Windows
   :synopsis: Generates root package initialisation code.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
from esdoc_mp.generators.generator import Generator
import esdoc_mp.generators.generator_utils as gu
import esdoc_mp.generators.python.utils as pgu


# Generator language.
_LANG = 'python'

# Template for package.
_TEMPLATE_PACKAGE_1 = 'root_package_1.txt'

# Template for package.
_TEMPLATE_PACKAGE_2 = 'root_package_2.txt'

# Set of template files.
_template_files = (
    _TEMPLATE_PACKAGE_1,
    _TEMPLATE_PACKAGE_2,
)

# Loaded templates.
_templates = gu.load_templates(_LANG, _template_files)



class RootGenerator(Generator):
    """Generates root level packages.

    """
    
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        def get_code(template, include_version):
            return (_templates[template], \
                    pgu.get_ontology_directory(ctx, include_version=include_version), \
                    pgu.get_package_init_file_name())

        return [
            get_code(_TEMPLATE_PACKAGE_1, False),
            get_code(_TEMPLATE_PACKAGE_2, True)
        ]


