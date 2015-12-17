
# -*- coding: utf-8 -*-

"""
.. module:: science_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 ontology schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""


def algorithm():
    """Used to hold information associated with an algorithm which implements some key
    part of a process, and its properties. In most cases this is quite a high level concept
    and isn't intended to describe the gory detail of how the code implements the algorithm
    rather the key scientific aspects of the algorithm.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("detailed_properties", "science.process_detail", "0.N"),
            ("diagnostic_variables", "data.variable_collection", "0.N"),
            ("heading", "str", "1.1"),
            ("implementation_overview", "str", "1.1"),
            ("prognostic_variables", "data.variable_collection", "0.N"),
            ("references", "shared.citation", "0.N")
        ],
        "doc_strings": {
            "detailed_properties": "Sets of properties for this algorithm.",
            "diagnostic_variables": "Diagnostic variables associated with this algorithm.",
            "heading": "Title for this collection of algorithm/property information.",
            "implementation_overview": "Overview of the algorithm implementation.",
            "prognostic_variables": "Prognostic variables associated with this algorithm.",
            "references": "Relevant references."
        }
    }


def conservation_properties():
    """Describes how prognostic variables are conserved.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("corrected_conserved_prognostic_variables", "data.variable_collection", "0.1"),
            ("correction_methodology", "str", "0.1"),
            ("flux_correction_was_used", "bool", "1.1")
        ],
        "doc_strings": {
            "corrected_conserved_prognostic_variables": "Set of variables which are conserved by *more* than the numerical scheme alone.",
            "correction_methodology": "Description of method by which correction was achieved.",
            "flux_correction_was_used": "Flag to indicate if correction involved flux correction."
        }
    }


def extent():
    """Key scientific characteristics of the grid use to simulate a specific domain.
    Note that the extent does not itself describe a grid, so, for example, a polar
    stereographic grid may have an extent of northern boundary 90N, southern boundary
    45N, but the fact that it is PS comes from the grid_type.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("eastern_boundary", "float", "0.1"),
            ("is_global", "bool", "1.1"),
            ("maximum_vertical_level", "float", "0.1"),
            ("minimum_vertical_level", "float", "0.1"),
            ("northern_boundary", "float", "0.1"),
            ("region_known_as", "str", "0.N"),
            ("southern_boundary", "float", "0.1"),
            ("western_boundary", "float", "0.1"),
            ("z_units", "str", "1.1")
        ],
        "doc_strings": {
            "eastern_boundary": "If not global, eastern boundary in degrees of longitude.",
            "is_global": "True if horizontal coverage is global.",
            "maximum_vertical_level": "Maximum vertical level.",
            "minimum_vertical_level": "Minimum vertical level.",
            "northern_boundary": "If not global, northern boundary in degrees of latitude.",
            "region_known_as": "Identifier or identifiers for the region covered by the extent.",
            "southern_boundary": "If not global, southern boundary in degrees of latitude.",
            "western_boundary": "If not global, western boundary in degrees of longitude.",
            "z_units": "Units of vertical measure."
        }
    }


def grid_summary():
    """Key scientific characteristics of the grid use to simulate a specific domain.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("grid_extent", "science.extent", "1.1"),
            ("grid_layout", "science.grid_layouts", "1.1"),
            ("grid_type", "science.grid_types", "1.1")
        ],
        "doc_strings": {
            "grid_extent": "The extent of the computational domain in horizontal and vertical space.",
            "grid_layout": "Type of horizontal grid-layout (e.g. Arakawa C-Grid.",
            "grid_type": "Description of basic grid (e.g. 'cubed-sphere')."
        }
    }


def model():
    """A model component: can be executed standalone, and has as scientific
    description available via a link to a science.domain document. (A configured model can
     be understood in terms of a simulation, a model, and a configuration.).

    """
    return {
        "type": "class",
        "base": "software.component_base",
        "is_abstract": False,
        "properties": [
            ("category", "science.model_types", "1.1"),
            ("coupled_software_components", "science.model", "0.N"),
            ("coupled_software_components_references", "shared.doc_reference", "0.N"),
            ("coupler", "software.coupling_framework", "0.1"),
            ("extra_conservation_properties", "science.conservation_properties", "0.1"),
            ("internal_software_components", "software.software_component", "0.N"),
            ("meta", "shared.doc_meta_info", "1.1"),
            ("scientific_domain", "science.scientific_domain", "0.N"),
            ("scientific_domain_references", "shared.doc_reference", "0.N")
        ],
        "doc_strings": {
            "category": "Generic type for this model.",
            "coupled_software_components": "Software components which are linked together using a coupler to deliver this model.",
            "coupler": "Overarching coupling framework for model.",
            "extra_conservation_properties": "Details of any extra methodology needed to conserve variables between coupled components.",
            "internal_software_components": "Software modules which together provide the functionality for this model.",
            "meta": "Metadata about how the model description was constructed.",
            "scientific_domain": "The scientific domains which this model simulates."
        }
    }


def process():
    """Provides structure for description of a process simulated within a particular
    area (or domain/realm/component) of a model. This will often be subclassed
    within a specific implementation so that constraints can be used to ensure
    that the vocabulary used is consistent with project requirements.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("algorithm_properties", "science.algorithm", "0.N"),
            ("description", "str", "0.1"),
            ("detailed_properties", "science.process_detail", "0.N"),
            ("implementation_overview", "str", "1.1"),
            ("keywords", "str", "1.1"),
            ("name", "str", "1.1"),
            ("references", "shared.reference", "0.N"),
            ("time_step_in_process", "float", "0.1")
        ],
        "doc_strings": {
            "algorithm_properties": "Descriptions of algorithms and their properties used in the process.",
            "description": "Short description of the process which is being simulated.",
            "detailed_properties": "Sets of properties for this process.",
            "implementation_overview": "General overview description of the implementation of this process.",
            "keywords": "keywords to help re-use and discovery of this information.",
            "name": "Short name for the process of interest.",
            "references": "Any relevant references describing this process and/or it's implementation.",
            "time_step_in_process": "Timestep (in seconds). Only needed if differing from parent component."
        }
    }


