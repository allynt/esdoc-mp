# -*- coding: utf-8 -*-

"""
.. module:: shared_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def cim_link():
    """Specialisation of online resource for link between CIM documents.

    """
    return {
        'type': 'class',
        'base': 'shared.online_resource',
        'is_abstract': False,
        'properties': [
            ('remote_type', 'str', '1.1',
                "CIM type of remote record.")
        ]
    }


def cimtext():
    """Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('content',)),
        'properties': [
            ('content', 'str', '1.1',
                "Raw content (including markup)."),
            ('content_type', 'shared.text_code', '1.1',
                "Type of content.")
        ]
    }


def citation():
    """Description of material suitable for citation - in the academic sense, i.e. for a journal bibliography.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('short_cite',)),
        'properties': [
            ('abstract', 'str', '0.1',
                "Document abstract."),
            ('citation_str', 'str', '1.1',
                "How the citation should be referenced in a bibliography."),
            ('context', 'str', '0.1',
                "Brief text description of why this resource is being cited."),
            ('doi', 'str', '0.1',
                "A digital object identifier."),
            ('short_cite', 'str', '0.1',
                "How you would refer to this in text (e.g. Meehl et al (2014))."),
            ('title', 'str', '0.1',
                "Full citation title."),
            ('url', 'shared.online_resource', '0.1',
                "A URL where the artifact can be obtained.")
        ]
    }


def key_float():
    """Holds a key and a float value.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s: %s', ('key', 'value')),
        'properties': [
            ('key', 'str', '1.1',
                "User defined key."),
            ('value', 'float', '1.1',
                "Value associated with a key (real number).")
        ]
    }


def number_array():
    """Provides a class for entering an array of numbers.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('values',)),
        'properties': [
            ('values', 'str', '1.1',
                "A space separated list of numbers.")
        ]
    }


def online_resource():
    """An approximation of ISO19115 CI_ONLINERESOURCE.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1',
                "Detail of how to access the resource."),
            ('linkage', 'str', '1.1',
                "A URL."),
            ('name', 'str', '1.1',
                "Name of online resource."),
            ('protocol', 'str', '0.1',
                "Protocol to use at the linkage.")
        ]
    }


def party():
    """Implements minimal material for an ISO19115-1 (2014) compliant party. 
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('address', 'str', '0.1',
                "Institutional address."),
            ('email', 'str', '0.1',
                "Email address."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Provides a unique identifier for the party."),
            ('name', 'str', '0.1',
                "Name of person or organisation."),
            ('organisation', 'bool', '0.1',
                "True if an organisation not a person."),
            ('url', 'shared.online_resource', '0.1',
                "URL of person or institution.")
        ]
    }


def pid():
    """A permanent identifier (with a resolution service).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('id', 'str', '1.1',
                "The identifier."),
            ('resolution_service', 'shared.online_resource', '1.1',
                "The resolution service.")
        ]
    }


def reference():
    """A citation which is forced to have a context provided.

    """
    return {
        'type': 'class',
        'base': 'shared.citation',
        'is_abstract': False,
        'pstr': ('%s', ('citation_str',)),
        'properties': [
        ]
    }


def responsibility():
    """Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s:%s', ('role', 'party')),
        'properties': [
            ('link_to_party', 'shared.doc_reference', '1.N',
                "Reference to linked document(s)."),
            ('party', 'shared.party', '1.N',
                "Parties delivering responsibility."),
            ('role', 'shared.role_code', '1.1',
                "Role that the party plays or played."),
            ('when', 'shared.time_period', '0.1',
                "Period when role was active, if no longer.")
        ]
    }


def role_code():
    """Responsibility role codes.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Principal Investigator", "None"),
            ("originator", "None"),
            ("author", "None"),
            ("collaborator", "None"),
            ("publisher", "None"),
            ("owner", "None"),
            ("processor", "None"),
            ("distributor", "None"),
            ("sponsor", "None"),
            ("user", "None"),
            ("point of contact", "None"),
            ("resource provider", "None"),
            ("custodian", "None")
        ]
    }


def standalone_document():
    """Raw base class for documents which are created standalone in a workflow.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('long_name', 'str', '0.1',
                "Longer version of activity name."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata describing how this document was created."),
            ('name', 'str', '1.1',
                "Short name or abbreviation."),
            ('references', 'shared.citation', '0.N',
                "Relevant documentation."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "People or organisations responsible for activity.")
        ]
    }


def text_code():
    """Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("plaintext", "Normal plain text")
        ]
    }


def vocab_member():
    """A term in an external (to the CIM) controlled vocabulary (CV).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('value',)),
        'properties': [
            ('uri', 'str', '0.1',
                "URI of the term in the controlled vocabulary."),
            ('value', 'str', '1.1',
                "Text value of the CV term."),
            ('vocab', 'shared.citation', '0.1',
                "Type of content.")
        ]
    }
