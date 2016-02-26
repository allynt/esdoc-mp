# -*- coding: utf-8 -*-

"""
.. module:: science_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def algorithm():
    """Used to hold information associated with an algorithm which implements some key
    part of a process. In most cases this is quite a high level concept and isn't intended
    to describe the gory detail of how the code implements the algorithm rather the key
    scientific aspects of the algorithm. In particular, it provides a method
    of grouping variables which take part in an algorithm within a process.

    """
    return {
        'type': 'class',
        'base': 'science.science_context',
        'is_abstract': False,
        'properties': [
            ('diagnostic_variables', 'data.variable_collection', '0.1',
                "Diagnostic variables associated with this algorithm."),
            ('forced_variables', 'data.variable_collection', '0.1',
                "Variables held constant within algorithm."),
            ('implementation_overview', 'str', '1.1',
                "Overview of the algorithm implementation."),
            ('prognostic_variables', 'data.variable_collection', '0.1',
                "Prognostic variables associated with this algorithm."),
            ('references', 'shared.reference', '0.N',
                "Relevant references.")
        ]
    }


def conservation_properties():
    """Describes how prognostic variables are conserved.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('corrected_conserved_prognostic_variables', 'data.variable_collection', '0.1',
                "Set of variables which are conserved by *more* than the numerical scheme alone."),
            ('correction_methodology', 'str', '0.1',
                "Description of method by which correction was achieved."),
            ('flux_correction_was_used', 'bool', '1.1',
                "Flag to indicate if correction involved flux correction.")
        ]
    }


def detail():
    """Provides detail of specific properties, there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality is assigned to that
    for possible responses, or (2) Detail is used to provide a collection for a set of
    properties which are defined in the sub-class. However, those properties must have a type
    which is selected from the classmap (that is, standard 'non-es-doc' types).

    """
    return {
        'type': 'class',
        'base': 'science.science_context',
        'is_abstract': False,
        'properties': [
            ('content', 'str', '0.1',
                "Free text description of process detail (if required)."),
            ('detail_selection', 'str', '0.N',
                "List of choices from the vocabulary of possible detailed options."),
            ('from_vocab', 'str', '0.1',
                "Name of an enumeration vocabulary of possible detail options."),
            ('select', 'str', '0.1',
                "Name of property to be selected from vocab."),
            ('with_cardinality', 'science.selection_cardinality', '0.1',
                "Required cardinality of selection from vocabulary.")
        ]
    }


def extent():
    """Key scientific characteristics of the grid use to simulate a specific domain.
    Note that the extent does not itself describe a grid, so, for example, a polar
    stereographic grid may have an extent of northern boundary 90N, southern boundary
    45N, but the fact that it is PS comes from the grid_type.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('region_known_as',)),
        'properties': [
            ('bottom_vertical_level', 'float', '0.1',
                "Bottom vertical level centre (e.g. level near land surface or level ocean floor)."),
            ('eastern_boundary', 'float', '0.1',
                "If not global, eastern boundary in degrees of longitude."),
            ('is_global', 'bool', '1.1',
                "True if horizontal coverage is global."),
            ('northern_boundary', 'float', '0.1',
                "If not global, northern boundary in degrees of latitude."),
            ('region_known_as', 'str', '0.N',
                "Identifier or identifiers for the region covered by the extent."),
            ('southern_boundary', 'float', '0.1',
                "If not global, southern boundary in degrees of latitude."),
            ('top_vertical_level', 'float', '0.1',
                "Top vertical level centre (e.g. level at TOA or level near ocean surface)."),
            ('western_boundary', 'float', '0.1',
                "If not global, western boundary in degrees of longitude."),
            ('z_units', 'str', '1.1',
                "Units of vertical measure (e.g. m, Pa, sigma_level.")
        ]
    }


def grid():
    """This describes the numerical grid used for the calculations.
    It is not necessarily the grid upon which the data is output.
    It is NOT the resolution, which is a property of a specific domain.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('additional_details', 'science.detail', '0.N',
                "Additional grid properties."),
            ('grid_extent', 'science.extent', '0.1',
                "Key geographic characteristics of the grid use to simulate a specific domain."),
            ('horizontal_grid_layout', 'str', '0.1',
                "Type of horizontal grid-layout (e.g. Arakawa C-Grid."),
            ('horizontal_grid_type', 'str', '0.1',
                "Description of basic horizontal grid (e.g. 'cubed-sphere')."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata about how the model description was constructed."),
            ('name', 'str', '1.1',
                "This is a string usually used by the modelling group to describe the grid.(e.g. the ENDGAME/New Dynamics dynamical cores have their own grids describing variable layouts."),
            ('vertical_grid_layout', 'str', '0.1',
                "Type of vertical grid-layout (e.g. Charney-Phillips."),
            ('vertical_grid_type', 'str', '0.1',
                "Description of basic vertical grid (e.g. 'atmosphere_hybrid_height_coordinate').")
        ]
    }


