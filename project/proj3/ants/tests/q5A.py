test = {
  'names': [
    'q5A',
    'qA5',
    '5A',
    'A5'
  ],
  'points': 3,
  'suites': [
    [
      {
        'test': r"""
        >>> # Testing fire parameters
        >>> fire = FireAnt()
        >>> FireAnt.food_cost
        4
        >>> fire.armor
        1
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing fire damage
        >>> place = Place('Fire Test1')
        >>> bee = Bee(5)
        >>> place.add_insect(bee)
        >>> place.add_insect(FireAnt())
        >>> bee.action(colony) # attack the FireAnt
        >>> bee.armor
        2
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing fire does damage to all Bees in its Place
        >>> place = Place('Fire Test2')
        >>> bee = Bee(3)
        >>> place.add_insect(bee)
        >>> place.add_insect(Bee(3))
        >>> place.add_insect(FireAnt())
        >>> bee.action(colony) # attack the FireAnt
        >>> len(place.bees)  # How many bees are left?
        0
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing FireAnt dies
        >>> place = Place('Fire Test3')
        >>> bee = Bee(1)
        >>> ant = FireAnt()
        >>> place.add_insect(bee)
        >>> place.add_insect(ant)
        >>> bee.action(colony) # attack the FireAnt
        >>> ant.armor
        0
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing fire damage is instance attribute
        >>> place = Place('Fire Test4')
        >>> bee = Bee(900)
        >>> buffAnt = ants.FireAnt()
        >>> buffAnt.damage = 500   # Feel the burn!
        >>> place.add_insect(bee)
        >>> place.add_insect(buffAnt)
        >>> bee.action(colony) # attack the FireAnt
        >>> bee.armor  # is damage an instance attribute?
        400
        """,
        'type': 'doctest'
      }
    ]
  ]
}