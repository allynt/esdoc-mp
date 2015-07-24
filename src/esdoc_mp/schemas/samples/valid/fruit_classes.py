

def fruit():
	"""A fruit base class.

	"""
	return {
		'base': None,
		'is_abstract': True,
		'type': 'class',
		'properties': [
			('sweetness', 'fruit.sweetness', '1.1'),
			('time_picked', 'datetime', '1.1'),
			('weight', 'float', '1.1')
		]
	}


def mango():
	"""A tropical fruit that growns in groves.

	"""
	return {
		'base': 'fruit.fruit',
		'is_abstract': False,
		'type': 'class'
	}


def orange():
	"""A citrus fruit the best of which come from Sicily.

	"""
	return {
		'base': 'fruit.fruit',
		'is_abstract': False,
		'type': 'class'
	}

