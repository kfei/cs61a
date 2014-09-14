test = {
  'names': [
    'q04',
    '4',
    'q4'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': """
        >>> score0, score1, start = bid_for_start(1, 1, goal=100) # start can be 0 or 1
        >>> score0
        100
        >>> score1
        100
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> score0, score1, start = bid_for_start(2, 7, goal=100)
        >>> score0
        0
        >>> score1
        10
        >>> start
        1
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> score0, score1, start = bid_for_start(8, 3, goal=100)
        >>> score0
        10
        >>> score1
        0
        >>> start
        0
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> score0, score1, start = bid_for_start(4, 3, goal=100)
        >>> score0
        3
        >>> score1
        4
        >>> start
        0
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> score0, score1, start = bid_for_start(3, 4, goal=100)
        >>> score0
        4
        >>> score1
        3
        >>> start
        1
        """,
        'type': 'doctest'
      }
    ]
  ]
}