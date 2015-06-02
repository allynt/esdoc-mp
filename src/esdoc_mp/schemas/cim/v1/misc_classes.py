# -*- coding: utf-8 -*-

"""
.. module:: misc_classes.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
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
            ('meta', 'shared.doc_meta_info', '1.1', None),
            ('data', 'data.data_object', '0.N', 'Associated input/output data.'),
            ('data_references', 'shared.doc_reference', '0.N', 'Reference to set of associated data objects.'),
            ('ensembles', 'activity.ensemble', '0.N', 'Associated ensemble runs.'),
            ('ensembles_references', 'shared.doc_reference', '0.N', 'Reference to set of associated ensembles.'),
            ('experiment', 'activity.numerical_experiment', '0.1', 'Associated numerical experiment.'),
            ('experiment_reference', 'shared.doc_reference', '0.1', 'Reference to the associated experiment.'),
            ('grids', 'grids.grid_spec', '0.N', 'Associated grid-spec.'),
            ('grids_references', 'shared.doc_reference', '0.N', 'Reference to the associated grid specs.'),
            ('model', 'software.model_component', '0.1', 'Associated model component.'),
            ('model_reference', 'shared.doc_reference', '0.1', 'Reference to the associated model component.'),
            ('platform', 'shared.platform', '0.1', 'Associated simulation execution platform.'),
            ('platform_reference', 'shared.doc_reference', '0.1', 'Reference to the associated platform.'),
            ('simulation', 'activity.simulation_run', '0.1', 'Associated simulation run.'),
            ('simulation_reference', 'shared.doc_reference', '0.1', 'Reference to the associated simulation.'),
        ],
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
