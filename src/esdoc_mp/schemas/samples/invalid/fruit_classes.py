

def fruit():
	"""A fruit base class.

	"""
	return {
		'base': None,
		'is_abstract': True,
		'type': 'class',
		'properties': [
			# Invalid property name
			('Sweetness', 'fruit.sweetness', '1.1'),
			# Invalid property type
			('time_picked', 'xxx', '1.1'),
			# Invalid property cardinality
			('weight', 'float', '1.X')
		]
	}


def mango():
	"""A tropical fruit that growns in groves.

	"""
	return {
		# Invalid base class reference
		'base': 'xxx.yyy',
		'is_abstract': False,
		'type': 'class'
	}


def orange():
	"""A citrus fruit the best of which come from Sicily.

	"""
	# Invalid - base attribute is missing
	return {
		'is_abstract': False,
		'type': 'class'
	}
