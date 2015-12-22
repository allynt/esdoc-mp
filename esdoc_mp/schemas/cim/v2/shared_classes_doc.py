# -*- coding: utf-8 -*-

"""
.. module:: shared_classes_doc.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def doc_meta_info():
    """Encapsulates document meta information.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('author', 'shared.party', '0.1',
                "Associated document author."),
            ('create_date', 'datetime', '1.1',
                "Date upon which the instance was created."),
            ('drs_keys', 'str', '0.N',
                "DRS related keys to support correlation of documents with datasets."),
            ('drs_path', 'str', '0.1',
                "DRS related path to support documents with datasets."),
            ('external_ids', 'str', '0.N',
                "Set of identifiers used to reference the document by external parties."),
            ('id', 'uuid', '1.1',
                "Universal document identifier."),
            ('institute', 'str', '0.1',
                "Name of institute with which instance is associated with."),
            ('language', 'str', '1.1',
                "Language with which instance is associated with."),
            ('project', 'str', '1.1',
                "Name of project with which instance is associated with."),
            ('reviews', 'shared.doc_quality_review', '0.N',
                "Set of quailty related reviews."),
            ('sort_key', 'str', '0.1',
                "Document sort key."),
            ('source', 'str', '1.1',
                "Name of application that created the instance."),
            ('source_key', 'str', '0.1',
                "Key of application that created the instance."),
            ('type', 'str', '1.1',
                "Document ontology type."),
            ('type_display_name', 'str', '0.1',
                "Document type display name."),
            ('type_sort_key', 'str', '0.1',
                "Document type sort key."),
            ('update_date', 'datetime', '1.1',
                "Date upon which the instance was last updated."),
            ('version', 'int', '1.1',
                "Document version identifier.")
        ]
    }


def doc_quality_review():
    """A review of a documents quality.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('completeness', 'str', '1.1',
                "Assessment of completeness of this document (assessment made by author)."),
            ('date', 'str', '1.1',
                "Date upon which review was made."),
            ('quality', 'str', '1.1',
                "Assessment of quality of this document."),
            ('reviewer', 'shared.party', '1.1',
                "Individual who made the metadata quality assessment.")
        ]
    }


def doc_reference():
    """A reference to another cim entity.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1',
                "A description of the element being referenced, in the context of the current class."),
            ('id', 'uuid', '0.1',
                "The ID of the element being referenced."),
            ('name', 'str', '0.1',
                "The name of the element being referenced."),
            ('type', 'str', '0.1',
                "The type of the element being referenced."),
            ('url', 'str', '0.1',
                "A URL associated witht he document reference."),
            ('version', 'int', '0.1',
                "The version of the element being referenced.")
        ]
    }
