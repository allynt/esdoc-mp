# -*- coding: utf-8 -*-

"""
.. module:: core.py
   :platform: Unix, Windows
   :synopsis: Core repesentation in memory of CMIP6 vocab definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect

from esdoc_mp.vocabs import cmip6



# Base url for linking back to meta-definitions.
_URL = "https://github.com/ES-DOC/esdoc-mp/blob/master/esdoc_mp/vocabs/"


class Vocab(object):
    """Wraps the definitions of the CMIP6 vocab.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.description = "{}.".format(cmip6.__doc__.split(".")[0])
        self.id = ".".join(cmip6.__name__.split(".")[-1:])
        self.style_type = "vocab"
        self.url = "{}{}".format(_URL, self.id.replace(".", "/"))
        self.domains = [Domain(self, i) for i in cmip6.domains]


class Domain(object):
    """Wraps the definitions of a CMIP6 science domain definition.

    """
    def __init__(self, owner, module):
        """Instance constructor.

        """
        self.description = "{}.".format(module.__doc__.split(".")[0])
        self.id = "{}.{}".format(owner.id, module.__name__.split(".")[-1])
        self.style_type = "domain"
        self.url = "{}{}".format(_URL, self.id.replace(".", "/"))
        self.processes = [Process(self, i) for i in module.processes]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-")),
            ("Python Definition", self.url)
        ]


class Process(object):
    """Wraps the definitions of a CMIP6 science process definition.

    """
    def __init__(self, owner, module):
        """Instance constructor.

        """
        self.description = "{}.".format(module.__doc__.split(".")[0])
        self.id = "{}.{}".format(owner.id, module.__name__.split(".")[-1])
        self.style_type = "process"
        self.url = "{}{}".format(_URL, self.id.replace(".", "/"))

        self.sub_processes = [SubProcess(self, i) for i in module.sub_processes]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-")),
            ("Python Definition", self.url)
        ]


class SubProcess(object):
    """Wraps the definitions of a CMIP6 science sub-process definition.

    """
    def __init__(self, owner, module):
        """Instance constructor.

        """
        self.description = "{}.".format(module.__doc__.split(".")[0])
        self.id = "{}.{}".format(owner.id, module.__name__.split(".")[-1])
        self.style_type = "sub-process"
        self.url = "{}{}.py".format(_URL, self.id.replace(".", "/"))

        self.details = [Detail(self, m[1], m[0])
                        for m in inspect.getmembers(module)
                        if not m[0].startswith("_")]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-")),
            ("Python Definition", self.url)
        ]


class Detail(object):
    """Wraps the definitions of a CMIP6 detail definition.

    """
    def __init__(self, owner, func, name):
        """Instance constructor.

        """
        self.description = "{}.".format(func.__doc__.split(".")[0])
        self.id = "{}.{}".format(owner.id, name)
        self.style_type = "detail"
        self.url = None
        self.properties = [DetailProperty(self, i.replace("_", "-"), v)
                           for i, v in func().items()]

    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-"))
        ]


class DetailProperty(object):
    """Wraps the definitions of a CMIP6 detail property definition.

    """
    def __init__(self, owner, name, obj):
        """Instance constructor.

        """
        self.cardinality = obj['cardinality']
        self.description = obj.get("description", None)
        self.id = "{}.{}".format(owner.id, name)
        self.style_type = "detail-property"
        self.is_enum = obj['type'] == 'enum'
        self.type = obj['type']
        self.choices = [EnumChoice(self, c[0], c[1])
                        for c in obj.get('choices', [])]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-")),
            ("Cardinality", self.cardinality),
            ("Type", self.type)
        ]


class EnumChoice(object):
    """Wraps the definitions of a CMIP6 enumeration choice definition.

    """
    def __init__(self, owner, value, description):
        """Instance constructor.

        """
        self.description = description
        self.id = "{}.{}".format(owner.id, value)
        self.value = value
        self.style_type = "enum-choice"


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-"))
        ]
