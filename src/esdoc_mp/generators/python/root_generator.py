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
        return [
            (
                _emit_module_init(ctx.ontology),
                pgu.get_ontology_directory(ctx, include_version=False),
                pgu.get_package_init_file_name()
            ),
            (
                _templates[_TEMPLATE_PACKAGE_2],
                pgu.get_ontology_directory(ctx),
                pgu.get_package_init_file_name()
            )
        ]


def _emit_module_init(o):
    """Emits package initializer."""
    def emit_imports():
        def emit_code_1(code):
            code += "from v{0} import *".format(
                pgu.get_package_module_name(p, 'typeset'))
            code += gu.emit_line_return()

            return code

        def emit_code_2(code, p):
            code += "import {0} as {1}".format(
                pgu.get_package_module_name(p, 'typeset'),
                p.op_name)
            code += gu.emit_line_return()

            return code

        return reduce(emit_code_1, o.packages, str()) + \
               reduce(emit_code_2, o.packages, gu.emit_line_return())


    code = _templates[_TEMPLATE_PACKAGE_1]
    #code = code.replace('{module-imports}', emit_imports())

    return code
