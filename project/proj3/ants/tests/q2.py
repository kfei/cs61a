test = {
  'names': [
    'q2',
    '2'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> HarvesterAnt.food_cost
        b911fabd1c66f55e635ee4f72fd9b5c1
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> ThrowerAnt.food_cost
        f4b3281120d40117b023d6c1a373fde6
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> # Testing HarvesterAnt action
        >>> colony.food = 4
        >>> HarvesterAnt().action(colony)
        >>> colony.food
        9120598f73414c1b785655f8e4e2c576
        # locked
        >>> HarvesterAnt().action(colony)
        >>> colony.food
        6e64cd41ecdfe7fd3b99f4395dfd7c25
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}