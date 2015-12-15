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
            ('data_references', 'shared.doc_reference', '0.N'),
            ('ensembles', 'activity.ensemble', '0.N'),
            ('ensembles_references', 'shared.doc_reference', '0.N'),
            ('experiment', 'activity.numerical_experiment', '0.1'),
            ('experiment_reference', 'shared.doc_reference', '0.1'),
            ('grids', 'grids.grid_spec', '0.N'),
            ('grids_references', 'shared.doc_reference', '0.N'),
            ('model', 'software.model_component', '0.1'),
            ('model_reference', 'shared.doc_reference', '0.1'),
            ('platform', 'shared.platform', '0.1'),
            ('platform_reference', 'shared.doc_reference', '0.1'),
            ('simulation', 'activity.simulation_run', '0.1'),
            ('simulation_reference', 'shared.doc_reference', '0.1'),
        ],
        'doc_strings': {
            'data': 'Associated input/output data.',
            'data_references': 'Reference to set of associated data objects.',
            'ensembles': 'Associated ensemble runs.',
            'ensembles_references': 'Reference to set of associated ensembles.',
            'experiment': 'Associated numerical experiment.',
            'experiment_reference': 'Reference to the associated experiment.',
            'grids': 'Associated grid-spec.',
            'grids_references': 'Reference to the associated grid specs.',
            'model': 'Associated model component.',
            'model_reference': 'Reference to the associated model component.',
            'platform': 'Associated simulation execution platform.',
            'platform_reference': 'Reference to the associated platform.',
            'simulation': 'Associated simulation run.',
            'simulation_reference': 'Reference to the associated simulation.'
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
