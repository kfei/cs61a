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
        'locked': True,
        'test': r"""
        >>> # Testing WallAnt parameters
        >>> wall = WallAnt()
        >>> wall.armor
        f4b3281120d40117b023d6c1a373fde6
        # locked
        >>> WallAnt.food_cost
        f4b3281120d40117b023d6c1a373fde6
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}