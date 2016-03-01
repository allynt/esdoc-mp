# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.ontologies.generators.generator_options
   :platform: Unix, Windows
   :synopsis: Encapsulates set of generator options.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



class GeneratorOptions(object):
    """Encapsulates set of generator options.

    """
    def __init__(self, key, language, io_dir):
        """Instance constructor.

        :param str key: Key assigned to generator.
        :param str language: Target code generation programming language.
        :param str io_dir: Directory to which output will be generated.

        """
        self.generator_key = key
        self.language = language.lower()
        self.output_dir = io_dir
