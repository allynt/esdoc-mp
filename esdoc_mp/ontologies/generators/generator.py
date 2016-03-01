# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.ontologies.generators.generator
   :platform: Unix, Windows
   :synopsis: Base class encapsulating functionality common to all cim code generators.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from abc import ABCMeta

from esdoc_mp.ontologies.generators import generator_utils as gu
from esdoc_mp.ontologies.generators.generator_context import GeneratorContext



class Generator(object):
    """Base class encapsulating functionality common to all code generators.

    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def execute(self, ontology, options):
        """Executes the code generator.

        :param esdoc_mp.ontologies.core.Ontology ontology: Ontology being processed.
        :param esdoc_mp.generator.GeneratorOptions options: Generation options.

        """
        # Instantiate context.
        ctx = GeneratorContext(ontology, options)

        # Escape if not required.
        if not self.is_required(ctx):
            return

        # Emits generated code to file system.
        def emit_code(code):
            if code is not None:
                if not isinstance(code, list):
                    code = [code]
                for code, dir, file in code:
                    gu.write_file(gu.format_code(ctx, code), dir, file)

        # Notify start.
        self.on_start(ctx)

        # Raise parsing events and emit code accordingly.
        emit_code(self.on_ontology_parse(ctx))
        for pkg in ctx.ontology.packages:
            ctx.set_package(pkg)
            emit_code(self.on_package_parse(ctx))
        for cls in ctx.ontology.classes:
            ctx.set_class(cls)
            emit_code(self.on_class_parse(ctx))
        for enum in ctx.ontology.enums:
            ctx.set_enum(enum)
            emit_code(self.on_enum_parse(ctx))

        # Notify end.
        self.on_end(ctx)


    def is_required(self, ctx):
        """Predicate determing whether code generation is required.

        :param esdoc_mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        return True


    def on_start(self, ctx):
        """Event handler for the parsing start event.

        :param esdoc_mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_end(self, ctx):
        """Event handler for the parsing end event.

        :param esdoc_mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param esdoc_mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param esdoc_mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_class_parse(self, ctx):
        """Event handler for the class parse event.

        :param esdoc_mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_enum_parse(self, ctx):
        """Event handler for the enum parse event.

        :param esdoc_mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


