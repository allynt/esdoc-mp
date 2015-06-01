# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.generators.python.serialization_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code to support serialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
from operator import add

from esdoc_mp.generators.generator import Generator
import esdoc_mp.generators.generator_utils as gu
import esdoc_mp.generators.python.utils as pgu



# Generator language.
_LANG = 'python'

# Template for main module.
_TEMPLATE_MAIN = "decoder.txt"

# Template for a decoder module.
_TEMPLATE_DECODER_MODULE = 'decoder_module.txt'

# Template for a decoder function.
_TEMPLATE_DECODER_FUNCTION = "decoder_function.txt"

# Template for a decoding xml utilities.
_TEMPLATE_DECODER_XML_UTILS = "decoder_xml_utils.txt"

# Set of template files.
_template_files = (
    _TEMPLATE_MAIN,
    _TEMPLATE_DECODER_MODULE,
    _TEMPLATE_DECODER_FUNCTION,
    _TEMPLATE_DECODER_XML_UTILS,
)

# Loaded templates.
_templates = gu.load_templates(_LANG, _template_files)



class DecoderGenerator(Generator):
    """Generates code to support decoding.

    """
    def is_required(self, ctx):
        """Predicate determing whether code generation is required.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return bool(ctx.ontology.decodings)


    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return [
            (
                _emit_module_init(ctx.ontology),
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('decoder')
            ),
            (
                _templates[_TEMPLATE_DECODER_XML_UTILS],
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('decoder_xml_utils')
            )
        ]

    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return (
            _emit_module_decoder_for_pkg(ctx.ontology, ctx.pkg),
            pgu.get_ontology_directory(ctx),
            pgu.get_package_module_file_name(ctx.pkg, 'decoder')
        )


def _emit_module_decoder_for_pkg(o, p):
    """Emits package decoder module."""
    code = _templates[_TEMPLATE_DECODER_MODULE]
    code = code.replace('{module-imports}', _emit_snippet_decoder_imports(o, p))
    code = code.replace('{decoding-functions}', _emit_snippet_decoding_fns(p))

    return code


def _emit_snippet_decoder_imports(o, p):
    """Emits set of package decoder imports."""
    imports = []

    def append_import(imp):
        if imp not in imports:
            imports.append(imp)

    # Set type decoding imports.
    for type in [t for t in p.external_types if t.is_class]:
        imp = 'from {0} import *'.format(
            pgu.get_package_module_name(type.name_of_package, 'decoder'))
        append_import(imp)

    if len(imports) > 0:
        return reduce(add, map(lambda i : i + gu.emit_line_return(), sorted(imports)))
    else:
        return ''


def _emit_snippet_decoding_fns(p):
    """Emits set of package class decodings."""
    code = ''
    for cls in p.classes:
        fn = _templates[_TEMPLATE_DECODER_FUNCTION]
        fn = fn.replace('{class-name}', cls.op_name)
        fn = fn.replace('{class-function-name}', pgu.get_class_functional_name(cls))
        fn = fn.replace('{package-name}', cls.package.op_name)
        fn = fn.replace('{class-doc-name}', pgu.get_class_doc_string_name(cls))
        fn = fn.replace('{class-decodings}', _emit_snippet_decodings(cls))
        fn += gu.emit_line_return(3)
        code += fn

    return code


def _emit_snippet_decodings(c):
    """Emits a set of class decodings."""
    code = ''
    for p in c.all_properties:
        for dc in c.get_property_decodings(p):
            if dc.decoding is not None:
                code += _emit_snippet_decoding(p, dc.decoding, dc.type)

    return code


def _emit_snippet_decoding(prp, decoding, type):
    """Emits a class property decoding."""
    def get_decoding_function():
        # ... simple/enum types - return type functional name
        #     (is directly mapped to a convertor function).
        if prp.type.is_simple or prp.type.is_enum:
            return '\'{0}\''.format(pgu.get_type_functional_name(prp.type))
        # ... complex classes - return class functional name.
        elif prp.type.is_class:
            type_name = prp.type.name if type is None else type
            return _get_decoder_function_name(type_name)

    tmpl = '{0}(\'{1}\', {2}, {3}, \'{4}\'),'
    return tmpl.format(
        gu.emit_line_return() + gu.emit_indent(2),
        prp.name,
        prp.is_iterative,
        get_decoding_function(),
        '' if decoding is None else decoding)


def _emit_module_init(o):
    """Emits package initializer."""
    def get_imports():
        def emit_code(code, c):
            return code + "from {0} import {1}".format(
                pgu.get_package_module_name(c.package, 'decoder'),
                _get_decoder_function_name(c)) + gu.emit_line_return()

        return reduce(emit_code, o.entities, str())

    code = _templates[_TEMPLATE_MAIN]
    code = code.replace('{module-imports}', get_imports())

    return code


def _get_decoder_function_name(name):
    """Converts class name to a decoder function name."""
    return 'decode_{0}'.format(pgu.get_class_functional_name(name))