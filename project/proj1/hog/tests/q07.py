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
        'locked': True,
        'test': """
        >>> dice = make_test_dice(3)   # dice always returns 3
        >>> max_scoring_num_rolls(dice)
        fd3dea4fa6dbe064e7819decc50f5148
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'answer': '444e81c65ba9564a84ae48a5099dc4e3',
        'choices': [
          'The lowest num_rolls',
          'The highest num_rolls',
          'A random num_rolls'
        ],
        'locked': True,
        'question': """
        If multiple num_rolls are tied for the highest scoring
        average, which should you return?
        """,
        'type': 'concept'
      },
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(2)     # dice always rolls 2
        >>> max_scoring_num_rolls(dice)
        fd3dea4fa6dbe064e7819decc50f5148
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
        >>> max_scoring_num_rolls(dice)
        dcedbd544b4dd65f1a51c85a270e0b21
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}