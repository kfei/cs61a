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
        'locked': True,
        'test': r"""
        >>> # Testing ScubaThrower parameters
        >>> scuba = ScubaThrower()
        >>> ScubaThrower.food_cost
        9120598f73414c1b785655f8e4e2c576
        # locked
        >>> scuba.armor
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
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
        'locked': True,
        'test': r"""
        >>> # Testing if ScubaThrower is watersafe
        >>> water = Water('Water')
        >>> ant = ScubaThrower()
        >>> water.add_insect(ant)
        >>> ant.place
        5d0ff896928a169c628d6a30a01b79f3
        # locked
        # choice: water
        # choice: None
        # choice: colony.hive
        # choice: colony.queen
        >>> ant.armor
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
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
        b911fabd1c66f55e635ee4f72fd9b5c1
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
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
        b911fabd1c66f55e635ee4f72fd9b5c1
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}