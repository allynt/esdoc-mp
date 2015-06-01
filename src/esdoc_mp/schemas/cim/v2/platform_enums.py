# -*- coding: utf-8 -*-

"""
.. module:: platform_enums.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 platform package enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def storage_systems():
    """Controlled vocabulary for storage  types (including filesystems).

    """
    return {
        'type':'enum',
        'base':None,
        'is_open':False,
        'members':[
            ('Lustre',None),
            ('GPFS',None),
            ('isilon',None),
            ('NFS',None),
            ('Panasas',None),
            ('Other Disk',None),
            ('Tape - MARS',None),
            ('Tape - MASS',None),
            ('Tape - Castor',None),
            ('Tape - Other',None),
            ('Unknown',None),
            ],
        }


def volume_units():
    """Appropriate storage volume units.

    """
    return {
        'type':'enum',
        'base':None,
        'is_open':False,
        'members':[
            ('GB', 'Gigabytes (1000^3)'),
            ('TB', 'Terabytes (1000^4)'),
            ('PB', 'Petabytes (1000^5)'),
            ('EB', 'Exabytes (1000^6)'),
            ('TiB', 'Tebibytes (1024^4)'),
            ('PiB', 'Pebibytes (1024^5)'),
            ('EiB', 'Exbibytes (1024^6)'),
        ],
    }


