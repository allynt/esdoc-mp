# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.ontologies.generators.python.typeset_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code encapsulating an ontology's typeset.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.ontologies.generators import generator_utils as gu
from esdoc_mp.ontologies.generators.python import utils as pgu
from esdoc_mp.ontologies.generators.generator import Generator



# Generator language.
_LANG = 'python'

# Template for main module.
_TEMPLATE_MAIN = "typeset.txt"

# Loaded templates.
_TEMPLATES = gu.load_templates(_LANG, (
    _TEMPLATE_MAIN,
))


class TypeSetGenerator(Generator):
    """Generates code to represent an ontology as a set of types.

    """
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        return [
            (
                _emit_module_init(ctx.ontology),
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('typeset')
            )
        ]


def _emit_module_init(o):
    """Emits package initializer.

    """
    def emit_type_keys():
        def get_code(c):
            code = "{0}.type_key = u'{1}.{2}.{0}'".format(
                c.op_full_name,
                o.op_name,
                o.op_version)
            code += gu.emit_line_return()

            return code

        return gu.emit(o.classes, get_code)


    def emit_type_attribute_info(c):
        def get_code(p):
            code = gu.emit_indent()
            code += "('{0}', {1}, {2}, {3}),".format(
                pgu.get_property_name(p),
                pgu.get_type_functional_name(p.type, True),
                p.is_required,
                p.is_iterative)
            code += gu.emit_line_return()

            return code

        return gu.emit(c.properties, get_code)


    def emit_type_info():
        def get_code(c):
            code = "# Set class type info (property-name, property-type, property-is-required, property-is-iterable)."
            code += gu.emit_line_return()
            code += "{0}.type_info = ({1})".format(
                c.op_full_name,
                gu.emit_line_return() + emit_type_attribute_info(c))
            code += gu.emit_line_return(2)

            return code

        return gu.emit(o.classes, get_code)

    def emit_type_imports():
        def get_code(p):
            code = "from {0} import *".format(
                pgu.get_package_module_name(p, 'typeset'))
            code += gu.emit_line_return()

            return code

        return gu.emit(o.packages, get_code)


    def emit_exports(collection):
        def get_code(p):
            return "{0}\'{1}\',{2}".format(
                gu.emit_indent(),
                p.op_name,
                gu.emit_line_return())

        return gu.emit(collection, get_code)


    def emit_supported_package_list():
        def get_code(p):
            return "{0}{1},{2}".format(
                gu.emit_indent(),
                p.op_name,
                gu.emit_line_return())

        return gu.emit(o.packages, get_code)


    def emit_supported_type_list():
        def get_code(c):
            return "{0}{1},{2}".format(
                gu.emit_indent(),
                c.op_full_name,
                gu.emit_line_return())

        return gu.emit(o.classes, get_code)


    code = _TEMPLATES[_TEMPLATE_MAIN]
    code = code.replace('{module-imports-packages}', pgu.emit_package_imports(o))
    code = code.replace('{module-imports-types}', emit_type_imports())
    code = code.replace('{module-exports-packages}', emit_exports(o.packages))
    code = code.replace('{module-exports-types}', emit_exports(o.classes))
    code = code.replace('{supported-package-list}', emit_supported_package_list())
    code = code.replace('{supported-type-list}', emit_supported_type_list())
    code = code.replace('{type-keys}', emit_type_keys())
    code = code.replace('{type-info}', emit_type_info())

    return code
