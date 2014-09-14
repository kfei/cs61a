test = {
  'names': [
    'q09',
    '9',
    'q9'
  ],
  'points': 2,
  'suites': [
    [
      {
        'test': """
        >>> swap_strategy(23, 60) # 23 + (1 + abs(6 - 0)) = 30
        0
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> swap_strategy(27, 17) # 27 + (1 + abs(1 - 7)) = 34
        5
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> swap_strategy(50, 80) # 1 + abs(8 - 0) = 9
        0
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> swap_strategy(12, 12) # Baseline
        5
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': """
        >>> swap_strategy(15, 34, 5, 4) # beneficial swap
        0
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> swap_strategy(8, 9, 5, 4) # harmful swap
        4
        """,
        'type': 'doctest'
      }
    ]
  ]
}