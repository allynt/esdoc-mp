# -*- coding: utf-8 -*-

"""
.. module:: model.py
   :platform: Unix, Windows
   :synopsis: A repesentation of CMIP6 specializations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect

from esdoc_mp.specializations.cmip6 import schema



# Base url for linking back to meta-definitions.
_URL = "https://github.com/ES-DOC/esdoc-mp/blob/master/esdoc_mp/specializations/cmip6/schema/"


class Specialization(object):
    """Wraps the definitions of the CMIP6 specialization.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.description = "{}.".format(schema.__doc__.split(".")[0])

        self.id = "cmip6"
        self.style_type = "specialization"
        self.url = _URL

        self.realms = [Realm(self, i) for i in schema.REALMS]


class Realm(object):
    """Wraps the definitions of a CMIP6 science realm definition.

    """
    def __init__(self, owner, defn):
        """Instance constructor.

        """
        self.defn = defn
        self.name = defn['main'].__name__.split(".")[-1]
        self.description = "{} realm.".format(self.name)

        self.id = "{}.{}".format(owner.id, self.name)
        self.style_type = "realm"
        self.url = "{}{}.py".format(_URL, self.name)

        # self.grid = defn.get('grid')
        # self.key_properties = defn.get('key_properties')
        self.processes = [Process(self, i) for i in defn['processes']]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id),
            ("Python Definition", self.url)
        ]


class Process(object):
    """Wraps the definitions of a CMIP6 science process definition.

    """
    def __init__(self, owner, defn):
        """Instance constructor.

        """
        self.defn = defn

        self.authors = defn.AUTHORS
        self.contact = defn.CONTACT
        self.description = defn.DESCRIPTION
        self.full_name = defn.__name__.split(".")[-1]
        self.name = "_".join(defn.__name__.split(".")[-1].split("_")[1:])
        self.qc_status = defn.QC_STATUS

        self.id = "{}.{}".format(owner.id, self.name)
        self.style_type = "process"
        self.url = "{}{}.py".format(_URL, self.full_name)

        try:
            defn.SUB_PROCESSES
        except AttributeError:
            self.sub_processes = []
        else:
            self.sub_processes = [SubProcess(self, i, j) for i, j in defn.SUB_PROCESSES.items()]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id),
            ("Python Definition", self.url)
        ]


class SubProcess(object):
    """Wraps the definitions of a CMIP6 science sub-process definition.

    """
    def __init__(self, owner, name, defn):
        """Instance constructor.

        """
        self.defn = defn
        self.name = name
        self.description = defn.get('description', name)

        self.id = "{}.{}".format(owner.id, name)
        self.style_type = "sub-process"
        self.url = owner.url

        for detail_ref in defn.get('details', []):
            print self.id, detail_ref, detail_ref in owner.defn.SUB_PROCESS_DETAILS

            # spd_defn = owner.defn.SUB_PROCESS_DETAILS[detail_ref]

        # self.details = [Detail(self, m[1], m[0])
        #                 for m in inspect.getmembers(module)
        #                 if inspect.isfunction(m[1]) and not m[0].startswith("_")]

    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id),
            ("Python Definition", self.url)
        ]