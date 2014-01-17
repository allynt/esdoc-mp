"""
CIM v1 quality package classes.
"""



def _evaluation():
    """Creates and returns instance of evaluation class."""
    return {
        'type' : 'class',
        'name' : 'evaluation',
        'base' : None,
        'is_abstract' : False,
        'doc' : None,
        'properties' : [
            ('date', 'datetime', '0.1', None),
            ('description', 'str', '0.1', None),
            ('did_pass', 'bool', '0.1', None),
            ('explanation', 'str', '0.1', None),
            ('specification', 'str', '0.1', None),
            ('specification_hyperlink', 'str', '0.1', None),
            ('type', 'str', '0.1', None),
            ('type_hyperlink', 'str', '0.1', None),
            ('title', 'str', '0.1', None),
        ],
        'decodings' : [
            ('date', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date'),
            ('description', 'gmd:evaluationMethodDescription/gco:CharacterString'),
            ('did_pass', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:pass/gco:Boolean'),
            ('explanation', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString'),
            ('type', 'child::gmd:result/@xlink:title'),
            ('type_hyperlink', 'child::gmd:result/@xlink:href'),
            ('specification', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/@xlink:title'),
            ('specification_hyperlink', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/@xlink:href'),
            ('title', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:title'),
        ]
    }


def _measure():
    """Creates and returns instance of measure class."""
    return {
        'type' : 'class',
        'name' : 'measure',
        'base' : None,
        'is_abstract' : False,
        'doc' : None,
        'properties' : [
            ('description', 'str', '0.1', None),
            ('identification', 'str', '0.1', None),
            ('name', 'str', '0.1', None),
        ],
        'decodings' : [
            ('description', 'child::cim:measureDescription'),
            ('identification', 'child::cim:measureIdentification/gmd:code/gco:CharacterString'),
            ('name', 'child::cim:nameOfMeasure'),

            # Hacks due to DKRZ misimplementation.
            ('description', 'parent::cim:report/child::gmd:measureDescription/gco:CharacterString'),
            ('name', 'parent::cim:report/child::gmd:nameOfMeasure/gco:CharacterString'),
        ]
    }


def _cim_quality():
    """Creates and returns instance of cim_quality class."""
    return {
        'type' : 'class',
        'name' : 'cim_quality',
        'base' : None,
        'is_abstract' : False,
        'is_entity' : True,
        'doc' : 'The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.',
        'properties' : [
            ('doc_info', 'shared.doc_info', '1.1', None),
            ('reports', 'quality.report', '0.N', None),
        ],
        'decodings' : [
            ('doc_info', 'self::cim:cIM_Quality'),
            ('reports', 'child::cim:report'),
        ]
    }


def _report():
    """Creates and returns instance of report class."""
    return {
        'type' : 'class',
        'name' : 'report',
        'base' : None,
        'is_abstract' : False,
        'doc' : None,
        'properties' : [
            ('date', 'datetime', '0.1', None),
            ('evaluation', 'quality.evaluation', '1.1', None),
            ('evaluator', 'shared.responsible_party', '0.1', None),
            ('measure', 'quality.measure', '1.1', None),
        ],
        'decodings' : [
            ('date', 'child::gmd:dateTime/gco:DateTime'),
            ('evaluation', 'self::cim:report'),
            ('evaluator', 'child::cim:evaluator'),
            ('measure', 'self::cim:report/cim:measure'),
        ]
    }


# Set of package classes.
classes = [
    _cim_quality(),
    _evaluation(),
    _measure(),
    _report(),
]
