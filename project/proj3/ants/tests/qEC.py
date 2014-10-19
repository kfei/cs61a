test = {
  'extra': True,
  'names': [
    'qEC',
    'EC',
    'ec',
    'extra'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> # Testing status parameters
        >>> slow = SlowThrower()
        >>> stun = StunThrower()
        >>> SlowThrower.food_cost
        f4b3281120d40117b023d6c1a373fde6
        # locked
        >>> StunThrower.food_cost
        6e64cd41ecdfe7fd3b99f4395dfd7c25
        # locked
        >>> slow.armor
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
        >>> stun.armor
        d051d778cc59e30ceee412e76d1fdbc4
        # locked
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing Slow
        >>> slow = SlowThrower()
        >>> bee = Bee(3)
        >>> colony.places["tunnel_0_0"].add_insect(slow)
        >>> colony.places["tunnel_0_4"].add_insect(bee)
        >>> slow.action(colony)
        >>> colony.time = 1
        >>> bee.action(colony)
        >>> bee.place.name # SlowThrower should cause slowness on odd turns
        'tunnel_0_4'
        >>> colony.time += 1
        >>> bee.action(colony)
        >>> bee.place.name # SlowThrower should cause slowness on odd turns
        'tunnel_0_3'
        >>> for _ in range(3):
        ...    colony.time += 1
        ...    bee.action(colony)
        >>> bee.place.name
        'tunnel_0_1'
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing Stun
        >>> error_msg = "StunThrower doesn't stun for exactly one turn."
        >>> stun = StunThrower()
        >>> bee = Bee(3)
        >>> colony.places["tunnel_0_0"].add_insect(stun)
        >>> colony.places["tunnel_0_4"].add_insect(bee)
        >>> stun.action(colony)
        >>> bee.action(colony)
        >>> bee.place.name # StunThrower should stun for exactly one turn
        'tunnel_0_4'
        >>> bee.action(colony)
        >>> bee.place.name # StunThrower should stun for exactly one turn
        'tunnel_0_3'
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': r"""
        >>> # Testing if effects stack
        >>> stun = StunThrower()
        >>> bee = Bee(3)
        >>> stun_place = colony.places["tunnel_0_0"]
        >>> bee_place = colony.places["tunnel_0_4"]
        >>> stun_place.add_insect(stun)
        >>> bee_place.add_insect(bee)
        >>> for _ in range(4): # stun bee four times
        ...    stun.action(colony)
        >>> passed = True
        >>> for _ in range(4):
        ...    bee.action(colony)
        ...    if bee.place.name != 'tunnel_0_4':
        ...        passed = False
        >>> passed
        818d43c4eb49bce28d693d249148409c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing multiple stuns
        >>> stun1 = StunThrower()
        >>> stun2 = StunThrower()
        >>> bee1 = Bee(3)
        >>> bee2 = Bee(3)
        >>> colony.places["tunnel_0_0"].add_insect(stun1)
        >>> colony.places["tunnel_0_1"].add_insect(bee1)
        >>> colony.places["tunnel_0_2"].add_insect(stun2)
        >>> colony.places["tunnel_0_3"].add_insect(bee2)
        >>> stun1.action(colony)
        >>> stun2.action(colony)
        >>> bee1.action(colony)
        >>> bee2.action(colony)
        >>> bee1.place.name
        922cc8e76e4df721c3123a518f16b467
        # locked
        >>> bee2.place.name
        6ee2dac456a484e0c52d92382c675744
        # locked
        >>> bee1.action(colony)
        >>> bee2.action(colony)
        >>> bee1.place.name
        ca02366e00a5ed9c798ad31c3bb8a2cb
        # locked
        >>> bee2.place.name
        359065a3eb11a7b754157e3fde96fc93
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> # Testing long effect stack
        >>> stun = StunThrower()
        >>> slow = SlowThrower()
        >>> bee = Bee(3)
        >>> colony.places["tunnel_0_0"].add_insect(stun)
        >>> colony.places["tunnel_0_1"].add_insect(slow)
        >>> colony.places["tunnel_0_4"].add_insect(bee)
        >>> for _ in range(3): # slow bee three times
        ...    slow.action(colony)
        >>> stun.action(colony) # stun bee once
        >>> colony.time = 0
        >>> bee.action(colony) # stunned
        >>> bee.place.name
        0743f00a386a9fdb01a8d03f6cafc604
        # locked
        >>> colony.time = 1
        >>> bee.action(colony) # slowed thrice
        >>> bee.place.name
        0743f00a386a9fdb01a8d03f6cafc604
        # locked
        >>> colony.time = 2
        >>> bee.action(colony) # slowed thrice
        >>> bee.place.name
        6ee2dac456a484e0c52d92382c675744
        # locked
        >>> colony.time = 3
        >>> bee.action(colony) # slowed thrice
        >>> bee.place.name
        6ee2dac456a484e0c52d92382c675744
        # locked
        >>> colony.time = 4
        >>> bee.action(colony) # slowed twice
        >>> bee.place.name
        359065a3eb11a7b754157e3fde96fc93
        # locked
        >>> colony.time = 5
        >>> bee.action(colony) # slowed twice
        >>> bee.place.name
        359065a3eb11a7b754157e3fde96fc93
        # locked
        >>> colony.time = 6
        >>> bee.action(colony) # slowed once
        >>> bee.place.name
        922cc8e76e4df721c3123a518f16b467
        # locked
        >>> colony.time = 7
        >>> bee.action(colony) # no effects
        >>> slow.armor
        11862fc8ebde17878dbcfc9a133b7094
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}