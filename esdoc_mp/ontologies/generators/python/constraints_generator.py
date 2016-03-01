# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.ontologies.generators.python.constraints_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code encapsulating an ontology's constraints.

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
_TEMPLATE_CONSTRAINTS = 'constraints.txt'

# Loaded templates.
_TEMPLATES = gu.load_templates(_LANG, (
    _TEMPLATE_CONSTRAINTS,
))


class ConstraintsGenerator(Generator):
    """Generates code to represent an ontology as a set of types.

    """
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        return [
            (
                _emit_module_constraints(ctx.ontology),
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('constraints')
            )
        ]


def _emit_module_constraints(o):
    """Emits constraints module.

    """
    def emit_constraint_set(c):
        """Emit a constraint set.

        """
        def get_code(ct):
            name, typeof, value = ct
            if typeof == 'type':
                value = pgu.get_type_functional_name(value, True)
            else:
                value = "'{}'".format(value)
            code = gu.emit_indent(2)
            code += "('{}', '{}', {}),".format(name, typeof, value)
            code += gu.emit_line_return()

            return code

        return gu.emit(c.all_constraints, get_code)


    def emit_class_constraints():
        """Emit set of class constraints.

        """
        def get_code(c):
            return "{}{}: ({}{}),{}".format(
                gu.emit_indent(),
                c.op_full_name,
                gu.emit_line_return() + emit_constraint_set(c),
                gu.emit_indent(),
                gu.emit_line_return(2))

        return gu.emit(o.classes, get_code)


    code = _TEMPLATES[_TEMPLATE_CONSTRAINTS]
    code = code.replace('{module-imports-packages}', pgu.emit_package_imports(o))
    code = code.replace('{constraints}', emit_class_constraints())

    return code
