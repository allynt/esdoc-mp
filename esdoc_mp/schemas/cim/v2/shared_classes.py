
# -*- coding: utf-8 -*-

"""
.. module:: shared_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 ontology schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""


def cim_link():
    """Specialisation of online resource for link between CIM documents.

    """
    return {
        "type": "class",
        "base": "shared.online_resource",
        "is_abstract": False,
        "properties": [
			("remote_type", "str", "1.1")
        ],
        "doc_strings": {
			"remote_type": "CIM type of remote record"
        }
    }


def cimtext():
    """Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("content", "str", "1.1"),
			("content_type", "shared.text_code", "1.1")
        ],
        "doc_strings": {
			"content": "Raw content (including markup)",
			"content_type": "Type of content"
        }
    }


def citation():
    """Description of material suitable for citation - in the academic sense, i.e. for a journal bibliography.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("abstract", "str", "0.1"),
			("citation_str", "str", "1.1"),
			("context", "str", "0.1"),
			("doi", "str", "0.1"),
			("short_cite", "str", "0.1"),
			("title", "str", "0.1"),
			("url", "shared.online_resource", "0.1")
        ],
        "doc_strings": {
			"abstract": "Document abstract",
			"citation_str": "How the citation should be referenced in a bibliography",
			"context": "Brief text description of why this resource is being cited",
			"doi": "A digital object identifier",
			"short_cite": "How you would refer to this in text (e.g. Meehl et al (2014)).",
			"title": "Full citation title.",
			"url": "A URL where the artifact can be obtained"
        }
    }


def key_float():
    """Holds a key and a float value.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("key", "str", "1.1"),
			("value", "float", "1.1")
        ],
        "doc_strings": {
			"key": "User defined key",
			"value": "Value associated with a key (real number)"
        }
    }


def number_array():
    """Provides a class for entering an array of numbers.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("values", "str", "1.1")
        ],
        "doc_strings": {
			"values": "A space separated list of numbers"
        }
    }


def online_resource():
    """An approximation of ISO19115 CI_ONLINERESOURCE.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("description", "str", "0.1"),
			("linkage", "str", "1.1"),
			("name", "str", "1.1"),
			("protocol", "str", "0.1")
        ],
        "doc_strings": {
			"description": "Detail of how to access the resource",
			"linkage": "A URL",
			"name": "Name of online resource",
			"protocol": "Protocol to use at the linkage"
        }
    }


def party():
    """Implements minimal material for an ISO19115-1 (2014) compliant party. 
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("address", "str", "0.1"),
			("email", "str", "0.1"),
			("meta", "shared.doc_meta_info", "1.1"),
			("name", "str", "0.1"),
			("organisation", "bool", "0.1"),
			("url", "shared.online_resource", "0.1")
        ],
        "doc_strings": {
			"address": "Institutional address",
			"email": "Email address",
			"meta": "Provides a unique identifier for the party",
			"name": "Name of person or organisation",
			"organisation": "True if an organisation not a person",
			"url": "URL of person or institution"
        }
    }


def pid():
    """A permanent identifier (with a resolution service).

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("id", "str", "1.1"),
			("resolution_service", "shared.online_resource", "1.1")
        ],
        "doc_strings": {
			"id": "The identifier",
			"resolution_service": "The resolution service"
        }
    }


def reference():
    """A citation which is forced to have a context provided.

    """
    return {
        "type": "class",
        "base": "shared.citation",
        "is_abstract": False,
        "properties": [
        ],
        "doc_strings": {
        }
    }


def responsibility():
    """Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty).

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("party", "shared.party", "1.N"),
			("party_references", "shared.doc_reference", "1.N"),
			("role", "shared.role_code", "1.1"),
			("when", "shared.time_period", "0.1")
        ],
        "doc_strings": {
			"party": "Parties delivering responsibility",
			"role": "Role that the party plays or played",
			"when": "Period when role was active, if no longer"
        }
    }


def role_code():
    """Responsibility role codes.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
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
        "type": "class",
        "base": None,
        "is_abstract": True,
        "properties": [
			("long_name", "str", "0.1"),
			("meta", "shared.doc_meta_info", "1.1"),
			("name", "str", "1.1"),
			("references", "shared.citation", "0.N"),
			("responsible_parties", "shared.responsibility", "0.N")
        ],
        "doc_strings": {
			"long_name": "Longer version of activity name",
			"meta": "Metadata describing how this document was created",
			"name": "Short name or abbreviation",
			"references": "Relevant documentation",
			"responsible_parties": "People or organisations responsible for activity"
        }
    }


def text_code():
    """Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
			("plaintext", "Normal plain text")
		]
    }


def vocab_member():
    """A term in an external (to the CIM) controlled vocabulary (CV).

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
			("uri", "str", "0.1"),
			("value", "str", "1.1"),
			("vocab", "shared.citation", "0.1")
        ],
        "doc_strings": {
			"uri": "URI of the term in the controlled vocabulary",
			"value": "Text value of the CV term",
			"vocab": "Type of content"
        }
    }
