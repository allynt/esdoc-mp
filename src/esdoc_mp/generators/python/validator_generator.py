"""
.. module:: esdoc_mp.generators.python.validation_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code to perform type instance validation.

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
_TEMPLATE_MAIN = "validator.txt"

# Template for a validator module.
_TEMPLATE_VALIDATOR_MODULE = 'validator_module.txt'

# Template for a validator function.
_TEMPLATE_VALIDATOR_FUNCTION = "validator_function.txt"

# Set of template files.
_template_files = (
    _TEMPLATE_VALIDATOR_MODULE,
    _TEMPLATE_VALIDATOR_FUNCTION,
    _TEMPLATE_MAIN,
)

# Loaded templates.
_templates = gu.load_templates(_LANG, _template_files)



class ValidatorGenerator(Generator):
    """Generates code to perform type instance validation.

    """
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return (
            _emit_module_init(ctx.ontology),
            pgu.get_ontology_directory(ctx),
            pgu.get_module_file_name('validator')
        )


    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return (
            _emit_module_validation_for_pkg(ctx.ontology, ctx.pkg),
            pgu.get_ontology_directory(ctx),
            pgu.get_package_module_file_name(ctx.pkg, 'validator')
        )


def _emit_module_init(o):
    """Emits package initialisation file."""
    def emit_imports():
        def emit_code_1(code, p):
            code += "from {0} import *".format(
                pgu.get_package_module_name(p, 'validator'))
            code += gu.emit_line_return()

            return code

        def emit_code_2(code, p):
            code += "import {0} as {1}".format(
                pgu.get_package_module_name(p, 'validator'),
                p.op_name)
            code += gu.emit_line_return()

            return code

        return reduce(emit_code_1, o.packages, str()) + \
               reduce(emit_code_2, o.packages, gu.emit_line_return())


    def emit_exports():
        def emit_code(code, c):
            code += "{0}\'{1}\',{2}".format(
                gu.emit_indent(),
                _get_validator_function_name(c),
                gu.emit_line_return())

            return code

        return reduce(emit_code, o.classes, str())


    def emit_supported_validator_list():
        def emit_code(code, c):
            code += gu.emit_indent()
            code +=  c.package.op_name
            code += '.'
            code +=  _get_validator_function_name(c)
            code += ','
            code += gu.emit_line_return()

            return code

        return reduce(emit_code, o.classes, str())


    code = _templates[_TEMPLATE_MAIN]
    code = code.replace('{module-imports}', emit_imports())
    code = code.replace('{module-exports}', emit_exports())
    code = code.replace('{supported-validator-list}', emit_supported_validator_list())

    return code


def _emit_module_validation_for_pkg(o, p):
    """Emits validation module for an ontology package."""
    def emit_imports():
        return ''

    def get_imports():
        imports = []

        def append_import(imp):
            if imp not in imports:
                imports.append(imp)

        # Set type decoding imports.
        for type in [t for t in p.external_types if t.is_class]:
            imp = 'from {0} import *'.format(
                pgu.get_package_module_name(type.name_of_package, 'validator'))
            append_import(imp)

        if len(imports) > 0:
            return reduce(add, map(lambda i : i + gu.emit_line_return(), sorted(imports)))
        else:
            return ''


    code = _templates[_TEMPLATE_VALIDATOR_MODULE]
    code = code.replace('{module-imports}', get_imports())
    code = code.replace('{validation-functions}', _emit_snippet_validator_fns(p))
    code = code.replace('{package-name}', p.op_name)

    return code


def _emit_snippet_validator_fns(p):
    """Emits set of validator functions."""
    def emit_code(code, c):
        fn = _templates[_TEMPLATE_VALIDATOR_FUNCTION]
        fn = fn.replace('{class-name}', c.op_name)
        fn = fn.replace('{class-function-body}', _emit_snippet_validator_fn(c))
        fn = fn.replace('{class-function-name}', pgu.get_class_functional_name(c))
        fn = fn.replace('{class-doc-name}', pgu.get_class_doc_string_name(c))

        return code + fn

    return reduce(emit_code, p.classes, str())


def _emit_snippet_validator_fn(c):
    """Emits a validator function."""
    return "return NotImplementedError()"


def _get_validator_function_name(name):
    """Converts name to a python class validator function name."""
    return 'validate_{0}'.format(pgu.get_class_functional_name(name))
