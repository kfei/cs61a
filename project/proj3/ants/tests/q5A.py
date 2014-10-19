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
        'locked': True,
        'test': r"""
        >>> # Testing fire parameters
        >>> fire = FireAnt()
        >>> FireAnt.food_cost
        f4b3281120d40117b023d6c1a373fde6
        # locked
        >>> fire.armor
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing fire damage
        >>> place = Place('Fire Test1')
        >>> bee = Bee(5)
        >>> place.add_insect(bee)
        >>> place.add_insect(FireAnt())
        >>> bee.action(colony) # attack the FireAnt
        >>> bee.armor
        b911fabd1c66f55e635ee4f72fd9b5c1
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> # Testing fire does damage to all Bees in its Place
        >>> place = Place('Fire Test2')
        >>> bee = Bee(3)
        >>> place.add_insect(bee)
        >>> place.add_insect(Bee(3))
        >>> place.add_insect(FireAnt())
        >>> bee.action(colony) # attack the FireAnt
        >>> len(place.bees)  # How many bees are left?
        11862fc8ebde17878dbcfc9a133b7094
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing FireAnt dies
        >>> place = Place('Fire Test3')
        >>> bee = Bee(1)
        >>> ant = FireAnt()
        >>> place.add_insect(bee)
        >>> place.add_insect(ant)
        >>> bee.action(colony) # attack the FireAnt
        >>> ant.armor
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
        >>> # Testing fire damage is instance attribute
        >>> place = Place('Fire Test4')
        >>> bee = Bee(900)
        >>> buffAnt = ants.FireAnt()
        >>> buffAnt.damage = 500   # Feel the burn!
        >>> place.add_insect(bee)
        >>> place.add_insect(buffAnt)
        >>> bee.action(colony) # attack the FireAnt
        >>> bee.armor  # is damage an instance attribute?
        224199c2ecb34505040bc79e373e3edf
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}