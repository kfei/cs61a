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
        'locked': True,
        'test': r"""
        >>> # Testing BodyguardAnt parameters
        >>> bodyguard = BodyguardAnt()
        >>> BodyguardAnt.food_cost
        f4b3281120d40117b023d6c1a373fde6
        # locked
        >>> bodyguard.armor
        b911fabd1c66f55e635ee4f72fd9b5c1
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing BodyguardAnt starts off empty
        >>> bodyguard.ant
        39bf9133062430f919b45aa38441a719
        # locked
        >>> bodyguard.action(colony)
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing BodyguardAnt contain_ant
        >>> bodyguard.contain_ant(test_ant)
        >>> bodyguard.ant
        2d2a95d0630acc4fa0fceba18ccc35e6
        # locked
        # choice: test_ant
        # choice: bodyguard
        # choice: None
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing BodyguardAnt container
        >>> bodyguard.container
        818d43c4eb49bce28d693d249148409c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing normal Ant container is false
        >>> test_ant.container
        de3faadc88f04fc1b271becbc2bec69a
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> # Testing bodyguard.can_contain returns True on non-containers
        >>> bodyguard.can_contain(test_ant)
        818d43c4eb49bce28d693d249148409c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing normal_ant.can_contain returns False
        >>> test_ant.can_contain(test_ant2)
        de3faadc88f04fc1b271becbc2bec69a
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing bodyguard.can_contain returns False on otherbodyguards
        >>> bodyguard.can_contain(bodyguard2)
        de3faadc88f04fc1b271becbc2bec69a
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing bodyguard.can_contain returns False once it is already containing
        >>> bodyguard.contain_ant(test_ant)
        >>> bodyguard.can_contain(test_ant2)
        de3faadc88f04fc1b271becbc2bec69a
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> # Testing modified add_insect test 1
        >>> place.add_insect(bodyguard)
        >>> place.add_insect(test_ant)
        >>> bodyguard.ant is test_ant
        818d43c4eb49bce28d693d249148409c
        # locked
        >>> place.ant is bodyguard
        818d43c4eb49bce28d693d249148409c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing modified add_insect test 2
        >>> place.add_insect(test_ant)
        >>> place.add_insect(bodyguard)
        >>> bodyguard.ant is test_ant
        818d43c4eb49bce28d693d249148409c
        # locked
        >>> place.ant is bodyguard
        818d43c4eb49bce28d693d249148409c
        # locked
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
        'locked': True,
        'test': r"""
        >>> # Testing what happens if bodyguard ant perishes
        >>> place.add_insect(bodyguard)
        >>> place.add_insect(test_ant)
        >>> bodyguard.reduce_armor(bodyguard.armor)
        >>> place.ant is test_ant
        818d43c4eb49bce28d693d249148409c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing bodyguard performs contained ant's action
        >>> food = colony.food
        >>> bodyguard.contain_ant(harvester)
        >>> bodyguard.action(colony)   # should do harvester's action
        >>> colony.food
        23894480fe872cf30bfe57e847595708
        # locked
        # choice: food + 1
        # choice: food
        # choice: 0
        # choice: 1
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing bodyguard performs thrower's action
        >>> ant = ThrowerAnt()
        >>> bee = ants.Bee(2)
        >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
        >>> colony.places["tunnel_0_0"].add_insect(ant)
        >>> colony.places["tunnel_0_3"].add_insect(bee)
        >>> bodyguard.action(colony)
        >>> bee.armor
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing removing a bodyguard doesn't remove contained ant
        >>> place = colony.places['tunnel_0_0']
        >>> bodyguard = BodyguardAnt()
        >>> test_ant = Ant(1)
        >>> place.add_insect(bodyguard)
        >>> place.add_insect(test_ant)
        >>> colony.remove_ant('tunnel_0_0')
        >>> place.ant is test_ant
        818d43c4eb49bce28d693d249148409c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
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
        6082c7bda5b0cd11f6257d982e4e2826
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> # Testing if we can construct a container besides BodyGuard
        >>> ant = ThrowerAnt()
        >>> ant.container = True
        >>> ant.ant = None
        >>> ant.can_contain(ThrowerAnt())
        818d43c4eb49bce28d693d249148409c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing container can contain a special non-container bodyguard
        >>> bodyguard = BodyguardAnt()
        >>> mod_guard = BodyguardAnt()
        >>> mod_guard.container = False
        >>> bodyguard.can_contain(mod_guard)
        818d43c4eb49bce28d693d249148409c
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}