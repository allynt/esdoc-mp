# -*- coding: utf-8 -*-

"""
.. module:: shared_enums.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v2 time related shared enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def calendar_types():
    """CF calendar types as defined in CF 1.6.

    """
    return {
        'type':'enum',
        'base':None,
        'is_open':False,
        'members':[
            ('gregorian','Mixed Gregorian/Julian calendar as defined by Udunits'),
            ('standard','Synonym for gregorian: Mixed Gregorian/Julian calendar as defined by Udunits'),
            ('proleptic_gregorian','A Gregorian calendar extended to dates before 1582-10-15. That is, a year is a leap year if either (i) it is divisible by 4 but not by 100 or (ii) it is divisible by 400.'),
            ('noleap','Gregorian calendar without leap years, i.e., all years are 365 days long.'),
            ('365_day','Synonym for noleap:Gregorian calendar without leap years, i.e., all years are 365 days long.'),
            ('all_leap','Gregorian calendar with every year being a leap year, i.e., all years are 366 days long.'),
            ('366_day','Synonym for all_leap:Gregorian calendar with every year being a leap year, i.e., all years are 366 days long.'),
            ('360_day','All years are 360 days divided into 30 day months.'),
            ('julian','Julian Calendar'),
            ('none','Perpetual time axis'),
        ],
    }


def period_date_types():
    """Create and return a period date type enum (used by time_period).

    """
    return {
        'type':'enum',
        'base':None,
        'doc':'Describes how a date is used in a period description',
        'is_open':False,
        'members':[
            ('unused','Date is not used'),
            ('date is start','The date defines the start of the period'),
            ('date is end','The date is the end of the period'),
        ],
    }


def slicetime_units():
    """Units for integers in a timeslice.

    """
    return {
        'type':'enum',
        'base':None,
        'is_open':False,
        'members':[
            ('yearly',None),
            ('monthly',None),
        ],
    }


def time_units():
    """Appropriate Time units for experiment durations in NWP and Climate Modelling.

    """
    # Don't include months, they're complicated!
    return {
        'type':'enum',
        'base':None,
        'is_open':False,
        'members':[
            ('years',None),
            ('days',None),
            ('seconds',None),
        ],
    }


