# -*- coding: utf-8 -*-

"""
.. module:: misc_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 miscellaneous package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def document_set():
    """Represents a bundled set of documents.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('meta', 'shared.doc_meta_info', '1.1'),
            ('data', 'data.data_object', '0.N'),
            ('ensembles', 'activity.ensemble', '0.N'),
            ('experiment', 'activity.numerical_experiment', '0.1'),
            ('grids', 'grids.grid_spec', '0.N'),
            ('model', 'software.model_component', '0.1'),
            ('platform', 'shared.platform', '0.1'),
            ('simulation', 'activity.simulation_run', '0.1'),
            ('link_to_data', 'shared.doc_reference', '0.N'),
            ('link_to_ensembles', 'shared.doc_reference', '0.N'),
            ('link_to_experiment', 'shared.doc_reference', '0.1'),
            ('link_to_grids', 'shared.doc_reference', '0.N'),
            ('link_to_model', 'shared.doc_reference', '0.1'),
            ('link_to_platform', 'shared.doc_reference', '0.1'),
            ('link_to_simulation', 'shared.doc_reference', '0.1'),
        ],
        'doc_strings': {
            'data': 'Associated input/output data.',
            'ensembles': 'Associated ensemble runs.',
            'experiment': 'Associated numerical experiment.',
            'grids': 'Associated grid-spec.',
            'model': 'Associated model component.',
            'platform': 'Associated simulation execution platform.',
            'simulation': 'Associated simulation run.',
            'link_to_data': 'Reference to set of associated data objects.',
            'link_to_ensembles': 'Reference to set of associated ensembles.',
            'link_to_experiment': 'Reference to the associated experiment.',
            'link_to_grids': 'Reference to the associated grid specs.',
            'link_to_model': 'Reference to the associated model component.',
            'link_to_platform': 'Reference to the associated platform.',
            'link_to_simulation': 'Reference to the associated simulation.'
        },
        'decodings' : [
            ('data', 'child::cim:dataObject'),
            ('ensembles', 'child::cim:ensemble'),
            ('experiment', 'child::cim:numericalExperiment'),
            ('model', 'child::cim:modelComponent'),
            ('grids', 'child::cim:gridSpec'),
            ('platform', 'child::cim:platform'),
            ('simulation', 'child::cim:simulationRun'),
        ]
    }
