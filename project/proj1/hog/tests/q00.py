test = {
  'names': [
    'q00',
    '0',
    'q0'
  ],
  'points': 0,
  'suites': [
    [
      {
        'test': """
        >>> test_dice = make_test_dice(4, 1, 2)
        >>> test_dice()
        4
        >>> test_dice() # Second call
        1
        >>> test_dice() # Third call
        2
        >>> test_dice() # Fourth call
        4
        """,
        'type': 'doctest'
      }
    ]
  ]
}