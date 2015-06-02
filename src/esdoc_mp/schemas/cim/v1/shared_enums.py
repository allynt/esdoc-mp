# -*- coding: utf-8 -*-

"""
.. module:: shared_enums.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 shared package enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def _change_property_type():
    """Creates and returns instance of change_property_type enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('InputMod', None),
            ('ModelMod', None),
            ('Decrement', None),
            ('Increment', None),
            ('Redistribution', None),
            ('Replacement', None),
            ('ParameterChange', 'A specific type of ModelMod'),
            ('CodeChange', 'A specific type of ModelMod'),
            ('AncillaryFile', 'A specific type of ModelMod'),
            ('BoundaryCondition', 'A specific type of ModelMod'),
            ('InitialCondition', 'A specific type of ModelMod'),
            ('Unused', None),
        ],
    }


def _compiler_type():
    """Creates and returns instance of compiler_type enum.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def _data_purpose():
    """Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('ancillaryFile', None),
            ('boundaryCondition', None),
            ('initialCondition', None),
        ],
    }


def _interconnect_type():
    """A list of connectors between machines.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def _machine_type():
    """A list of known machines.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('Parallel', None),
            ('Vector', None),
            ('Beowulf', None),
        ],
    }


def _machine_vendor_type():
    """A list of organisations that create machines.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def _operating_system_type():
    """A list of common operating systems.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def _processor_type():
    """A list of known cpu's.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def _unit_type():
    """A list of scientific units.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


