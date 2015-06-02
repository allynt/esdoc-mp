# -*- coding: utf-8 -*-

"""
.. module:: data_classes.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 data package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def data_content():
    """The contents of the data object; like ISO: MD_ContentInformation.

    """
    return {
        'type' : 'class',
        'base' : 'shared.data_source',
        'is_abstract' : False,
        'properties' : [
            ('aggregation', 'str', '0.1', 'Describes how the content has been aggregated together: sum, min, mean, max, ...'),
            ('frequency', 'str', '0.1', 'Describes the frequency of the data content: daily, hourly, ...'),
            ('topic', 'data.data_topic', '1.1', None),
        ],
        'decodings' : [
            ('aggregation', 'child::cim:aggregation'),
            ('frequency', 'child::cim:frequency/@value'),
            ('topic', 'child::cim:topic'),
        ]
    }


def data_distribution():
    """Describes how a DataObject is distributed.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('access', 'str', '0.1', None),
            ('fee', 'str', '0.1', None),
            ('format', 'str', '0.1', None),
            ('responsible_party', 'shared.responsible_party', '0.1', None),
        ],
        'decodings' : [
            ('access', '@distributionAccess'),
            ('format', 'child::cim:distributionFormat/@value'),
            ('responsible_party', 'child::cim:responsibleParty'),
        ]
    }


def data_extent():
    """A data object extent represents the geographical and temporal coverage associated with a data object.

    """

    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('temporal', 'data.data_extent_temporal', '1.1', None),
            ('geographical', 'data.data_extent_geographical', '1.1', None),
        ],
        'decodings' : [
            ('geographical', 'child::gmd:geographicElement'),
            ('temporal', 'child::gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod'),
        ]
    }


def data_extent_geographical():
    """A data object geographical extent represents the geographical coverage associated with a data object.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('east', 'float', '0.1', None),
            ('south', 'float', '0.1', None),
            ('west', 'float', '0.1', None),
            ('north', 'float', '0.1', None),
        ],
        'decodings' : [
            ('east', 'child::gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal'),
            ('south', 'child::gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal'),
            ('west', 'child::gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal'),
            ('north', 'child::gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal'),
        ]
    }


def data_extent_temporal():
    """A data object temporal extent represents the temporal coverage associated with a data object.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('begin', 'date', '0.1', None),
            ('end', 'date', '0.1', None),
            ('time_interval', 'data.data_extent_time_interval', '0.1', None),
        ],
        'decodings' : [
            ('begin', 'child::gml:beginPosition'),
            ('end', 'child::gml:endPosition'),
            ('time_interval', 'child::gml:timeInterval'),
        ]
    }


def data_extent_time_interval():
    """A data object temporal extent represents the temporal coverage associated with a data object.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('unit', 'str', '0.1', None),
            ('factor', 'int', '0.1', None),
            ('radix', 'int', '0.1', None),
        ],
        'decodings' : [
            ('factor', '@factor'),
            ('radix', '@radix'),
            ('unit', '@unit'),
        ]
    }


def data_hierarchy_level():
    """The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('name', 'data.data_hierarchy_type', '0.1', 'What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.'),
            # TODO - sink to to shared.property_value
            ('is_open', 'bool', '0.1', None),
            # TODO - resolve property type to shared.property_value
            ('value', 'str', '0.1', 'What is the name of the specific HierarchyLevel this DataObject is being organised at (ie: if the HierarchyLevel is "run" then the name might be the runid).'),
        ],
        'decodings' : [
            ('is_open', 'child::cim:hierarchyLevelName/@open'),
            ('name', 'child::cim:hierarchyLevelName/@value'),
            ('value', 'child::cim:hierarchyLevelValue'),
        ]
    }


