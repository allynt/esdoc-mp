

def fibrosity():
    """Measure of a vegetable's fibrosity.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('low', 'Relatively low in fibre per vegatable.'),
            ('medium', 'Average amount of fibre per vegatable.'),
            ('high', 'High amount of fibre per vegatable.'),
        ]
    }
