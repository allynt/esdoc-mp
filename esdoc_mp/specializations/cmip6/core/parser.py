# -*- coding: utf-8 -*-

"""
.. module:: parser.py
   :platform: Unix, Windows
   :synopsis: An event style parser over the vocab definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.utils import log
from esdoc_mp.specializations.cmip6.core import Specialization



class SpecializationParser(object):
    """An event driven CMIP6 specializations parser.

    """
    def __init__(self, realm_filter=None, verbose=False):
        """Instance constructor.

        """
        self.realm_filter = realm_filter
        self.verbose = verbose


    def parse(self):
        """Parses the CMIP6 vocabulary raising events as it does so.

        """
        # Instantiate specialization wrapper.
        specialization = Specialization()

        # Raise specialization parse event.
        if self.verbose:
            log("parsing specialization --> {}".format(specialization))
        self.on_specialization_parse(specialization)

        # Set realms.
        realms = specialization.realms
        if self.realm_filter:
            realms = [d for d in realms if self.realm_filter == d.name]

        # Parse realms.
        for realm in realms:
            self._parse_realm(realm)


    def on_specialization_parse(self, specialization):
        """On specialization parse event handler.

        """

        pass


    def on_realm_parse(self, realm):
        """On realm parse event handler.

        """
        pass


    def on_process_parse(self, realm, process):
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


    def _parse_realm(self, realm):
        """Parses a realm.

        """
        # Raise realm parse event.
        if self.verbose:
            log("parsing: {}".format(realm))
        self.on_realm_parse(realm)

        # Parse child processes.
        processes = sorted(realm.processes, key = lambda p: p.name)
        for process in processes:
            self._parse_process(realm, process)


    def _parse_process(self, realm, process):
        """Parses a realm process.

        """
        # Raise process parse event.
        if self.verbose:
            log("parsing: {}".format(process))
        self.on_process_parse(realm, process)

        # Parse child sub-processes.
        sub_processes = sorted(process.sub_processes, key = lambda sp: sp.name)
        for sub_process in sub_processes:
            self._parse_subprocess(realm, process, sub_process)


    def _parse_subprocess(self, realm, process, sub_process):
        """Parses a realm sub process.

        """
        # Raise sub-process parse event.
        if self.verbose:
            log("parsing: {}".format(sub_process))
        self.on_subprocess_parse(process, sub_process)

        return

        # Iterate set of sub-process details.
        for detail in sub_process.details:
            # Raise sub-process detail parse event.
            if self.verbose:
                log("parsing: {}".format(detail))
            self.on_detail_parse(sub_process, detail)

            # Iterate set of detail properties.
            for detail_property in detail.properties:
                # Raise detail-property parse event.
                if self.verbose:
                    log("parsing: {}".format(detail_property))
                self.on_detail_property_parse(detail, detail_property)
