# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.ontologies.generators.python.typekey_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code encapsulating an ontology's type keys.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.ontologies import core
from esdoc_mp.ontologies.generators import generator_utils as gu
from esdoc_mp.ontologies.generators.python import utils as pgu
from esdoc_mp.ontologies.generators.generator import Generator
from esdoc_mp import utils



# Generator language.
_LANG = 'python'

# Template for the constraints module.
_TEMPLATE_KEYS = 'typekey.txt'

# Loaded templates.
_TEMPLATES = gu.load_templates(_LANG, (
    _TEMPLATE_KEYS,
))


class TypeKeyGenerator(Generator):
    """Generates code that maps an ontology type to it's key.

    """
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        return [
            (
                _emit_typekeys(ctx.ontology),
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('typekey')
            )
        ]


def _emit_typekeys(o):
    """Emits typekeys module.

    """
    def emit_typekey():
        """Emit a class type key.

        """
        def get_code(c):
            return "{}{}: '{}.{}.{}',{}".format(
                gu.emit_indent(),
                c.op_full_name,
                o.op_name,
                o.op_version,
                c.op_full_name,
                gu.emit_line_return())

        return gu.emit(o.classes, get_code)


    code = _TEMPLATES[_TEMPLATE_KEYS]
    code = code.replace('{module-imports-packages}', pgu.emit_package_imports(o))
    code = code.replace('{typekeys}', emit_typekey())

    return code
