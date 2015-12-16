
# -*- coding: utf-8 -*-

"""
.. module:: software_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 ontology schema definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""


def component_base():
    """Base class for software component properties, whether a top level model,
    or a specific piece of code known as a component. In software terms, a
    component is a discrete set of code that takes input data and generates output data.
    Components may or may not have scientific descriptions.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": True,
        "properties": [
            ("description", "str", "0.1"),
            ("development_history", "software.development_path", "0.1"),
            ("documentation", "shared.citation", "0.N"),
            ("long_name", "str", "0.1"),
            ("name", "str", "1.1"),
            ("release_date", "datetime", "0.1"),
            ("repository", "shared.online_resource", "0.1"),
            ("version", "str", "0.1")
        ],
        "doc_strings": {
			"description": "Textural description of component",
			"development_history": "History of the development of this component",
			"documentation": "Descriptions of the component functionality",
			"long_name": "Long name for component",
			"name": "Short name of component",
			"release_date": "The date of publication of the component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)",
			"repository": "Location of code for this component",
			"version": "Version identifier"
        }
    }


def composition():
    """Describes how component variables are coupled together either to/from other
    SoftwareComponents or external data files. The variables specified by a component's
    composition must be owned by that component, or a  child of that component;
    child components cannot couple together parent variables.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("couplings", "str", "0.N"),
            ("description", "str", "0.1")
        ],
        "doc_strings": {
			"couplings": "#FIXME",
			"description": "#FIXME"
        }
    }


def development_path():
    """Describes the software development path for this model/component.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("consortium_name", "str", "0.1"),
            ("creators", "shared.responsibility", "0.N"),
            ("developed_in_house", "bool", "1.1"),
            ("funding_sources", "shared.responsibility", "0.N"),
            ("previous_version", "str", "0.1")
        ],
        "doc_strings": {
			"consortium_name": "If model/component is developed as part of a consortium, provide consortium name.",
			"creators": "Those responsible for creating this component",
			"developed_in_house": "Model or component was mostly developed in house",
			"funding_sources": "The entities that funded this software component.",
			"previous_version": "Name of a previous version"
        }
    }


def entry_point():
    """Describes a function or subroutine of a SoftwareComponent.
    BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model.
    Currently, a very basic schedule can be approximated by using the "proceeds" and "follows" attributes,
    however a more complete system is required for full BFG compatibility.
    Every EntryPoint can have a set of arguments associated with it.
    These reference (previously defined) variables.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("name", "str", "0.1")
        ],
        "doc_strings": {
			"name": "#FIXME"
        }
    }


def gridspec():
    """Fully defines the computational grid used.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("description", "str", "1.1")
        ],
        "doc_strings": {
			"description": "Textural description"
        }
    }


def software_component():
    """An embedded piece of software that does not normally function as a standalone model (although
    it may be used standalone in a test harness).

    """
    return {
        "type": "class",
        "base": "software.component_base",
        "is_abstract": False,
        "properties": [
            ("composition", "software.composition", "0.1"),
            ("connection_points", "software.variable", "0.N"),
            ("coupling_framework", "software.coupling_framework", "0.1"),
            ("dependencies", "software.entry_point", "0.N"),
            ("grid", "software.gridspec", "0.1"),
            ("language", "software.programming_language", "0.1"),
            ("license", "str", "0.1"),
            ("sub_components", "software.software_component", "0.N")
        ],
        "doc_strings": {
			"composition": "#FIXME",
			"connection_points": "The set of data entities which are available for I/O and/or coupling",
			"coupling_framework": "The coupling framework that this entire component conforms to.",
			"dependencies": "#FIXME",
			"grid": "A reference to the grid that is used by this component.",
			"language": "Language the component is written in",
			"license": "The license held by this piece of software.",
			"sub_components": "Internal software sub-components of this component."
        }
    }


def variable():
    """An instance of a model software variable which may be prognostic or diagnostic, and which is
    available as a connection to other software components. Note that these variables may only exist
    within the software workflow as interim quantities or coupling endpoints. Input and output
    variables will be a subset of these software variables.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("description", "str", "0.1"),
            ("name", "str", "1.1"),
            ("prognostic", "bool", "1.1")
        ],
        "doc_strings": {
			"description": "Description of how the variable is being used in the s/w",
			"name": "Short name for the variable",
			"prognostic": "Whether or not prognostic or diagnostic"
        }
    }
