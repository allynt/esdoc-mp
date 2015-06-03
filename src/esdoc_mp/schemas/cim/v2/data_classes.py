# -*- coding: utf-8 -*-

"""
.. module:: data_classes.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 data class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def dataset():
    """Discovery level metadata for a dataset.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('dataset_author', 'linked_to(shared.party)', '0.N'),
            ('availability', 'shared.onlineResource', '0.N'),
            ('description', 'str', '0.1'),
            ('meta', 'shared.meta', '1.1'),
            ('name', 'str', '1.1'),
            ('produced_by', 'linked_to(activity.simulation)', '0.1'),
            ('references', 'shared.citation', '0.N'),
            ('related_to_dataset', 'linked_to(data.dataset)', '0.N')
        ],
        'doc_strings': {
            'dataset_author': 'Creator of the dataset',
            'availability': 'Where the data is located, and how it is accessed',
            'description': 'Textural description of dataset',
            'meta': 'Metadata describing the creation of this dataset description document.',
            'name': 'Name of dataset',
            'produced_by': 'Makes a link back to originating activity',
            'references': 'Relevant reference document',
            'related_to_dataset': 'Related dataset'
        }
    }
