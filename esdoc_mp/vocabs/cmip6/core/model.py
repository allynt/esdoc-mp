# -*- coding: utf-8 -*-

"""
.. module:: core.py
   :platform: Unix, Windows
   :synopsis: Core repesentation in memory of CMIP6 vocab definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect

from esdoc_mp.vocabs.cmip6 import schema



# Base url for linking back to meta-definitions.
_URL = "https://github.com/ES-DOC/esdoc-mp/blob/master/esdoc_mp/vocabs/"


class Vocab(object):
    """Wraps the definitions of the CMIP6 vocab.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.description = "{}.".format(schema.__doc__.split(".")[0])
        self.id = "cmip6"
        self.style_type = "vocab"
        self.url = "{}{}".format(_URL, self.id.replace(".", "/"))
        self.realms = [Realm(self, i) for i in schema.realms]


class Realm(object):
    """Wraps the definitions of a CMIP6 science realm definition.

    """
    def __init__(self, owner, module):
        """Instance constructor.

        """
        self.description = "{}.".format(module.__doc__.split(".")[0])
        self.id = "{}.{}".format(owner.id, module.__name__.split(".")[-1])
        self.name = module.__name__.split(".")[-1]
        self.style_type = "realm"
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
        self.name = module.__name__.split(".")[-1]
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
        self.module = module
        self.name = module.__name__.split(".")[-1]
        self.style_type = "sub-process"
        self.url = "{}{}.py".format(_URL, self.id.replace(".", "/"))
        self.details = [Detail(self, m[1], m[0])
                        for m in inspect.getmembers(module)
                        if inspect.isfunction(m[1]) and not m[0].startswith("_")]

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
        self.name = name
        self.owner = owner
        self.style_type = "detail"
        self.line_begin, self.line_end = _get_line_numbers(owner.module, name)
        self.url = "{}#L{}-L{}".format(owner.url, self.line_begin, self.line_end)
        self.properties = [DetailProperty(self, i.replace("_", "-"), v)
                           for i, v in func().items()]

    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-")),
            ("Python Definition", self.url)
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
        self.name = name
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
            ("Type", self.type),
            ("Cardinality", self.cardinality)
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


def _get_line_numbers(module, func_name=None):
    """Returns line numbers within which a definition is defined.

    """
    begin, end = 0, 0
    with open(inspect.getfile(module).replace(".pyc", ".py"), 'r') as f:
        if func_name is None:
            end = len(f.readlines())
        else:
            for line_no, line in enumerate(f.readlines()):
                if begin and line.startswith("def"):
                    end = line_no - 2
                    break
                if not begin and line.startswith("def {}()".format(func_name)):
                    begin = line_no + 1
    if func_name and begin and not end:
        end = line_no + 1

    return begin, end
