test = {
  'names': [
    'q6B',
    'qB6',
    '6B',
    'B6'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': r"""
        >>> # Testing ScubaThrower parameters
        >>> scuba = ScubaThrower()
        >>> ScubaThrower.food_cost
        5
        >>> scuba.armor
        1
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'teardown': r"""
        ThrowerAnt.action = old_thrower_action
        ThrowerAnt.throw_at = old_throw_at
        """,
        'test': r"""
        >>> # Testing ScubaThrower Inheritance from ThrowerAnt
        >>> def new_action(self, colony):
        ...     raise NotImplementedError()
        >>> def new_throw_at(self, target):
        ...     raise NotImplementedError()
        >>> old_thrower_action = ThrowerAnt.action
        >>> old_throw_at = ThrowerAnt.throw_at
        >>> ThrowerAnt.action = new_action
        >>> test_scuba = ScubaThrower()
        >>> passed = 0
        >>> try:
        ...     test_scuba.action(colony)
        ... except NotImplementedError:
        ...     passed += 1
        >>> ThrowerAnt.action = old_thrower_action
        >>> ThrowerAnt.throw_at = new_throw_at
        >>> test_scuba = ScubaThrower()
        >>> try:
        ...     test_scuba.throw_at(Bee(1))
        ... except NotImplementedError:
        ...     passed += 1
        >>> ThrowerAnt.throw_at = old_throw_at
        >>> passed
        2
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing if ScubaThrower is watersafe
        >>> water = Water('Water')
        >>> ant = ScubaThrower()
        >>> water.add_insect(ant)
        >>> ant.place
        water
        # choice: water
        # choice: None
        # choice: colony.hive
        # choice: colony.queen
        >>> ant.armor
        1
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing ScubaThrower on land
        >>> place1 = colony.places["tunnel_0_0"]
        >>> place2 = colony.places["tunnel_0_4"]
        >>> ant = ScubaThrower()
        >>> bee = Bee(3)
        >>> place1.add_insect(ant)
        >>> place2.add_insect(bee)
        >>> ant.action(colony)
        >>> bee.armor  # ScubaThrower can throw on land
        2
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing ScubaThrower in the water
        >>> water = Water("water")
        >>> water.entrance = colony.places["tunnel_0_1"]
        >>> target = colony.places["tunnel_0_4"]
        >>> ant = ScubaThrower()
        >>> bee = Bee(3)
        >>> water.add_insect(ant)
        >>> target.add_insect(bee)
        >>> ant.action(colony)
        >>> bee.armor  # ScubaThrower can throw in water
        2
        """,
        'type': 'doctest'
      }
    ]
  ]
}