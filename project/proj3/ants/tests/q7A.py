test = {
  'names': [
    'q7A',
    '7A',
    'qA7',
    'A7'
  ],
  'points': 3,
  'suites': [
    [
      {
        'test': r"""
        >>> # Testing NinjaAnt parameters
        >>> ninja = NinjaAnt()
        >>> ninja.armor
        1
        >>> NinjaAnt.food_cost
        6
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing non-NinjaAnts still block bees
        >>> p0 = colony.places["tunnel_0_0"]
        >>> p1 = colony.places["tunnel_0_1"]
        >>> bee = Bee(2)
        >>> p1.add_insect(bee)
        >>> p1.add_insect(ThrowerAnt())
        >>> bee.action(colony)  # attack ant, don't move past it
        >>> bee.place
        p1
        # choice: p1
        # choice: p0
        # choice: None
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing NinjaAnts do not block bees
        >>> p0 = colony.places["tunnel_0_0"]
        >>> p1 = colony.places["tunnel_0_1"]
        >>> bee = Bee(2)
        >>> p1.add_insect(bee)
        >>> p1.add_insect(NinjaAnt())
        >>> bee.action(colony)  # shouldn't attack ant, move past it
        >>> bee.place
        p0
        # choice: p0
        # choice: p1
        # choice: None
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing NinjaAnt strikes all bees in its place
        >>> test_place = colony.places["tunnel_0_0"]
        >>> for _ in range(3):
        ...     test_place.add_insect(Bee(1))
        >>> ninja = NinjaAnt()
        >>> test_place.add_insect(ninja)
        >>> ninja.action(colony)   # should strike all bees in place
        >>> len(test_place.bees)
        0
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing damage is looked up on the instance
        >>> place = colony.places["tunnel_0_0"]
        >>> bee = Bee(900)
        >>> place.add_insect(bee)
        >>> buffNinja = NinjaAnt()
        >>> buffNinja.damage = 500  # Sharpen the sword
        >>> place.add_insect(buffNinja)
        >>> buffNinja.action(colony)
        >>> bee.armor
        400
        """,
        'type': 'doctest'
      }
    ]
  ]
}