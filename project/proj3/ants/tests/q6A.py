test = {
  'names': [
    'q6A',
    'qA6',
    '6A',
    'A6'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': r"""
        >>> # Testing WallAnt parameters
        >>> wall = WallAnt()
        >>> wall.armor
        4
        >>> WallAnt.food_cost
        4
        """,
        'type': 'doctest'
      }
    ]
  ]
}