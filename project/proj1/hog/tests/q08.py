test = {
  'names': [
    'q08',
    'q8',
    '8'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': """
        >>> bacon_strategy(0, 0)
        5
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> bacon_strategy(70, 50)
        5
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> bacon_strategy(50, 70)
        0
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> bacon_strategy(32, 4, 5, 4)
        0
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> bacon_strategy(20, 25, 5, 4)
        4
        """,
        'type': 'doctest'
      }
    ]
  ]
}