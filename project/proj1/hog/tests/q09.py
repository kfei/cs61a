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
        'locked': True,
        'test': """
        >>> swap_strategy(23, 60) # 23 + (1 + abs(6 - 0)) = 30
        a35a401fcb51280d218e16de5e7cb0a7
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(27, 17) # 27 + (1 + abs(1 - 7)) = 34
        d87e16ee855df1206e866191a0fa53c5
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(50, 80) # 1 + abs(8 - 0) = 9
        a35a401fcb51280d218e16de5e7cb0a7
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(12, 12) # Baseline
        d87e16ee855df1206e866191a0fa53c5
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(15, 34, 5, 4) # beneficial swap
        a35a401fcb51280d218e16de5e7cb0a7
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(8, 9, 5, 4) # harmful swap
        faad4f8d17a80574927d9912aba33890
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}