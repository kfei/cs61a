test = {
  'names': [
    'q2',
    '2'
  ],
  'points': 2,
  'suites': [
    [
      {
        'test': r"""
        >>> HarvesterAnt.food_cost
        2
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> ThrowerAnt.food_cost
        4
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing HarvesterAnt action
        >>> colony.food = 4
        >>> HarvesterAnt().action(colony)
        >>> colony.food
        5
        >>> HarvesterAnt().action(colony)
        >>> colony.food
        6
        """,
        'type': 'doctest'
      }
    ]
  ]
}