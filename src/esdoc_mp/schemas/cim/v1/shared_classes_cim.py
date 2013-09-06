"""
CIM v1 shared package classes.
"""

def _cim_document_relationship():
    """Creates and returns instance of cim_document_relationship class."""
    return {
        'type' : 'class',
        'name' : 'cim_document_relationship',
        'base' : 'shared.cim_relationship',
        'abstract' : False,
        'doc' : 'Contains the set of relationships supported by a Document.',
        'properties' : [
            ('target', 'shared.cim_document_relationship_target', '1.1', None),
            ('type', 'shared.cim_document_relationship_type', '1.1', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description'),
            ('direction', 'self::cim:documentRelationship/@direction'),
            ('type', 'self::cim:documentRelationship/@type'),
            ('target', 'child::cim:target'),
        ]
    }


def _cim_document_relationship_target():
    """Creates and returns instance of cim_document_relationship_target class."""
    return {
        'type' : 'class',
        'name' : 'cim_document_relationship_target',
        'base' : None,
        'abstract' : False,
        'doc' : None,
        'properties' : [
            ('reference', 'shared.cim_reference', '0.1', None),
            ('document', 'shared.cim_document_type', '0.1', None),
        ],
        'decodings' : [
            ('reference', 'child::cim:reference'),
        ]
    }


def _cim_info():
    """Creates and returns instance of cim_info class."""
    return {
        'type' : 'class',
        'name' : 'cim_info',
        'base' : None,
        'abstract' : False,
        'doc' : 'Encapsulates common cim information.',
        'properties' : [
            ('author', 'shared.responsible_party', '0.1', 'Universally identifies the CIM instance'),
            ('create_date', 'datetime', '1.1', 'The date the instance was created'),
            ('external_ids', 'shared.standard_name', '0.N', 'A non-CIM (non-GUID) id used to reference the element in question.'),
            ('genealogy', 'shared.cim_genealogy', '0.1', 'Specifies the relationship of this document with another document. Various relationship types (depending on the type of document; ie: simulation, component, etc.) are supported.'),
            ('id', 'uuid', '1.1', 'Universally identifies the instance.'),
            ('language', 'str', '1.1', 'Language with which instance is associated with.'),
            ('metadata_id', 'uri', '0.1', None),
            ('metadata_version', 'str', '0.1', None),
            ('project', 'str', '1.1', 'Name of project with which instance is associated with.'),
            ('source', 'str', '1.1', 'The source application that created the instance.'),
            ('status', 'shared.document_status_type', '0.1', None),
            ('version', 'str', '1.1', 'Universally identifies the instance version.'),
        ],
        'decodings' : [
            ('author', 'child::cim:documentAuthor'),
            ('create_date', 'child::cim:documentCreationDate'),
            ('external_ids', 'child::cim:externalID'),
            ('genealogy', 'child::cim:documentGenealogy'),
            ('id', 'child::cim:documentID'),
            ('version', 'child::cim:documentVersion'),
        ]
    }


def _cim_genealogy():
    """Creates and returns instance of cim_genealogy class."""
    return {
        'type' : 'class',
            'name' : 'cim_genealogy',
        'base' : None,
        'abstract' : False,
        'doc' : 'A record of a document\'s history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.',
        'properties' : [
            ('relationships', 'shared.cim_relationship', '0.N', None),
        ],
        'decodings' : [
            ('relationships', 'child::cim:relationship/cim:documentRelationship', 'shared.cim_document_relationship'),
        ]
    }


def _cim_reference():
    """Creates and returns instance of reference class."""
    return {
        'type' : 'class',
        'name' : 'cim_reference',
        'base' : None,
        'abstract' : False,
        'doc' : 'A reference to another cim entity',
        'properties' : [
            ('changes', 'shared.change', '0.N', 'An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances.'),
            ('description', 'str', '0.1', 'A description of the element being referenced, in the context of the current class.'),
            ('external_id', 'str', '0.1', 'A non-CIM (non-GUID) id used to reference the element in question.'),
            ('id', 'uuid', '0.1', 'The ID of the element being referenced.'),
            ('name', 'str', '0.1', 'The name of the element being referenced.'),
            ('type', 'str', '0.1', 'The type of the element being referenced.'),
            ('version', 'str', '0.1', 'The version of the element being referenced.'),
        ],
        'decodings' : [
            ('changes', 'child::cim:change'),
            ('description', 'child::cim:description'),
            ('external_id', 'child::cim:externalID'),
            ('id', 'child::cim:id'),
            ('name', 'child::cim:name'),
            ('type', 'child::cim:type'),
            ('version', 'child::cim:version'),
        ]
    }


def _cim_relationship():
    """Creates and returns instance of relationship class."""
    return {
        'type' : 'class',
        'name' : 'cim_relationship',
        'base' : None,
        'abstract' : True,
        'doc' : 'A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document\'s genealogy.',
        'properties' : [
            ('description', 'str', '0.1', None),
            ('direction', 'shared.cim_relationship_direction_type', '1.1', None),
        ],
        'decodings' : [
        ]
    }

# Set of package classes.
classes = [
        _cim_document_relationship(),
        _cim_document_relationship_target(),
        _cim_genealogy(),
        _cim_info(),
        _cim_reference(),
        _cim_relationship()
]
