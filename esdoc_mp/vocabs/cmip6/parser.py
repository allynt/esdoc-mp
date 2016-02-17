# -*- coding: utf-8 -*-

"""
.. module:: parser.py
   :platform: Unix, Windows
   :synopsis: An event style parser over the vocab definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.utils import log
from esdoc_mp.vocabs.cmip6.core import Vocab



class VocabParser(object):
    """An event driven CMIP6 vocab parser.

    """
    def __init__(self, domain_filter=None):
        """Instance constructor.

        """
        self.domain_filter = domain_filter


    def parse(self):
        """Parses the CMIP6 vocabulary raising events as it does so.

        """
        # Instantiate vocab wrapper.
        vocab = Vocab()

        # Raise vocab parse event.
        log("parsing vocabulary --> {}".format(vocab))
        self.on_vocab_parse(vocab)

        # Parse child domains.
        domains = [d for d in vocab.domains \
                   if self.domain_filter and self.domain_filter == d.name]
        for domain in domains:
            self._parse_domain(domain)


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


    def _parse_domain(self, domain):
        """Parses a domain.

        """
        # Raise domain parse event.
        log("parsing: {}".format(domain))
        self.on_domain_parse(domain)

        # Parse child processes.
        processes = sorted(domain.processes, key = lambda p: p.name)
        for process in processes:
            self._parse_process(domain, process)


    def _parse_process(self, domain, process):
        """Parses a domain process.

        """
        # Raise process parse event.
        log("parsing: {}".format(process))
        self.on_process_parse(domain, process)

        # Parse child sub-processes.
        sub_processes = sorted(process.sub_processes, key = lambda sp: sp.name)
        for sub_process in sub_processes:
            self._parse_subprocess(domain, process, sub_process)


    def _parse_subprocess(self, domain, process, sub_process):
        """Parses a domain sub process.

        """
        # Raise sub-process parse event.
        log("parsing: {}".format(sub_process))
        self.on_subprocess_parse(process, sub_process)

        # Iterate set of sub-process details.
        for detail in sub_process.details:
            # Raise sub-process detail parse event.
            log("parsing: {}".format(detail))
            self.on_detail_parse(sub_process, detail)

            # Iterate set of detail properties.
            for detail_property in detail.properties:
                # Raise detail-property parse event.
                log("parsing: {}".format(detail_property))
                self.on_detail_property_parse(detail, detail_property)
