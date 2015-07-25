

def sweetness():
    """Measure of a fruit's sweetness.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('low', 'A relatively low amount of sugar per fruit.'),
            ('medium', 'An average amount of sugar per fruit.'),
            ('high', 'A higher than average amount of sugar per fruit.'),
        ],
    }
