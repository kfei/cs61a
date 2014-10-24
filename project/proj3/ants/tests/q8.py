test = {
  'names': [
    'q8',
    '8'
  ],
  'params': {
    'doctest': {
      'setup': r"""
      place = Place("TestProblem8")
      bodyguard = BodyguardAnt()
      bodyguard2 = BodyguardAnt()
      test_ant = Ant()
      test_ant2 = Ant()
      harvester = HarvesterAnt()
      """
    }
  },
  'points': 5,
  'suites': [
    [
      {
        'test': r"""
        >>> # Testing BodyguardAnt parameters
        >>> bodyguard = BodyguardAnt()
        >>> BodyguardAnt.food_cost
        4
        >>> bodyguard.armor
        2
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing BodyguardAnt starts off empty
        >>> bodyguard.ant
        None
        >>> bodyguard.action(colony)
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing BodyguardAnt contain_ant
        >>> bodyguard.contain_ant(test_ant)
        >>> bodyguard.ant
        test_ant
        # choice: test_ant
        # choice: bodyguard
        # choice: None
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing BodyguardAnt container
        >>> bodyguard.container
        True
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing normal Ant container is false
        >>> test_ant.container
        False
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing bodyguard.can_contain returns True on non-containers
        >>> bodyguard.can_contain(test_ant)
        True
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing normal_ant.can_contain returns False
        >>> test_ant.can_contain(test_ant2)
        False
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing bodyguard.can_contain returns False on otherbodyguards
        >>> bodyguard.can_contain(bodyguard2)
        False
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing bodyguard.can_contain returns False once it is already containing
        >>> bodyguard.contain_ant(test_ant)
        >>> bodyguard.can_contain(test_ant2)
        False
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing modified add_insect test 1
        >>> place.add_insect(bodyguard)
        >>> place.add_insect(test_ant)
        >>> bodyguard.ant is test_ant
        True
        >>> place.ant is bodyguard
        True
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing modified add_insect test 2
        >>> place.add_insect(test_ant)
        >>> place.add_insect(bodyguard)
        >>> bodyguard.ant is test_ant
        True
        >>> place.ant is bodyguard
        True
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing modified add_insect test 3
        >>> place.add_insect(bodyguard)
        >>> place is bodyguard.place
        True
        >>> passed = False
        >>> try:
        ...     place.add_insect(bodyguard2)  # can't add bodyguard in another bodyguard
        ... except AssertionError:
        ...     passed = True
        >>> passed
        True
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing modified add_insect test 4
        >>> place.add_insect(bodyguard)
        >>> place.add_insect(test_ant)
        >>> passed = False
        >>> try:
        ...     place.add_insect(test_ant2)  # can't add third ant
        ... except AssertionError:
        ...     passed = True
        >>> passed
        True
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing what happens if bodyguard ant perishes
        >>> place.add_insect(bodyguard)
        >>> place.add_insect(test_ant)
        >>> bodyguard.reduce_armor(bodyguard.armor)
        >>> place.ant is test_ant
        True
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing bodyguard performs contained ant's action
        >>> food = colony.food
        >>> bodyguard.contain_ant(harvester)
        >>> bodyguard.action(colony)   # should do harvester's action
        >>> colony.food
        food + 1
        # choice: food + 1
        # choice: food
        # choice: 0
        # choice: 1
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing bodyguard performs thrower's action
        >>> ant = ThrowerAnt()
        >>> bee = ants.Bee(2)
        >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
        >>> colony.places["tunnel_0_0"].add_insect(ant)
        >>> colony.places["tunnel_0_3"].add_insect(bee)
        >>> bodyguard.action(colony)
        >>> bee.armor
        1
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing removing a bodyguard doesn't remove contained ant
        >>> place = colony.places['tunnel_0_0']
        >>> bodyguard = BodyguardAnt()
        >>> test_ant = Ant(1)
        >>> place.add_insect(bodyguard)
        >>> place.add_insect(test_ant)
        >>> colony.remove_ant('tunnel_0_0')
        >>> place.ant is test_ant
        True
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing bodyguarded ant keeps instance attributes
        >>> test_ant = Ant()
        >>> def new_action( colony):
        ...     test_ant.armor += 9000
        >>> test_ant.action = new_action
        >>> place = colony.places['tunnel_0_0']
        >>> bodyguard = BodyguardAnt()
        >>> place.add_insect(test_ant)
        >>> place.add_insect(bodyguard)
        >>> place.ant.action(colony)
        >>> place.ant.ant.armor
        9001
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing if we can construct a container besides BodyGuard
        >>> ant = ThrowerAnt()
        >>> ant.container = True
        >>> ant.ant = None
        >>> ant.can_contain(ThrowerAnt())
        True
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing container can contain a special non-container bodyguard
        >>> bodyguard = BodyguardAnt()
        >>> mod_guard = BodyguardAnt()
        >>> mod_guard.container = False
        >>> bodyguard.can_contain(mod_guard)
        True
        """,
        'type': 'doctest'
      }
    ]
  ]
}