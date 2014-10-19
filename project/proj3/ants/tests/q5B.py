test = {
  'names': [
    'q5B',
    'qB5',
    '5B',
    'B5'
  ],
  'points': 3,
  'suites': [
    [
      {
        'test': r"""
        >>> # Testing Long/ShortThrower paramters
        >>> short_t = ShortThrower()
        >>> long_t = LongThrower()
        >>> ShortThrower.food_cost
        3
        >>> LongThrower.food_cost
        3
        >>> short_t.armor
        1
        >>> long_t.armor
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
        >>> # Testing LongThrower Inheritance from ThrowerAnt
        >>> def new_action(self, colony):
        ...     raise NotImplementedError()
        >>> def new_throw_at(self, target):
        ...     raise NotImplementedError()
        >>> old_thrower_action = ThrowerAnt.action
        >>> old_throw_at = ThrowerAnt.throw_at
        >>> ThrowerAnt.action = new_action
        >>> test_long = LongThrower()
        >>> passed = 0
        >>> try:
        ...     test_long.action(colony)
        ... except NotImplementedError:
        ...     passed += 1
        >>> ThrowerAnt.action = old_thrower_action
        >>> ThrowerAnt.throw_at = new_throw_at
        >>> test_long = LongThrower()
        >>> try:
        ...     test_long.throw_at(Bee(1))
        ... except NotImplementedError:
        ...     passed += 1
        >>> ThrowerAnt.throw_at = old_throw_at
        >>> passed
        2
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
        >>> # Testing ShortThrower Inheritance from ThrowerAnt
        >>> def new_action(self, colony):
        ...     raise NotImplementedError()
        >>> def new_throw_at(self, target):
        ...     raise NotImplementedError()
        >>> old_thrower_action = ThrowerAnt.action
        >>> old_throw_at = ThrowerAnt.throw_at
        >>> ThrowerAnt.action = new_action
        >>> test_short = ShortThrower()
        >>> passed = 0
        >>> try:
        ...     test_short.action(colony)
        ... except NotImplementedError:
        ...     passed += 1
        >>> ThrowerAnt.action = old_thrower_action
        >>> ThrowerAnt.throw_at = new_throw_at
        >>> test_short = ShortThrower()
        >>> try:
        ...     test_short.throw_at(Bee(1))
        ... except NotImplementedError:
        ...     passed += 1
        >>> ThrowerAnt.throw_at = old_throw_at
        >>> passed
        2
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Test LongThrower Hit
        >>> ant = LongThrower()
        >>> in_range = Bee(2)
        >>> colony.places['tunnel_0_0'].add_insect(ant)
        >>> colony.places["tunnel_0_4"].add_insect(in_range)
        >>> ant.action(colony)
        >>> in_range.armor
        1
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing LongThrower miss
        >>> ant = LongThrower()
        >>> out_of_range = Bee(2)
        >>> colony.places["tunnel_0_0"].add_insect(ant)
        >>> colony.places["tunnel_0_3"].add_insect(out_of_range)
        >>> ant.action(colony)
        >>> out_of_range.armor
        2
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Test ShortThrower hit
        >>> ant = ShortThrower()
        >>> in_range = Bee(2)
        >>> colony.places['tunnel_0_0'].add_insect(ant)
        >>> colony.places["tunnel_0_2"].add_insect(in_range)
        >>> ant.action(colony)
        >>> in_range.armor
        1
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing ShortThrower miss
        >>> ant = ShortThrower()
        >>> out_of_range = Bee(2)
        >>> colony.places["tunnel_0_0"].add_insect(ant)
        >>> colony.places["tunnel_0_3"].add_insect(out_of_range)
        >>> ant.action(colony)
        >>> out_of_range.armor
        2
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing if max_range is looked up in the instance
        >>> ant = ShortThrower()
        >>> ant.max_range = 10   # Buff the ant's range
        >>> colony.places["tunnel_0_0"].add_insect(ant)
        >>> bee = Bee(2)
        >>> colony.places["tunnel_0_6"].add_insect(bee)
        >>> ant.action(colony)
        >>> bee.armor
        1
        """,
        'type': 'doctest'
      }
    ]
  ]
}