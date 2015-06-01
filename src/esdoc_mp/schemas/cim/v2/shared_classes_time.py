# -*- coding: utf-8 -*-

"""
.. module:: shared_classes_time.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 time related shared class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""


def calendar():
    """Describes the calendar required/used in an experiment/simulation. This class is based on the
    calendar attributes and properties found in the CF netCDF conventions.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'pstr':('%s',('cal_type',)),
        'properties' : [
            ('description', 'str', '0.1', 'Extra information about the calendar'),
            ('cal_type','time.calendar_types','1.1','Type of calendar used'),
            ('name','str','0.1','Can be used to name a special calendar type'),
            ('month_lengths','int','0.N','Used for special calendars to provide month lengths'),
        ],
    }


def date_time():
    """A date or time. Either in simulation time with the simulation
       calendar, or with reference to a simulation start, in which
       case the datetime is an interval after the start date.

    """
    return {
        'type': 'class',
        'is_abstract': False,
        'base': None,
        'pstr': ('%s(offset %s)',('value','offset')),
        'properties':[
            ('value','str','1.1','Date or time - some of (from left to right): yyyy-mm-dd:hh:mm:ss'),
            ('offset','bool','0.1','Date is offset from start of an integration'),
        ],
    }


def datetime_set():
    """Provides a set of dates which are displaced by a regular interval.

    Note that we assume either a periodic set of dates which can
    be date and/or time, or an irregular set which can only be dates.

    """
    return  {
        'type': 'class',
        'is_abstract': True,
        'base': None,
        'properties': [
            ('length','int','1.1','Number of times in set'),
        ]
    }


def irregular_date_set():
    """Provides a set of dates as a list of dates.

    """
    return  {
        'type': 'class',
        'is_abstract':False,
        'base': 'shared.datetime_set',
        'properties': [
            ('date_set','str','1.1','Set of dates, comma separated yyyy-mm-dd'),
        ],
    }


def regular_time_set():
    """Provides a set of dates which are displaced by a regular interval.

    """
    return  {
        'type': 'class',
        'is_abstract':False,
        'base': 'shared.datetime_set',
        'pstr':('%s times from %s at %s intervals',('length','start_date','increment')),
        'properties': [
            ('start_date','time.date_time','1.1','Beginning of time set'),
            ('length','int','1.1','Number of times in set'),
            ('increment','time.time_period','1.1','Interval between members of set'),
        ],
    }


def time_period():
    """Provides a time interval description."""
    # Simplify all those things we had in CIM 1.x ... they're all in here ...
    # Should be XML serialised using an EX_TemporalExtent.
    return {
        'type': 'class',
        'is_abstract':False,
        'base':None,
        'pstr':('%s %s',('length','units')),
        'properties': [
            ('length','int','1.1','Duration of the time period'),
            ('units','time.time_units','1.1','Appropriate time units'),
            ('calendar','time.calendar','0.1','Calendar, default is standard aka gregorian'),
            ('date','time.date_time','0.1','Optional start/end date of time period'),
            ('date_type','time.period_date_types','1.1','Describes how the date is used to define the period'),
        ]
    }


def timeslice_list():
    """A list of timeslices either as months in  year, or as days in a month:
        yearlist: 1,4,5 refers to jan,april,may,
        monthlist: 1,5,6 refers to the 1st, 5th and 6th of the month

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract':False,
        'properties': [
            ('members','shared.numberArray','1.1','Values as integers'),
            ('units','time.slicetimeUnits','1.1','Interval against which members refer'),
        ]
    }
