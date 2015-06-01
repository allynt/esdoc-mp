# -*- coding: utf-8 -*-

"""
CIM v1 activity package enums.
"""



def conformance_type():
    """Creates and returns instance of conformance_type enum."""
    return {
        'type' : 'enum',
        'name' : 'conformance_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('not conformant', 'Describes a simulation that is purpefully non-conformant to an experimental requirement.'),
            ('standard config', 'Describes a simulation that is "naturally" conformant to an experimental requirement.'),
            ('via inputs', 'Describes a simulation that conforms to an experimental requirement by using particular inputs.'),
            ('via model mods', 'Describes a simulation that conforms to an experimental requirement by changing the configuration of the software model implementing that simulation.'),
            ('combination', 'Describes a simulation that conforms to an experimental requirement by using more than one method.'),
        ],
    }


def downscaling_type():
    """Creates and returns instance of downscaling_type enum."""
    return {
        'type' : 'enum',
        'name' : 'downscaling_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('statistical', None),
            ('dynamic', None),
        ],
    }


def ensemble_type():
    """Creates and returns instance of ensemble_type enum."""
    return {
        'type' : 'enum',
        'name' : 'ensemble_type',
        'is_open' : True,
        'doc' : None,
        'members' : [

        ],
    }


def experiment_relationship_type():
    """Creates and returns instance of experiment_relationship_type enum."""
    return {
        'name' : 'experiment_relationship_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('previousRealisation', None),
            ('continuationOf', None),
            ('controlExperiment', None),
            ('higherResolutionVersionOf', None),
            ('lowerResolutionVersionOf', None),
            ('increaseEnsembleOf', None),
            ('modifiedInputMethodOf', None),
            ('shorterVersionOf', None),
            ('extensionOf', None),
        ],
    }


def frequency_type():
    """Creates and returns instance of frequency_type enum."""
    return {
        'type' : 'enum',
        'name' : 'frequency_type',
        'is_open' : True,
        'doc' : None,
        'members' : [

        ],
    }


def project_type():
    """Creates and returns instance of project_type enum."""
    return {
        'type' : 'enum',
        'name' : 'project_type',
        'is_open' : True,
        'doc' : None,
        'members' : [],
    }


def resolution_type():
    """Creates and returns instance of resolution_type enum."""
    return {
        'type' : 'enum',
        'name' : 'resolution_type',
        'is_open' : True,
        'doc' : None,
        'members' : [],
    }    


def simulation_relationship_type():
    """Creates and returns instance of simulation_relationship_type enum."""
    return {
        'name' : 'simulation_relationship_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('extensionOf', None),
            ('responseTo', None),
            ('continuationOf', None),
            ('previousSimulation', None),
            ('higherResolutionVersionOf', None),
            ('lowerResolutionVersionOf', None),
            ('fixedVersionOf', None),
            ('followingSimulation', None),
        ],
    }


def simulation_type():
    """Creates and returns instance of simulation_type enum."""
    return {
        'type' : 'enum',
        'name' : 'simulation_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('simulationRun', None),
            ('assimilation', None),
            ('simulationComposite', None),
        ],
    }



