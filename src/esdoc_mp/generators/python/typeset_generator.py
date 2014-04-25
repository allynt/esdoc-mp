"""
.. module:: esdoc_mp.generators.python.typeset_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code encapsulating an ontology's typeset.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
from esdoc_mp.generators.generator import Generator
import esdoc_mp.core as ontology
import esdoc_mp.utils.runtime as rt
import esdoc_mp.generators.generator_utils as gu
import esdoc_mp.generators.python.utils as pgu



# Generator language.
_LANG = 'python'

# Template for main module.
_TEMPLATE_MAIN = "typeset.txt"

# Template for a typeset module.
_TEMPLATE_TYPESET_MODULE = 'typeset_module.txt'

# Template for typeset meta-information.
_TEMPLATE_META_MODULE = 'typeset_meta.txt'

# Template for a concrete class.
_TEMPLATE_CLASS_CONCRETE = "typeset_class_concrete.txt"

# Template for an abstract class.
_TEMPLATE_CLASS_ABSTRACT = "typeset_class_abstract.txt"

# Template for an enumeration.
_TEMPLATE_ENUM = "typeset_enum.txt"

# Set of template files.
_template_files = (
    _TEMPLATE_MAIN,
    _TEMPLATE_TYPESET_MODULE,
    _TEMPLATE_META_MODULE,
    _TEMPLATE_CLASS_CONCRETE,
    _TEMPLATE_CLASS_ABSTRACT,
    _TEMPLATE_ENUM
)

# Loaded templates.
_templates = gu.load_templates(_LANG, _template_files)


class TypesetGenerator(Generator):
    """Generates code to represent an ontology as a set of types.

    """
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return [
            (
                _emit_module_init(ctx.ontology),
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('typeset')
            ),
            (
                _emit_module_meta(ctx.ontology),
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('typeset_meta')
            )
        ]


    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return (
            _emit_module_typeset_for_pkg(ctx.ontology, ctx.pkg),
            pgu.get_ontology_directory(ctx),
            pgu.get_package_module_file_name(ctx.pkg, 'typeset')
        )


def _emit_module_meta(o):
    """Emits typeset meta-information module."""
    def emit_imports():
        def emit_code(code, p):
            code += "import {0} as {1}".format(
                pgu.get_package_module_name(p, 'typeset'),
                p.op_name)
            code += gu.emit_line_return()

            return code

        return reduce(emit_code, o.packages, str())


    def emit_type_keys():
        def emit_code(code, c):
            code += "{0}.type_key = '{1}.{2}.{0}'".format(
                c.op_full_name,
                o.op_name,
                o.op_version)
            code += gu.emit_line_return()

            return code

        return reduce(emit_code, o.classes, str())


    def emit_type_attribute_info(c):
        def emit_code(code, p):
            code += gu.emit_indent()
            code += "('{0}', {1}, {2}, {3}),".format(
                pgu.get_property_name(p),
                pgu.get_type_functional_name(p.type, True),
                p.is_required,
                p.is_iterative)
            code += gu.emit_line_return()

            return code

        return reduce(emit_code, c.properties, str())


    def emit_type_info():
        def emit_code(code, c):
            code += "{0}.type_info = ({1})".format(
                c.op_full_name,
                gu.emit_line_return() + emit_type_attribute_info(c))
            code += gu.emit_line_return(2)

            return code

        return reduce(emit_code, o.classes, str())


    code = _templates[_TEMPLATE_META_MODULE]
    code = code.replace('{module-imports}', emit_imports())
    code = code.replace('{type-keys}', emit_type_keys())
    code = code.replace('{type-info}', emit_type_info())

    return code


def _emit_module_typeset_for_pkg(o, p):
    """Emits typeset module for an ontology package."""
    def emit_imports():
        def emit_code(code, p):
            code += "import {0} as {1}".format(
                pgu.get_package_module_name(p, 'typeset'),
                p.op_name)
            code += gu.emit_line_return()

            return code

        return reduce(emit_code, p.associated, str())


    def get_classes(p):
        # Return list of classes sorted in dependency order.
        result = [c for c in p.classes if c.base is None or c.base.package != p]

        while len(result) < len(p.classes):
            n = len(result)
            for c in [c for c in p.classes if c not in result]:
                if c.base in result:
                    result.append(c)

            # Error if parse revels unresolvable dependencies.
            if n == len(result):
                msg = "Package {0} has circular class dependencies."
                msg = msg.format(p)
                rt.throw(msg.format(p))

        return result


    def emit_types():
        def emit_code(code, t):
            if isinstance(t, ontology.Class):
                code += _emit_snippet_class(t)
            else:
                code += _emit_snippet_enum(t)
            code += gu.emit_line_return(2)

            return code

        return reduce(emit_code, get_classes(p), str()) + \
               reduce(emit_code, p.enums, str())


    code = _templates[_TEMPLATE_TYPESET_MODULE]
    code = code.replace('{imports}', emit_imports())
    code = code.replace('{types}', emit_types())
    code = code.replace('{package-name}', p.op_name)

    return code


def _emit_module_init(o):
    """Emits package initializer."""
    def emit_imports():
        def emit_code_1(code, p):
            code += "from {0} import *".format(
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


    def emit_exports():
        def emit_code(code, t):
            code += "{0}\'{1}\',{2}".format(
                gu.emit_indent(),
                t.op_name,
                gu.emit_line_return())

            return code

        return reduce(emit_code, o.packages, str()) + \
               reduce(emit_code, o.classes, str())


    def emit_supported_type_list():
        def emit_code(code, c):
            code += gu.emit_indent()
            code +=  c.op_full_name
            code += ','
            code += gu.emit_line_return()

            return code

        return reduce(emit_code, o.classes, str())


    code = _templates[_TEMPLATE_MAIN]
    code = code.replace('{module-imports}', emit_imports())
    code = code.replace('{module-exports}', emit_exports())
    code = code.replace('{supported-type-list}', emit_supported_type_list())

    return code


def _emit_snippet_enum(e):
    """Emits code corresponding to a python enum."""
    code = _templates[_TEMPLATE_ENUM]
    code = code.replace('{enum-name}', pgu.get_enum_name(e))
    code = code.replace('{enum-doc-string}', e.doc_string)

    return code


def _emit_snippet_class(c):
    """Emits code corresponding to a python class."""
    # Open template.
    if c.is_abstract:
        code = _templates[_TEMPLATE_CLASS_ABSTRACT]
    else:
        code = _templates[_TEMPLATE_CLASS_CONCRETE]

    # Generate code.
    code = code.replace('{class-name}', c.op_name)
    code = code.replace('{base-class-name}', c.op_base_name)
    code = code.replace('{class-doc-string}', _emit_snippet_class_doc_string(c))
    code = code.replace('{class_constants}', _emit_snippet_class_property_constants(c))
    code = code.replace('{class-properties}', _emit_snippet_class_properties(c))

    return code


def _emit_snippet_class_doc_string(c):
    """Emits class doc string."""
    doc_string = "" if not c.doc_string else c.doc_string

    if doc_string:
        doc_string = "{0}{1}{2}".format(doc_string,
                                        gu.emit_line_return(2),
                                        gu.emit_indent())

    return "{0}{1}{2}".format(gu.emit_line_return(2),
                              gu.emit_indent(),
                              doc_string)



def _emit_snippet_class_properties(c):
    """Emits set of class properties."""
    def emit_code(code, p):
        code += "{0}{1}{2}# {3}{4}".format(
            gu.emit_indent(2),
            pgu.get_property_ctor(p),
            ''.ljust(50 - len(pgu.get_property_ctor(p))),
            pgu.get_type_doc_name(p.type),
            gu.emit_line_return()
        )

        return code

    return reduce(emit_code, c.properties, str())


def _emit_snippet_class_property_constants(c):
    """Emits set of class property constants."""
    def emit_code(code, cnt):
        prp = c.get_property(cnt[0])
        if prp is not None:
            code += '{0}self.{1} = {2}("{3}"){4}'.format(
                gu.emit_indent(2),
                cnt[0],
                pgu.get_type_functional_name(prp.type),
                cnt[1],
                gu.emit_line_return()
            )

        return code

    return reduce(emit_code, c.constants, str())
