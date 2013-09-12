"""
CIM v1 shared package enums.
"""



def _change_property_type():
    """Creates and returns instance of change_property_type enum."""
    return {
        'type' : 'enum',
        'name' : 'change_property_type',
        'is_open' : False,
        'doc' : None,
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
    """Creates and returns instance of compiler_type enum."""
    return {
        'type' : 'enum',
        'name' : 'compiler_type',
        'is_open' : True,
        'doc' : 'A list of known compilers.',
        'members' : [ ],
    }


def _data_purpose():
    """Creates and returns instance of data_purpose enum."""
    return {
        'type' : 'enum',
        'name' : 'data_purpose',
        'is_open' : False,
        'doc' : 'Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.',
        'members' : [
            ('ancillaryFile', None),
            ('boundaryCondition', None),
            ('initialCondition', None),
        ],
    }


def _interconnect_type():
    """Creates and returns instance of interconnect_type enum."""
    return {
        'type' : 'enum',
        'name' : 'interconnect_type',
        'is_open' : True,
        'doc' : "A list of connectors between machines.",
        'members' : [ ],
    }


def _machine_type():
    """Creates and returns instance of machine_type enum."""
    return {
        'type' : 'enum',
        'name' : 'machine_type',
        'is_open' : False,
        'doc' : 'A list of known machines.',
        'members' : [
            ('Parallel', None),
            ('Vector', None),
            ('Beowulf', None),
        ],
    }


def _machine_vendor_type():
    """Creates and returns instance of machine_vendor_type enum."""
    return {
        'type' : 'enum',
        'name' : 'machine_vendor_type',
        'is_open' : True,
        'doc' : 'A list of organisations that create machines.',
        'members' : [ ],
    }


def _operating_system_type():
    """Creates and returns instance of operating_system_type enum."""
    return {
        'type' : 'enum',
        'name' : 'operating_system_type',
        'is_open' : True,
        'doc' : 'A list of common operating systems.',
        'members' : [ ],
    }


def _processor_type():
    """Creates and returns instance of processor_type enum."""
    return {
        'type' : 'enum',
        'name' : 'processor_type',
        'is_open' : True,
        'doc' : "A list of known cpu's.",
        'members' : [ ],
    }


def _unit_type():
    """Creates and returns instance of unit_type enum."""
    return {
        'type' : 'enum',
        'name' : 'unit_type',
        'is_open' : True,
        'doc' : "A list of scientific units.",
        'members' : [ ],
    }


# Set of package enums.
enums = [
    _change_property_type(),
    _compiler_type(),
    _data_purpose(),
    _interconnect_type(),
    _machine_type(),
    _machine_vendor_type(),
    _operating_system_type(),
    _processor_type(),
    _unit_type(),
]


