# -*- coding: utf-8 -*-

"""
CIM v1 shared package time reated classes.
"""

def calendar():
    """Creates and returns instance of calendar class."""
    return {
        'type' : 'class',
        'name' : 'calendar',
        'base' : None,
        'is_abstract' : True,
        'doc' : 'Describes a method of calculating a span of dates.',
        'properties' : [
            ('description', 'str', '0.1', 'Describes the finer details of the calendar, in case they are not-obvious.  For example, if an experiment has changing conditions within it (ie: 1% CO2 increase until 2100, then hold fixed for the remaining period of the  experment)'),
            ('length', 'int', '0.1', None),
            ('range', 'shared.date_range', '0.1', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description'),
            ('length', 'child::cim:length'),
            ('range', 'child::cim:range/cim:closedDateRange', 'shared.closed_date_range'),
            ('range', 'child::cim:range/cim:openDateRange', 'shared.open_date_range'),
        ]
    }


def closed_date_range():
    """Creates and returns instance of closed_date_range class."""
    return {
        'type' : 'class',
        'name' : 'closed_date_range',
        'base' : 'shared.date_range',
        'is_abstract' : False,
        'doc' : 'A date range with specified start and end points.',
        'properties' : [
            ('end', 'datetime', '0.1', 'End date is optional becuase the length of a ClosedDateRange can be calculated from the StartDate plus the Duration element.'),
            ('start', 'datetime', '1.1', None),
        ],
        'decodings' : [
            ('end', 'child::cim:endDate'),
            ('start', 'child::cim:startDate'),
        ]
    }


def daily_360():
    """Creates and returns instance of daily_360 class."""
    return {
        'type' : 'class',
        'name' : 'daily_360',
        'base' : 'shared.calendar',
        'is_abstract' : False,
        'doc' : None,
        'properties' : [ ],
        'decodings' : [ ]
    }


def date_range():
    """Creates and returns instance of date_range class."""
    return {
        'type' : 'class',
        'name' : 'date_range',
        'base' : None,
        'is_abstract' : True,
        'doc' : None,
        'properties' : [
            ('duration', 'str', '0.1', None),
        ],
        'decodings' : [
            ('duration', 'child::cim:duration'),
        ]
    }


def open_date_range():
    """Creates and returns instance of open_date_range class."""
    return {
        'type' : 'class',
        'name' : 'open_date_range',
        'base' : 'shared.date_range',
        'is_abstract' : False,
        'doc' : 'A date range without a specified start and/or end point.',
        'properties' : [
            ('end', 'datetime', '0.1', None),
            ('start', 'datetime', '0.1', None),
        ],
        'decodings' : [
            ('end', 'child::cim:endDate'),
            ('start', 'child::cim:startDate'),
        ]
    }


def perpetual_period():
    """Creates and returns instance of perpetual_period class."""
    return {
        'type' : 'class',
        'name' : 'perpetual_period',
        'base' : 'shared.calendar',
        'is_abstract' : False,
        'doc' : None,
        'properties' : [ ],
        'decodings' : [ ]
    }
    

def real_calendar():
    """Creates and returns instance of real_calendar class."""
    return {
        'type' : 'class',
        'name' : 'real_calendar',
        'base' : 'shared.calendar',
        'is_abstract' : False,
        'doc' : None,
        'properties' : [ ],
        'decodings' : [ ]
    }