def process_detail():
    """Three possible implementations of process_detail:
        1) A generic description of some aspect of detail,
        2) Several specific descriptions selected from a vocabulary, or
        3) One specfic property selected from a vocabulary.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("content", "str", "0.1"),
            ("heading", "str", "0.1"),
            ("properties", "shared.key_float", "0.N"),
            ("selection", "str", "0.N"),
            ("vocabulary", "str", "0.1")
        ],
        "doc_strings": {
            "content": "Free text description of process detail (if required).",
            "heading": "A heading for this detail description.",
            "properties": "Any relevant numeric properties.",
            "selection": "List of choices from the vocabulary of appropriate sub-processes.",
            "vocabulary": "Name of an enumeration vocabulary of relevant sub-processes."
        }
    }


def resolution():
    """Describes the computational spatial resolution of a component or process. Not intended
        to replace or replicate the output grid description.  When it appears as part of a process
        description, provide only properties that differ from parent domain. Note that where
        different variables have different grids, differences in resolution can be captured by
        repeating the number_of_ properties.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("equivalent_horizontal_resolution", "float", "1.1"),
            ("is_adaptive_grid", "bool", "0.1"),
            ("name", "str", "1.1"),
            ("number_of_levels", "int", "0.N"),
            ("number_of_xy_gridpoints", "int", "0.N")
        ],
        "doc_strings": {
            "equivalent_horizontal_resolution": "Resolution in metres of 'typical grid cell' (for gross comparisons of resolution), eg. 50000 (50km).",
            "is_adaptive_grid": "Default is False, set true if grid resolution changes during execution.",
            "name": "This is a string usually used by the modelling group to describe their model component  or process resolution,  e.g. N512L180 or T512L70 etc.",
            "number_of_levels": "Number of vertical levels resolved.",
            "number_of_xy_gridpoints": "Total number of horizontal points on computational grids."
        }
    }


def scientific_domain():
    """Scientific area of a numerical model - usually a sub-model or component.
    Can also be known as a realm.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("extra_conservation_properties", "science.conservation_properties", "0.1"),
            ("grid", "science.grid_summary", "0.1"),
            ("meta", "shared.doc_meta_info", "1.1"),
            ("name", "str", "1.1"),
            ("overview", "str", "0.1"),
            ("realm", "str", "0.1"),
            ("references", "shared.reference", "0.N"),
            ("resolution", "science.resolution", "1.1"),
            ("simulates", "science.process", "1.N"),
            ("time_step", "float", "1.1"),
            ("tuning_applied", "science.tuning", "0.1")
        ],
        "doc_strings": {
            "extra_conservation_properties": "Details of any extra methodology needed to conserve variables between processes.",
            "grid": "Summary description of the grid upon which computations were carried out.",
            "meta": "Metadata describing the construction of this domain description.",
            "name": "Name of the scientific domain (e.g. ocean).",
            "overview": "Free text overview description of key properties of domain.",
            "realm": "Canonical name for the domain of this scientific area.",
            "references": "Any relevant references describing the implementation of this domain in a relevant model.",
            "resolution": "Default resolution of component.",
            "simulates": "Processes simulated within the domain.",
            "time_step": "Timestep (in seconds) of overall component.",
            "tuning_applied": "Describe any tuning used to optimise the parameters in this model/component."
        }
    }


def tuning():
    """Method used to optimise equation parameters in model component (aka 'tuning').

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("description", "str", "1.1"),
            ("global_mean_metrics_used", "data.variable_collection", "0.1"),
            ("regional_metrics_used", "data.variable_collection", "0.1"),
            ("trend_metrics_used", "data.variable_collection", "0.1")
        ],
        "doc_strings": {
            "description": "Brief description of tuning methodology. Include information about observational period(s) used.",
            "global_mean_metrics_used": "Set of metrics of the global mean state used in tuning model parameters.",
            "regional_metrics_used": "Which regional metrics of mean state (e.g Monsoons, tropical means etc) have been used in tuning.",
            "trend_metrics_used": "Which observed trend metrics have been used in tuning model parameters."
        }
    }
