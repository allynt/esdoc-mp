# -*- coding: utf-8 -*-

"""
.. module:: shared_classes_doc.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 document related shared class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def cim_link():
     """Specialisation of online resource for link between documents.

     """
     return {
        'type': 'class',
        'base': 'shared.online_resource',
        'is_abstract': False,
        'properties':  [
            ('remote_type', 'str', '1.1', 'Type of remote record'),
        ],
         'constraints':  [
             ('description', 'value', 'Link to CIM document, accessible at the URL')
         ]
    }


def cim_text():
    """A text class which supports plaintext, html, ...etc.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s',('content',)),
        'properties': [
            ('content', 'str', '1.1', 'Raw content (including markup)'),
            ('content_type', 'shared.textCode', '1.1', 'Type of content')
        ]
    }


def meta():
    """Metadata for all documents.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'doc': 'Document metadata',
        'properties': [
            ('author', 'linked_to(shared.party)', '1.1', 'The document author'),
            ('completeness', 'str', '0.1', 'Assessment of completeness of this document'),
            ('create_date', 'datetime', '1.1', 'Date upon which the instance was created'),
            ('quality', 'str', '0.1', 'Assessment of quality of this document'),
            ('uid', 'uuid', '1.1', 'Universal document identifier.'),
            ('update_date', 'datetime', '1.1', 'Date upon which the instance was last updated'),
            ('version', 'int', '1.1', 'Document version')
        ],
        'notes_for_review': [
            ('Is completeness property relevant'),
            ('Is quality property relevant')
        ]
    }


