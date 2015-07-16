# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.generators.generator_context
   :platform: Unix, Windows
   :synopsis: Encpasulates contextual information used by generators.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



class GeneratorContext(object):
    """Encpasulates contextual information passed to generators.

    :ivar ontology: Ontology being processed.
    :ivar options: Generation options.

    """
    def __init__(self, ontology, options):
        """Instance constructor.

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

        :param esdoc_mp.core.Package pkg: An ontology package being processed.

        """
        self.pkg = pkg
        self.cls = None
        self.enum = None


    def set_class(self, cls):
        """Sets current class type being processed.

        :param esdoc_mp.core.Class cls: A class type being processed.

        """
        self.pkg = cls.package
        self.cls = cls
        self.enum = None


    def set_enum(self, enum):
        """Sets current enumerated type being processed.

        :param esdoc_mp.core.Enum enum: An enumerated type being processed.

        """
        self.pkg = enum.package
        self.cls = None
        self.enum = enum
