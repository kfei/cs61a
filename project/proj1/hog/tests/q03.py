test = {
  'names': [
    'q03',
    '3',
    'q3'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': """
        >>> select_dice(4, 24) == six_sided
        False
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> select_dice(16, 64) == six_sided
        True
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> select_dice(0, 0) == six_sided
        False
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> select_dice(50, 80) == six_sided
        True
        """,
        'type': 'doctest'
      }
    ]
  ]
}