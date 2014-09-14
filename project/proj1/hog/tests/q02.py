test = {
  'names': [
    'q02',
    '2',
    'q2'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': """
        >>> take_turn(2, 0,  make_test_dice(4, 6, 1))
        10
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> take_turn(3, 20, make_test_dice(4, 6, 1))
        1
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> take_turn(0, 35)
        3
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> take_turn(0, 71)
        7
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> take_turn(0, 7)
        8
        """,
        'type': 'doctest'
      }
    ]
  ]
}