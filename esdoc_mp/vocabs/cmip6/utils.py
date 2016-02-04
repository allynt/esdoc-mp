# Base url for linking back to meta-definitions.
_URL = "https://github.com/ES-DOC/esdoc-mp/tree/master/esdoc_mp/vocabs/cmip6"


class Vocab(object):
    """Wraps the definitions of the CMIP6 vocab.

    """
    def __init__(self, module):
        """Instance constructor.

        """
        self._module = module
        self.domains = [Domain(i) for i in module.domains]

    @property
    def help(self):
        """Vocabulary help text.

        """
        return "{}.".format(self._module.__doc__.split(".")[0])

    @property
    def name(self):
        """Vocabulary canonical name.

        """
        return self._module.__name__.split(".")[-1]

    @property
    def id(self):
        """Vocabulary identifier.

        """
        return ".".join(self._module.__name__.split(".")[-2:])


    @property
    def url(self):
        """Vocab definition url.

        """
        return _URL


class Domain(object):
    """Wraps the definitions of a CMIP6 science domain definition.

    """
    def __init__(self, module):
        """Instance constructor.

        """
        self._module = module
        self.processes = [Process(i) for i in module.processes]
        self.fpath = "/Users/macg/dev/esdoc/repos/esdoc-cv/cmip6/mindmaps/ocean-1.mm"

    @property
    def help(self):
        """Domain help text.

        """
        return "{}.".format(self._module.__doc__.split(".")[0])

    @property
    def name(self):
        """Domain canonical name.

        """
        return self._module.__name__.split(".")[-1].replace("_", "-")

    @property
    def id(self):
        """Domain identifier.

        """
        return ".".join(self._module.__name__.split(".")[-2:])


class Process(object):
    """Wraps the definitions of a CMIP6 science process definition.

    """
    def __init__(self, module):
        """Instance constructor.

        """
        self._module = module
        self.sub_processes = [SubProcess(i) for i in module.sub_processes]

    @property
    def help(self):
        """Process help text.

        """
        return "{}.".format(self._module.__doc__.split(".")[0])

    @property
    def name(self):
        """Process canonical name.

        """
        return self._module.__name__.split(".")[-1].replace("_", "-")

    @property
    def id(self):
        """Process identifier.

        """
        return ".".join(self._module.__name__.split(".")[-3:])

    @property
    def notes(self):
        """Process notes.

        """
        return "{}\n\n{}".format(self.id, self.help)

    @property
    def url(self):
        """Process definition url.

        """
        return "{}/{}.py".format(_URL, self._module.__name__.replace(".", "/"))


class SubProcess(object):
    """Wraps the definitions of a CMIP6 science sub-process definition.

    """
    def __init__(self, module):
        """Instance constructor.

        """
        self._module = module

    @property
    def details(self):
        """Associated process details.

        """
        return [ProcessDetail(self._module, i) for i in self._defn['values']['details']]

    @property
    def id(self):
        """Sub-process identifier.

        """
        return self._defn['values']['id']

    @property
    def name(self):
        """Sub-process canonical name.

        """
        return self._module.__name__.split(".")[-1].replace("_", "-")

    @property
    def notes(self):
        """Sub-process notes.

        """
        return "{}\n\n{}".format(self.id, self.context)

    @property
    def url(self):
        """Sub-process definition url.

        """
        return "{}/{}.py".format(_URL, self._module.__name__.replace(".", "/"))


class ProcessDetail(object):
    """Wraps the definitions of a CMIP6 process detail definition.

    """
    def __init__(self, module, module_var):
        """Instance constructor.

        """
        self._module = module
        self._module_var = module_var

    @property
    def context(self):
        return self._defn['values']['context']

    @property
    def id(self):
        return self._defn['values']['id']

    @property
    def name(self):
        return self._defn['values']['name']

    @property
    def notes(self):
        return "{}\n\n{}".format(self.id, self.context)

    @property
    def url(self):
        return "{}/{}.py".format(_URL, self._module.__name__.replace(".", "/"))

