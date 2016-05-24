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
_URL = "https://github.com/ES-DOC/esdoc-mp/blob/master/esdoc_mp/specializations/"


class Specialization(object):
    """Wraps the definitions of the CMIP6 specialization.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.description = "{}.".format(schema.__doc__.split(".")[0])

        self.id = "cmip6"
        self.style_type = "specialization"
        self.url = "{}{}".format(_URL, self.id.replace(".", "/"))

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
        self.url = "{}{}".format(_URL, self.id.replace(".", "/"))

        # self.grid = defn.get('grid')
        # self.key_properties = defn.get('key_properties')
        self.processes = [Process(self, i) for i in defn['processes']]


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
    def __init__(self, owner, defn):
        """Instance constructor.

        """
        self.defn = defn

        self.authors = defn.AUTHORS
        self.contact = defn.CONTACT
        self.description = defn.DESCRIPTION
        self.name = "_".join(defn.__name__.split(".")[-1].split("_")[1:])
        self.qc_status = defn.QC_STATUS

        self.id = "{}.{}".format(owner.id, self.name)
        self.style_type = "process"
        self.url = "{}{}".format(_URL, self.id.replace(".", "/"))

        # self.sub_processes = [SubProcess(self, i) for i in module.sub_processes]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-")),
            ("Python Definition", self.url)
        ]