import inspect

from esdoc_mp.utils import log



# Base url for linking back to meta-definitions.
_URL = "https://github.com/ES-DOC/esdoc-mp/blob/master/esdoc_mp/vocabs/"


class VocabParser(object):
    """Parses CMIP6 vocab raising events as it does so.

    """
    def __init__(self, domain_filter=None):
        """Instance constructor.

        """
        self.domain_filter = domain_filter

    def parse(self):
        """Parses the CMIP6 vocabulary.

        """
        vocab = Vocab()

        log("parsing: {}".format(vocab))
        self.on_vocab_parse(vocab)

        for domain in vocab.domains:
            if self.domain_filter and self.domain_filter == domain.name:
                continue
            log("parsing: {}".format(domain))
            self.on_domain_parse(domain)

            for process in sorted(domain.processes, key = lambda p: p.name):
                log("parsing: {}".format(process))
                self.on_process_parse(domain, process)

                for sub_process in sorted(process.sub_processes, key = lambda sp: sp.name):
                    log("parsing: {}".format(sub_process))
                    self.on_subprocess_parse(process, sub_process)

                    for detail in sub_process.details:
                        log("parsing: {}".format(detail))
                        self.on_detail_parse(sub_process, detail)

                        for detail_property in detail.properties:
                            log("parsing: {}".format(detail_property))
                            self.on_detail_property_parse(detail, detail_property)


    def on_vocab_parse(self, vocab):
        """On vocabulary parse event handler.

        """

        pass


    def on_domain_parse(self, domain):
        """On domain parse event handler.

        """
        pass


    def on_process_parse(self, domain, process):
        """On process parse event handler.

        """
        pass


    def on_subprocess_parse(self, process, subprocess):
        """On sub-process parse event handler.

        """
        pass


    def on_detail_parse(self, owner, detail):
        """On detail parse event handler.

        """
        pass


    def on_detail_property_parse(self, owner, detail):
        """On process detail parse event handler.

        """
        pass


class _Node(object):
    """Represents a node in the vocab.

    """
    def __init__(self, module, depth):
        """Instance constructor.

        """
        self._module = module
        self._depth = depth


    def __repr__(self):
        """Instance representation.

        """
        return "{}".format(self.id)


    @property
    def description(self):
        """Node description.

        """
        return "{}.".format(self._module.__doc__.split(".")[0])


    @property
    def id(self):
        """Node identifier.

        """
        return ".".join(self._module.__name__.split(".")[0 - self._depth:])


    @property
    def name(self):
        """Node canonical name.

        """
        return self._module.__name__.split(".")[-1].replace("_", "-")


    @property
    def type(self):
        """Node type.

        """
        type_ = self.__class__.__name__.lower().replace("_", "-")

        return type_[1:] if type_.startswith("-") else type_


    @property
    def url(self):
        """Vocab definition url.

        """
        url = "{}{}" if self._depth <= 3 else "{}{}.py"

        return url.format(_URL, self.id.replace(".", "/"))


    @property
    def notes(self):
        """Returns set of notes associated with a property definiion.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.replace("_", "-")),
            ("Python Definition", self.url)
        ]


class Vocab(_Node):
    """Wraps the definitions of the CMIP6 vocab.

    """
    def __init__(self):
        """Instance constructor.

        """
        from esdoc_mp.vocabs import cmip6
        super(Vocab, self).__init__(cmip6, 1)

        self.domains = [_Domain(i) for i in cmip6.domains]


class _Domain(_Node):
    """Wraps the definitions of a CMIP6 science domain definition.

    """
    def __init__(self, module):
        """Instance constructor.

        """
        super(_Domain, self).__init__(module, 2)
        self.processes = [_Process(i) for i in module.processes]


class _Process(_Node):
    """Wraps the definitions of a CMIP6 science process definition.

    """
    def __init__(self, module):
        """Instance constructor.

        """
        super(_Process, self).__init__(module, 3)
        self.sub_processes = [_Sub_Process(i) for i in module.sub_processes]


class _Sub_Process(_Node):
    """Wraps the definitions of a CMIP6 science sub-process definition.

    """
    def __init__(self, module):
        """Instance constructor.

        """
        super(_Sub_Process, self).__init__(module, 4)
        self._module = module
        self.details = [_Detail(self, m[0], m[1]) for m in inspect.getmembers(module) if not m[0].startswith("_")]


class _Detail(object):
    """Wraps the definitions of a CMIP6 detail definition.

    """
    def __init__(self, owner, name, func):
        """Instance constructor.

        """
        self.owner = owner
        self.name = name
        self.func = func
        self.obj = func()
        self.properties = [_DetailProperty(self, i.replace("_", "-"), v) for i, v in self.obj.items()]

    def __repr__(self):
        """Instance representation.

        """
        return "{}".format(self.id)


    @property
    def description(self):
        """Node description text.

        """
        return "{}.".format(self.func.__doc__.split(".")[0])


    @property
    def id(self):
        """Node identifier.

        """
        return "{}.{}".format(self.owner.id, self.name)


    @property
    def type(self):
        """Node type.

        """
        return "detail"


    @property
    def notes(self):
        """Returns set of notes associated with a property definiion.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.replace("_", "-"))
        ]



class _DetailProperty(object):
    """Wraps the definitions of a CMIP6 detail property definition.

    """
    def __init__(self, owner, name, obj):
        """Instance constructor.

        """
        self.cardinality = obj['cardinality']
        self.description = obj.get("description", None)
        self.id = "{}.{}".format(owner.id, name)
        self.owner = owner
        self.name = name
        self.obj = obj
        self.type = "detail-property"
        self.type_ = obj['type']

        self.choices = [_EnumChoice(self, c[0], c[1]) for c in obj.get('choices', [])]

    def __repr__(self):
        """Instance representation.

        """
        return "{}".format(self.id)


    @property
    def is_enum(self):
        """Returns flag indicating whether property is an enumeration declaration.

        """
        return self.type_ == 'enum'


    @property
    def notes(self):
        """Returns set of notes associated with a property definiion.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.replace("_", "-")),
            ("Cardinality", self.cardinality),
            ("Type", self.type_)
        ]


class _EnumChoice(object):
    """Wraps the definitions of a CMIP6 enumeration choice definition.

    """
    def __init__(self, owner, value, description):
        """Instance constructor.

        """
        self.owner = owner
        self.name = value
        self.value = value
        self.description = description
        self.id = "{}.{}".format(owner.id, value)


    def __repr__(self):
        """Instance representation.

        """
        return self.id

    @property
    def type(self):
        """Node type.

        """
        return "enum-choice"


    @property
    def notes(self):
        """Returns set of notes associated with a property definiion.

        """
        return [
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-"))
        ]
