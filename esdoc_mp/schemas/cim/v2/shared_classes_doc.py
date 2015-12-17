
# -*- coding: utf-8 -*-

"""
.. module:: shared_classes_doc.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 ontology schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""


def doc_meta_info():
    """Encapsulates document meta information.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("author", "shared.party", "0.1"),
            ("author_reference", "shared.doc_reference", "0.1"),
            ("create_date", "datetime", "1.1"),
            ("drs_keys", "str", "0.N"),
            ("drs_path", "str", "0.1"),
            ("external_ids", "str", "0.N"),
            ("id", "uuid", "1.1"),
            ("institute", "str", "0.1"),
            ("language", "str", "1.1"),
            ("project", "str", "1.1"),
            ("sort_key", "str", "0.1"),
            ("source", "str", "1.1"),
            ("source_key", "str", "0.1"),
            ("type", "str", "1.1"),
            ("type_display_name", "str", "0.1"),
            ("type_sort_key", "str", "0.1"),
            ("update_date", "datetime", "1.1"),
            ("version", "int", "1.1")
        ],
        "doc_strings": {
            "author": "Associated document author.",
            "author_reference": "Reference to the associated document author.",
            "create_date": "Date upon which the instance was created.",
            "drs_keys": "DRS related keys to support correlation of documents with datasets.",
            "drs_path": "DRS related path to support documents with datasets.",
            "external_ids": "Set of identifiers used to reference the document by external parties.",
            "id": "Universal document identifier.",
            "institute": "Name of institute with which instance is associated with.",
            "language": "Language with which instance is associated with.",
            "project": "Name of project with which instance is associated with.",
            "sort_key": "Document sort key.",
            "source": "Name of application that created the instance.",
            "source_key": "Key of application that created the instance.",
            "type": "Document ontology type.",
            "type_display_name": "Document type display name.",
            "type_sort_key": "Document type sort key.",
            "update_date": "Date upon which the instance was last updated.",
            "version": "Document version identifier."
        }
    }


def doc_reference():
    """A reference to another cim entity.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("description", "str", "0.1"),
            ("id", "uuid", "0.1"),
            ("name", "str", "0.1"),
            ("type", "str", "0.1"),
            ("url", "str", "0.1"),
            ("version", "int", "0.1")
        ],
        "doc_strings": {
            "description": "A description of the element being referenced, in the context of the current class.",
            "id": "The ID of the element being referenced.",
            "name": "The name of the element being referenced.",
            "type": "The type of the element being referenced.",
            "url": "A URL associated witht he document reference.",
            "version": "The version of the element being referenced."
        }
    }