def key_properties():
    """High level list of key properties. It can be specialised in
    extension packages using the detail extensions.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('additional_detail', 'science.detail', '0.N',
                "Additional property details."),
            ('extra_conservation_properties', 'science.conservation_properties', '0.1',
                "Details of methodology needed to conserve variables between processes."),
            ('grid', 'linked_to(science.grid)', '1.1',
                "The grid used to layout the variables (e.g. the Global ENDGAME-grid)."),
            ('resolution', 'science.resolution', '1.1',
                "The resolution of the grid (e.g. N512L180)."),
            ('time_step', 'float', '1.1',
                "Timestep (in seconds) of overall component."),
            ('tuning_applied', 'science.tuning', '0.1',
                "Describe any tuning used to optimise the parameters in this domain.")
        ]
    }


def model():
    """A model component: can be executed standalone, and has as scientific
    description available via a link to a science.domain document. (A configured model can
     be understood in terms of a simulation, a model, and a configuration.).

    """
    return {
        'type': 'class',
        'base': 'software.component_base',
        'is_abstract': False,
        'properties': [
            ('category', 'science.model_types', '1.1',
                "Generic type for this model."),
            ('coupled_components', 'linked_to(science.model)', '0.N',
                "Software components which are linked together using a coupler to deliver this model."),
            ('coupler', 'software.coupling_framework', '0.1',
                "Overarching coupling framework for model."),
            ('id', 'str', '0.1',
                "Vocabulary identifier, where this model description was constructed via a controlled vocabulary."),
            ('internal_software_components', 'software.software_component', '0.N',
                "Software modules which together provide the functionality for this model."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata about how the model description was constructed."),
            ('model_default_properties', 'science.key_properties', '0.1',
                "Model default key properties (may be over-ridden in domain properties)."),
            ('simulates', 'linked_to(science.scientific_domain)', '0.N',
                "The scientific domains which this model simulates.")
        ]
    }


def process():
    """Provides structure for description of a process simulated within a particular
    area (or domain/realm/component) of a model. This will often be subclassed
    within a specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with project requirements
    for information.

    """
    return {
        'type': 'class',
        'base': 'science.science_context',
        'is_abstract': False,
        'properties': [
            ('algorithms', 'science.algorithm', '0.N',
                "Descriptions of algorithms and their properties used in the process."),
            ('implementation_overview', 'str', '1.1',
                "General overview description of the implementation of this process."),
            ('keywords', 'str', '0.1',
                "keywords to help re-use and discovery of this information."),
            ('properties', 'science.detail', '0.N',
                "Sets of properties for this process."),
            ('references', 'shared.reference', '0.N',
                "Any relevant references describing this process and/or it's implementation."),
            ('sub_processes', 'science.sub_process', '0.N',
                "Discrete portion of a process with common process details.")
        ]
    }


def resolution():
    """Describes the computational spatial resolution of a component or process.
    Not intended to replace or replicate the output grid description.
    When it appears as part of a process description, provide only properties that differ from parent domain.
    Note that this is supposed to capture gross features of the grid, we expect many grids will have
    different variable layouts, those should be described in the grid description, and the exact resolution
    is not required. Note that many properties are not appropriate for adaptive grids.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('equivalent_resolution_km', 'float', '0.1',
                "Resolution in km of 'typical grid cell' (at the equator, for gross comparisons of resolution), eg. 50."),
            ('is_adaptive_grid', 'bool', '0.1',
                "Default is False. Set true if grid resolution changes during execution."),
            ('name', 'str', '1.1',
                "This is a string usually used by the modelling group to describe the resolution of this grid,  e.g. N512L180 or T512L70 etc."),
            ('number_of_levels', 'int', '0.1',
                "Number of vertical levels resolved."),
            ('number_of_xy_gridpoints', 'int', '0.1',
                "Total number of horizontal points on computational grids."),
            ('typical_x_degrees', 'float', '0.1',
                "Horizontal X resolution in degrees of grid cells, if applicable eg. 3.75."),
            ('typical_y_degrees', 'float', '0.1',
                "Horizontal Y resolution in degrees of grid cells, if applicable eg. 2.5.")
        ]
    }


