test = {
  'names': [
    'q07',
    '7',
    'q7'
  ],
  'points': 2,
  'suites': [
    [
      {
        'test': """
        >>> dice = make_test_dice(3)   # dice always returns 3
        >>> max_scoring_num_rolls(dice)
        10
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'answer': 'The lowest num_rolls',
        'choices': [
          'The lowest num_rolls',
          'The highest num_rolls',
          'A random num_rolls'
        ],
        'question': """
        If multiple num_rolls are tied for the highest scoring
        average, which should you return?
        """,
        'type': 'concept'
      },
      {
        'test': """
        >>> dice = make_test_dice(2)     # dice always rolls 2
        >>> max_scoring_num_rolls(dice)
        10
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
        >>> max_scoring_num_rolls(dice)
        1
        """,
        'type': 'doctest'
      }
    ]
  ]
}