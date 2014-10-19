test = {
  'names': [
    'q4B',
    'qB4',
    'B4',
    '4B'
  ],
  'points': 2,
  'suites': [
    [
      {
        'answer': 'random_or_none, defined in ant.py',
        'choices': [
          'random_or_none, defined in ant.py',
          'random.random(), defined in the "random" module',
          'getitem, defined in the "operators" module'
        ],
        'question': 'What function selects a random bee from a list of bees?',
        'type': 'concept'
      },
      {
        'test': r"""
        >>> # Testing nearest_bee
        >>> thrower = ThrowerAnt()
        >>> colony.places['tunnel_0_0'].add_insect(thrower)
        >>> place = colony.places['tunnel_0_0']
        >>> near_bee = Bee(2)
        >>> far_bee = Bee(2)
        >>> colony.places["tunnel_0_3"].add_insect(near_bee)
        >>> colony.places["tunnel_0_6"].add_insect(far_bee)
        >>> hive = colony.hive
        >>> thrower.nearest_bee(hive)
        near_bee
        # choice: near_bee
        # choice: far_bee
        >>> thrower.action(colony)    # Attack!
        >>> near_bee.armor            # Should do 1 damage
        1
        >>> thrower.place             # Don't change self.place!
        place
        # choice: place
        # choice: hive
        # choice: colony.queen
        # choice: None
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing Nearest bee not in the hive
        >>> thrower = ThrowerAnt()
        >>> colony.places["tunnel_0_0"].add_insect(thrower)
        >>> hive = colony.hive
        >>> bee = Bee(2)
        >>> hive.add_insect(bee)       # adding a bee to the hive
        >>> thrower.nearest_bee(hive)  # bee or None ?
        None
        # choice: None
        # choice: bee
        # choice: thrower
        # choice: hive
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Test that ThrowerAnt attacks bees on its own square
        >>> thrower = ThrowerAnt()
        >>> colony.places['tunnel_0_0'].add_insect(thrower)
        >>> near_bee = Bee(2)
        >>> colony.places["tunnel_0_0"].add_insect(near_bee)
        >>> thrower.nearest_bee(colony.hive)   # near_bee or None ?
        near_bee
        # choice: near_bee
        # choice: None
        # choice: thrower
        # choice: hive
        >>> thrower.action(colony)   # Attack!
        >>> near_bee.armor           # should do 1 damage
        1
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing ThrowerAnt chooses a random target
        >>> thrower = ThrowerAnt()
        >>> colony.places["tunnel_0_0"].add_insect(thrower)
        >>> bee1 = Bee(1001)
        >>> bee2 = Bee(1001)
        >>> colony.places["tunnel_0_3"].add_insect(bee1)
        >>> colony.places["tunnel_0_3"].add_insect(bee2)
        >>> # Throw 1000 times. The first bee should take ~1000*1/2 = ~500 damage,
        >>> # and have ~501 remaining.
        >>> for _ in range(1000):
        ...     thrower.action(colony)
        >>> # Test if damage to bee1 is within 6 standard deviations (~95 damage)
        >>> # If bees are chosen uniformly, this is true 99.9999998% of the time.
        >>> def dmg_within_tolerance():
        ...     return abs(bee1.armor-501) < 95
        >>> dmg_within_tolerance()
        True
        """,
        'type': 'doctest'
      }
    ]
  ]
}