def science_context():
    """This is the base class for the science mixins, that is the classes which
    we expect to be specialised and extended by project specific vocabularies.
    It is expected that values of these will be provided within vocabulary
    definitions.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('context', 'str', '1.1',
                "Scientific context for which this description is provided."),
            ('id', 'str', '1.1',
                "Identifier for this collection of properties."),
            ('name', 'str', '1.1',
                "The name of this process/algorithm/sub-process/detail.")
        ]
    }


def scientific_domain():
    """Scientific area of a numerical model - usually a sub-model or component.
    Can also be known as a realm.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('differing_key_properties', 'science.key_properties', '0.1',
                "Key properties for the domain which differ from model defaults (grid, timestep etc)."),
            ('id', 'str', '0.1',
                "Vocabulary identifier, where this domain description was constructed via a  controlled vocabulary."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata describing the construction of this domain description."),
            ('name', 'str', '1.1',
                "Name of the scientific domain (e.g. ocean)."),
            ('overview', 'str', '0.1',
                "Free text overview description of key properties of domain."),
            ('realm', 'str', '0.1',
                "Canonical name for the domain of this scientific area."),
            ('references', 'shared.reference', '0.N',
                "Any relevant references describing the implementation of this domain in a relevant model."),
            ('simulates', 'science.process', '1.N',
                "Processes simulated within the domain.")
        ]
    }


def selection_cardinality():
    """Provides the possible cardinalities for selecting from a controlled vocabulary.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("0.1", "Zero or one selections are permitted"),
            ("0.N", "Zero or many selections are permitted"),
            ("1.1", "One and only one selection is required"),
            ("1.N", "At least one, and possibly many, selections are required")
        ]
    }


def sub_process():
    """Provides structure for description of part of process simulated within a particular
    area (or domain/realm/component) of a model. Typically this will be a part of process
    which shares common properties. It will normally be sub classed within a specific
    implementation so that constraints can be used to ensure that the process details requested are
    consistent with projects requirements for information.

    """
    return {
        'type': 'class',
        'base': 'science.science_context',
        'is_abstract': False,
        'properties': [
            ('implementation_overview', 'str', '1.1',
                "General overview description of the implementation of this part of the process."),
            ('properties', 'science.detail', '0.N',
                "Sets of properties for this process."),
            ('references', 'shared.reference', '0.N',
                "Any relevant references describing this part of the process and/or it's implementation.")
        ]
    }


def tuning():
    """Method used to optimise equation parameters in model component (aka 'tuning').

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '1.1',
                "Brief description of tuning methodology. Include information about observational period(s) used."),
            ('global_mean_metrics_used', 'data.variable_collection', '0.1',
                "Set of metrics of the global mean state used in tuning model parameters."),
            ('regional_metrics_used', 'data.variable_collection', '0.1',
                "Which regional metrics of mean state (e.g Monsoons, tropical means etc) have been used in tuning."),
            ('trend_metrics_used', 'data.variable_collection', '0.1',
                "Which observed trend metrics have been used in tuning model parameters.")
        ]
    }
