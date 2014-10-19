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
        'locked': True,
        'test': r"""
        >>> # Testing NinjaAnt parameters
        >>> ninja = NinjaAnt()
        >>> ninja.armor
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
        >>> NinjaAnt.food_cost
        6e64cd41ecdfe7fd3b99f4395dfd7c25
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing non-NinjaAnts still block bees
        >>> p0 = colony.places["tunnel_0_0"]
        >>> p1 = colony.places["tunnel_0_1"]
        >>> bee = Bee(2)
        >>> p1.add_insect(bee)
        >>> p1.add_insect(ThrowerAnt())
        >>> bee.action(colony)  # attack ant, don't move past it
        >>> bee.place
        fb50f4eb57e41edbc17b6cd4060c23cb
        # locked
        # choice: p1
        # choice: p0
        # choice: None
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> # Testing NinjaAnts do not block bees
        >>> p0 = colony.places["tunnel_0_0"]
        >>> p1 = colony.places["tunnel_0_1"]
        >>> bee = Bee(2)
        >>> p1.add_insect(bee)
        >>> p1.add_insect(NinjaAnt())
        >>> bee.action(colony)  # shouldn't attack ant, move past it
        >>> bee.place
        a45151fa4d29859b7aa62dce41584097
        # locked
        # choice: p0
        # choice: p1
        # choice: None
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing NinjaAnt strikes all bees in its place
        >>> test_place = colony.places["tunnel_0_0"]
        >>> for _ in range(3):
        ...     test_place.add_insect(Bee(1))
        >>> ninja = NinjaAnt()
        >>> test_place.add_insect(ninja)
        >>> ninja.action(colony)   # should strike all bees in place
        >>> len(test_place.bees)
        11862fc8ebde17878dbcfc9a133b7094
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
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
        224199c2ecb34505040bc79e373e3edf
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}