def data_object():
    """A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

    """
    return {
        'type' : 'class',
        'base' : 'shared.data_source',
        'is_abstract' : False,
        'is_entity' : True,
        'properties' : [
            ('meta', 'shared.doc_meta_info', '1.1', None),
            ('acronym', 'str', '0.1', None),
            ('child_object', 'data.data_object', '0.N', None),
            ('citations', 'shared.citation', '0.N', None),
            ('content', 'data.data_content', '0.N', 'The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)'),
            ('data_status', 'data.data_status_type', '0.1', None),
            ('description', 'str', '0.1', None),
            ('distribution', 'data.data_distribution', '0.1', None),
            ('extent', 'data.data_extent', '0.1', None),
            ('hierarchy_level', 'data.data_hierarchy_level', '0.1', None),
            ('keyword', 'str', '0.1', None),
            # TODO - define type
            ('geometry_model', 'str', '0.1', None),
            ('parent_object', 'data.data_object', '0.1', None),
            ('parent_object_reference', 'shared.doc_reference', '0.1', None),
            ('properties', 'data.data_property', '0.N', None),
            ('purpose', 'str', '0.1', None),
            ('restriction', 'data.data_restriction', '0.N', None),
            # TODO - define type
            ('source_simulation', 'str', '0.1', None),
            ('storage', 'data.data_storage', '0.N', None),
        ],
        'decodings' : [
            ('meta', 'self::cim:dataObject'),
            ('acronym', 'child::cim:acronym'),
            ('citations', '//cim:citation[not(cim:citation)]'),
            ('content', 'child::cim:content'),
            ('data_status', 'self::cim:dataObject/@dataStatus'),
            ('description', 'child::cim:description'),
            ('distribution', 'child::cim:distribution'),
            ('extent', 'child::cim:extent'),
            ('hierarchy_level', 'self::cim:dataObject'),
            ('keyword', 'child::cim:keyword'),
            ('properties', 'child::cim:dataProperty/cim:dataProperty'),
            ('purpose', 'self::cim:dataObject/@purpose'),
            ('storage', 'child::cim:storage/cim:ipStorage', 'data.data_storage_ip'),
        ]
    }


def data_property():
    """A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

    """
    return {
        'type' : 'class',
        'base' : 'shared.property',
        'is_abstract' : False,
        'properties' : [
            ('description', 'str', '0.1', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description'),
        ]
    }


def data_restriction():
    """An access or use restriction on some element of the DataObject actual data.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('scope', 'str', '0.1', 'The thing (data or metadata, access or use) that this restriction is applied to.'),
            ('restriction', 'str', '0.1', 'The thing (data or metadata, access or use) that this restriction is applied to.'),
            ('license', 'shared.license', '0.1', 'The thing (data or metadata, access or use) that this restriction is applied to.'),
        ],
        'decodings' : [

        ]
    }


def data_storage():
    """Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : True,
        'properties' : [
            ('size', 'int', '0.1', None),
            ('format', 'str', '0.1', None),
            ('modification_date', 'datetime', '0.1', None),
            ('location', 'str', '0.1', None),
        ],
        'decodings' : [
        ]
    }


def data_storage_db():
    """Contains attributes to describe a DataObject stored as a database file.

    """
    return {
        'type' : 'class',
        'base' : 'data.data_storage',
        'is_abstract' : False,
        'properties' : [
            ('access_string', 'str', '0.1', None),
            ('name', 'str', '0.1', None),
            ('owner', 'str', '0.1', None),
            ('table', 'str', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def data_storage_file():
    """Contains attributes to describe a DataObject stored as a single file.

    """
    return {
        'type' : 'class',
        'base' : 'data.data_storage',
        'is_abstract' : False,
        'properties' : [
            ('file_system', 'str', '0.1', None),
            ('path', 'str', '0.1', None),
            ('file_name', 'str', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def data_storage_ip():
    """Contains attributes to describe a DataObject stored as a database file.

    """
    return {
        'type' : 'class',
        'base' : 'data.data_storage',
        'is_abstract' : False,
        'properties' : [
            ('protocol', 'str', '0.1', None),
            ('host', 'str', '0.1', None),
            ('path', 'str', '0.1', None),
            ('file_name', 'str', '0.1', None),
        ],
        'decodings' : [
            ('file_name', 'child::cim:fileName'),
            ('format', 'child::cim:dataFormat/@value'),
        ]
    }


def data_topic():
    """Describes the content of a data object: the variable name, units, etc.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('name', 'str', '0.1', None),
            ('description', 'str', '0.1', None),
            ('unit', 'str', '0.1', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description'),
            ('name', 'child::cim:name'),
            ('unit', 'child::cim:unit/@value'),
        ]
    }
