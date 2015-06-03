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
            ('abstract', 'str', '0.1'),
            ('citation_str', 'str', '1.1'),
            ('description', 'str', '0.1'),
            ('doi', 'str', '0.1'),
            ('title', 'str', '0.1'),
            ('url', 'shared.online_resource', '0.1')
        ],
        'doc_strings': {
            'abstract': 'Document abstract',
            'citation_str': 'How the citation should be referenced',
            'description': 'Brief textural description of document',
            'doi': 'A digital object identifer',
            'title': 'Document title',
            'url': 'A URL where the artifact can be obtained'
        }
    }


def online_resource():
    """An approximation of ISO19115 CI_ONLINERESOURCE.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties':  [
            ('description', 'str', '0.1'),
            ('linkage', 'str', '1.1'),
            ('name', 'str', '1.1'),
            ('protocol', 'str', '0.1')
        ],
        'doc_strings': {
            'description': 'Detail of how to access the resource',
            'linkage': 'A URL',
            'name': 'Name of online resource',
            'protocol': 'Protocol to use at the linkage'
        }
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
            ('role', 'shared.role_code', '1.1'),
            ('party', 'linked_to(shared.party)', '1.N'),
            ('when', 'time.time_period', '0.1')
        ],
        'doc_strings': {
            'role': 'Role that the party plays or played',
            'party': 'Parties delivering responsibility',
            'when': 'Period when role was active, if no longer'
        }
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
            ('address', 'str', '0.1'),
            ('email', 'str', '0.1'),
            ('meta', 'shared.meta', '1.1'),
            ('name', 'str', '0.1'),
            ('organisation', 'bool', '0.1'),
            ('url', 'shared.online_resource', '0.1')
        ],
        'doc_strings': {
            'meta': 'Provides a unique identifier for the party',
            'name': 'Name of person or organisation',
            'organisation': 'True if an organisation not a person'
        }
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
            ('values', 'str', '1.1')
        ],
        'doc_strings': {
            'values': 'A space separated list of numbers'
        }
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
            ('uri', 'str', '0.1'),
            ('value', 'str', '1.1'),
            ('vocab', 'shared.citation', '0.1'),
        ],
        'doc_strings': {
            'uri': 'URI of the term in the controlled vocabulary',
            'value': 'Text value of the CV term',
            'vocab': 'Type of content'
        }
    }
