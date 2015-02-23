# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.generators.generator_context
   :platform: Unix, Windows
   :synopsis: Encpasulates contextual information used by generators.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



class GeneratorContext(object):
    """Encpasulates contextual information used by generators.

    :ivar ontology: Ontology being processed.
    :ivar options: Generation options.

    """
    def __init__(self, ontology, options):
        """Constructor.

        :param ontology: Ontology being processed.
        :param options: Generation options.
        :type ontology: esdoc_mp.core.Ontology
        :type options: esdoc_mp.GeneratorOptions

        """
        self.ontology = ontology
        self.options = options
        self.pkg = None
        self.cls = None
        self.enum = None
        

    @property
    def language(self):
        """Gets target programming language."""
        return self.options.language


    @property
    def generator_key(self):
        """Gets generator key."""
        return self.options.generator_key


    @property
    def output_dir(self):
        """Gets target output directory."""
        return self.options.output_dir


    def set_package(self, pkg):
        """Sets current package being processed.

        :param pkg: An ontology package being processed.
        :type pkg: esdoc_mp.core.package.Package

        """
        self.pkg = pkg
        self.cls = None
        self.enum = None


    def set_class(self, cls):
        """Sets current class type being processed.

        :param cls: A class type being processed.
        :type cls: esdoc_mp.core.class_.Class

        """
        self.pkg = cls.package
        self.cls = cls
        self.enum = None


    def set_enum(self, enum):
        """Sets current enumerated type being processed.

        :param enum: An enumerated type being processed.
        :type enum: esdoc_mp.core.enum.Enum

        """
        self.pkg = enum.package
        self.cls = None
        self.enum = enum
