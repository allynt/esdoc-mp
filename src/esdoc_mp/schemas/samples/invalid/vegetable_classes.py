

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


# Invalid - doc-string is missing
def carrot():
	return {
		'base': 'vegetable.vegetable',
		'is_abstract': False,
		'type': 'class'
	}


def broccoli():
	"""Green and good for the brain.

	"""
	# Invalid - is_abstract attributes is missing
	return {
		'base': 'vegetable.vegetable',
		'type': 'class'
	}

