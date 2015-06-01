# -*- coding: utf-8 -*-

"""
.. module:: shared_enums.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 shared enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def role_code():
    """Roles that a party may play in delivering a responsibility.

    Definitions sourced from: https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115_and_19115-2_CodeList_Dictionaries#CI_RoleCode

    """
    return {
        'type': 'enum',
        'base': None,
        'is_open': False,
        'members': [
            ('Principal Investigator', None),
            ('originator', None),
            ('author', None),
            ('collaborator', None),
            ('publisher', None),
            ('owner', None),
            ('processor', None),
            ('distributor', None),
            ('sponsor', None),
            ('user', None),
            ('point of contact', None),
            ('resource provider', None),
            ('custodian', None),
        ]
    }


def text_code():
    """Types of text understood by the CIM notebook.

    """
    return {
        'type': 'enum',
        'base': None,
        'is_open': False,
        'members': [
            ('plaintext', 'Normal plain text'),
        ]
    }


