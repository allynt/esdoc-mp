

def vegetable():
	"""A vegetable base class.

	"""
	return {
		'base': None,
		'is_abstract': False,
		'type': 'class',
		'properties': [
			('fibrosity', 'vegetable.fibrosity', '1.1'),
			('time_picked', 'datetime', '1.1'),
			('weight', 'float', '1.1')
		]
	}


def carrot():
	"""Orange and good for the eyes.

	"""
	return {
		'base': 'vegetable.vegetable',
		'is_abstract': False,
		'type': 'class'
	}


def broccoli():
	"""Green and good for the brain.

	"""
	return {
		'base': 'vegetable.vegetable',
		'is_abstract': False,
		'type': 'class'
	}

