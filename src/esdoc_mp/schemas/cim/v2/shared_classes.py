# -*- coding: utf-8 -*-

"""
.. module:: shared_classes.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 shared class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def citation():
    """A document, book, or academic paper..

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('abstract', 'str', '0.1', 'Document abstract'),
            ('citation_str', 'str', '1.1', 'How the citation should be referenced'),
            ('description', 'str', '0.1', 'Brief textural description of document'),
            ('doi', 'str', '0.1', 'A digital object identifer'),
            ('title', 'str', '0.1', 'Document title'),
            ('url', 'shared.online_resource', '0.1', 'A URL where the artifact can be obtained'),
        ],
    }


def online_resource():
    """An approximation of ISO19115 CI_ONLINERESOURCE.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties':  [
            ('description', 'str', '0.1', 'Detail of how to access the resource'),
            ('linkage', 'str', '1.1', 'A URL'),
            ('name', 'str', '1.1', 'Name of online resource'),
            ('protocol', 'str', '0.1', 'Protocol to use at the linkage'),
        ],
    }


def responsibility():
    """Identifies a person or organisation and their role in doing something.

    NOTE: Implements the ISO19115-1 (2014) CI_Responsibility (which replaces responsibleParty).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr':  ('%s:%s', ('role', 'party',)),
        'properties':  [
            ('role', 'shared.role_code', '1.1', 'Role that the party plays or played'),
            ('party', 'linked_to(shared.party)', '1.N', 'Parties delivering responsibility'),
            ('when', 'time.time_period', '0.1', 'Period when role was active, if no longer'),
        ]
    }


def party():
    """A person or organisation.

    NOTE: Implements minimal material for an ISO19115-1 (2014) compliant party.
    For our purposes this is a much better animal than the previous responsibleParty
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties':  [
            ('address', 'str', '0.1', None),
            ('email', 'str', '0.1', None),
            ('meta', 'shared.meta', '1.1', 'Provides a unique identifier for the party'),
            ('name', 'str', '0.1', 'Name of person or organisation'),
            ('organisation', 'bool', '0.1', 'True if an organisation not a person'),
            ('url', 'shared.online_resource', '0.1', None),
        ],
    }


def number_array():
    """An array of numbers as a space separated list.

    """
    # NOT_CURRENTLY_USED ???
    # Significantly kludgey as well, since it's kind of a GUI
    # concept masqueradingi in the domain model ...
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s',('values',)),
        'properties': [
            ('values', 'str', '1.1', 'A space separated list of numbers'),
        ]
    }


def vocab_member():
    """A term in an external (to the CIM) controlled vocabulary (CV).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s',('value',)),
        'properties': [
            ('uri', 'str', '0.1', 'URI of the term in the controlled vocabulary'),
            ('value', 'str', '1.1', 'Text value of the CV term'),
            ('vocab', 'shared.citation', '0.1', 'Type of content'),
        ],
    }


