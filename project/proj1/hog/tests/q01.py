test = {
  'names': [
    'q01',
    '1',
    'q1'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': """
        >>> roll_dice(2, make_test_dice(4, 6, 1))
        10
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> roll_dice(3, make_test_dice(4, 6, 1))
        1
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> roll_dice(3, make_test_dice(1, 2, 3))
        1
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> counted_dice = make_test_dice(4, 1, 2, 6)
        >>> roll_dice(3, counted_dice)
        1
        >>> roll_dice(1, counted_dice)  # Make sure you call dice exactly num_rolls times!
        6
        """,
        'type': 'doctest'
      }
    ]
  ]
}