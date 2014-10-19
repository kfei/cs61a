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
        'answer': '0a1ba6fbdd7b538e3579cd509fd4aa28',
        'choices': [
          'random_or_none, defined in ant.py',
          'random.random(), defined in the "random" module',
          'getitem, defined in the "operators" module'
        ],
        'locked': True,
        'question': 'What function selects a random bee from a list of bees?',
        'type': 'concept'
      },
      {
        'locked': True,
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
        fe38a55cb790cbd21e0c461bf76c915b
        # locked
        # choice: near_bee
        # choice: far_bee
        >>> thrower.action(colony)    # Attack!
        >>> near_bee.armor            # Should do 1 damage
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
        >>> thrower.place             # Don't change self.place!
        2d02cc78eb2a9ec7632d5858754a9bc8
        # locked
        # choice: place
        # choice: hive
        # choice: colony.queen
        # choice: None
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing Nearest bee not in the hive
        >>> thrower = ThrowerAnt()
        >>> colony.places["tunnel_0_0"].add_insect(thrower)
        >>> hive = colony.hive
        >>> bee = Bee(2)
        >>> hive.add_insect(bee)       # adding a bee to the hive
        >>> thrower.nearest_bee(hive)  # bee or None ?
        39bf9133062430f919b45aa38441a719
        # locked
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
        'locked': True,
        'test': r"""
        >>> # Test that ThrowerAnt attacks bees on its own square
        >>> thrower = ThrowerAnt()
        >>> colony.places['tunnel_0_0'].add_insect(thrower)
        >>> near_bee = Bee(2)
        >>> colony.places["tunnel_0_0"].add_insect(near_bee)
        >>> thrower.nearest_bee(colony.hive)   # near_bee or None ?
        fe38a55cb790cbd21e0c461bf76c915b
        # locked
        # choice: near_bee
        # choice: None
        # choice: thrower
        # choice: hive
        >>> thrower.action(colony)   # Attack!
        >>> near_bee.armor           # should do 1 damage
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
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