test = {
  'names': [
    'q9',
    '9'
  ],
  'params': {
    'doctest': {
      'setup': r"""
      def queen_layout(queen, register_place, steps=5):
          "Create a two-tunnel layout with water in the middle of 5 steps."
          for tunnel in range(2):
              exit = queen
              for step in range(steps):
                  place = ants.Water if step == steps//2 else ants.Place
                  exit = place('tunnel_{0}_{1}'.format(tunnel, step), exit)
                  register_place(exit, step == steps-1)
      
      imp.reload(ants)
      hive = ants.Hive(ants.make_test_assault_plan())
      colony = ants.AntColony(None, hive, ants.ant_types(), queen_layout)
      queen = ants.QueenAnt()
      imposter = ants.QueenAnt()
      """
    }
  },
  'points': 5,
  'suites': [
    [
      {
        'test': r"""
        >>> # Testing queen place
        >>> colony_queen = ants.Place('Original Queen Location of the Colony')
        >>> ant_queen = ants.Place('Place given to the QueenAnt')
        >>> queen_place = ants.QueenPlace(colony_queen, ant_queen)
        >>> colony_queen.bees = [ants.Bee(1, colony_queen) for _ in range(3)]
        >>> ant_queen.bees = [ants.Bee(2, colony_queen) for _ in range(4)]
        >>> len(queen_place.bees)
        7
        >>> bee_armor = sum(bee.armor for bee in queen_place.bees)
        >>> bee_armor
        11
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing double damage
        >>> back = ants.ThrowerAnt()
        >>> thrower_damage = back.damage
        >>> front = ants.FireAnt()
        >>> fire_damage = front.damage
        >>> side_back = ants.ThrowerAnt()
        >>> side_front = ants.ThrowerAnt()
        >>> armor, side_armor = 20, 10
        >>> bee, side_bee = ants.Bee(armor), ants.Bee(side_armor)
        >>> colony.places['tunnel_0_0'].add_insect(back)
        >>> colony.places['tunnel_0_2'].add_insect(queen)
        >>> colony.places['tunnel_0_4'].add_insect(bee)
        >>> colony.places['tunnel_1_1'].add_insect(side_back)
        >>> colony.places['tunnel_1_3'].add_insect(side_front)
        >>> colony.places['tunnel_1_4'].add_insect(side_bee)
        >>> # Simulate a battle in Tunnel 0 (contains Queen)
        >>> back.action(colony)
        >>> armor -= thrower_damage  # No doubling until queen's action
        >>> bee.armor # if failed, damage doubled too early
        armor
        >>> queen.action(colony)
        >>> armor -= thrower_damage  # Queen should always deal normal damage
        >>> bee.armor # if failed, Queen damage incorrect
        armor
        >>> bee.action(colony)  # Bee moves forward
        >>> colony.places['tunnel_0_3'].add_insect(front)  # Fire ant added
        >>> back.action(colony)
        >>> armor -= 2 * thrower_damage  # Damage doubled in back
        >>> bee.armor  # if failed, back damage incorrect
        armor
        >>> queen.action(colony)
        >>> armor -= thrower_damage  # Queen should always deal normal damage
        >>> bee.armor # If failed, Queen damage incorrect (2)
        armor
        >>> back.action(colony)
        >>> armor -= 2 * thrower_damage  # Thrower damage still doubled
        >>> bee.armor # Back damage incorrect
        armor
        >>> bee.action(colony)
        >>> armor -= 2 * fire_damage  # Fire damage doubled
        >>> bee.armor # if failed, Fire damage incorrect
        armor
        >>> # Simulate a battle in Tunnel 1 (no Queen)
        >>> side_bee.armor  # if failed, side bee took damage when it shouldn't have
        side_armor
        >>> side_back.action(colony)
        >>> side_armor -= thrower_damage  # Ant in another tunnel: normal damage
        >>> side_bee.armor # If failed, side back damage is incorrect
        side_armor
        >>> side_front.action(colony)
        >>> side_armor -= thrower_damage  # Ant in another tunnel: normal damage
        >>> side_bee.armor # If failed, side front damage is incorrect
        side_armor
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing Game ends when Queen place is infiltrated
        >>> bee = ants.Bee(3)
        >>> colony.places['tunnel_0_1'].add_insect(queen)
        >>> colony.places['tunnel_0_2'].add_insect(bee)
        >>> queen.action(colony)
        >>> len(colony.queen.bees) <= 0 # If failed, Game ended before it should have
        True
        >>> bee.action(colony)
        >>> len(colony.queen.bees) > 0 # Game should have ended
        True
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing Imposter Queen
        >>> ant = ants.ThrowerAnt()
        >>> bee = ants.Bee(10)
        >>> colony.places['tunnel_0_0'].add_insect(queen)
        >>> colony.places['tunnel_0_1'].add_insect(imposter)
        >>> colony.places['tunnel_0_3'].add_insect(ant)
        >>> colony.places['tunnel_0_4'].add_insect(bee)
        >>> imposter.action(colony)
        >>> bee.armor   # Imposter should not damage bee
        10
        >>> ant.damage  # Imposter should not double damage
        1
        >>> queen.action(colony)
        >>> bee.armor   # Queen should damage bee
        9
        >>> ant.damage  # Queen should double damage
        2
        >>> ant.action(colony)
        >>> bee.armor   # If failed, ThrowerAnt has incorrect damage
        7
        >>> queen.armor   # Long live the Queen
        1
        >>> imposter.armor  # Short-lived imposter
        0
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing bodyguard doubling
        >>> bee = ants.Bee(3)
        >>> guard = ants.BodyguardAnt()
        >>> guard.damage, doubled = 5, 10
        >>> colony.places['tunnel_0_1'].add_insect(queen)
        >>> colony.places['tunnel_0_1'].add_insect(guard)
        >>> colony.places['tunnel_0_2'].add_insect(bee)
        >>> queen.action(colony)
        >>> guard.damage # Bodyguard should be buffed
        doubled
        >>> queen.action(colony)
        >>> bee.armor   # QueenAnt should not have been buffed
        1
        >>> guard.damage  # Bodyguard should not be buffed twice
        doubled
        >>> len(colony.queen.bees) <= 0 # Game should not have ended
        True
        >>> bee.action(colony)
        >>> len(colony.queen.bees) > 0 # Game should have ended
        True
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing bodyguard contain doubling
        >>> guard = ants.BodyguardAnt()
        >>> guard.damage, doubled = 5, 10
        >>> ant = ants.ThrowerAnt()
        >>> ant_doubled = 2 * ant.damage
        >>> colony.places['tunnel_0_1'].add_insect(queen)
        >>> colony.places['tunnel_0_3'].add_insect(guard)
        >>> colony.places['tunnel_0_3'].add_insect(ant)
        >>> queen.action(colony)
        >>> guard.damage # Bodyguard damage should have doubled
        doubled
        >>> ant.damage   # Contained ant should be buffed
        ant_doubled
        >>> queen.action(colony)
        >>> guard.damage # Bodyguard should not be buffed twice
        doubled
        >>> ant.damage   # contained ant should not be buffed twice
        ant_doubled
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'test': r"""
        >>> # Testing Remove
        >>> p0 = colony.places['tunnel_0_0']
        >>> p1 = colony.places['tunnel_0_1']
        >>> p0.add_insect(queen)
        >>> p1.add_insect(imposter)
        >>> p0.remove_insect(queen)
        >>> p1.remove_insect(imposter)
        >>> queen == p0.ant # Queen can't be removed
        True
        >>> p1.ant      # Imposter should have been removed
        None
        >>> queen.action(colony)
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing that game still ends the old-fashioned way
        >>> bee = ants.Bee(3)
        >>> # The bee has an uninterrupted path to the heart of the colony
        >>> colony.places['tunnel_0_1'].add_insect(bee)
        >>> colony.places['tunnel_0_2'].add_insect(queen)
        >>> queen.action(colony)
        >>> bee.action(colony)
        >>> len(colony.queen.bees) <= 0 # Game should not be over
        True
        >>> queen.action(colony)
        >>> bee.action(colony)
        >>> len(colony.queen.bees) > 0 # Game should have ended
        True
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> # Testing if queen will buff newly added ants
        >>> colony.places['tunnel_0_0'].add_insect(ants.ThrowerAnt())
        >>> colony.places['tunnel_0_2'].add_insect(queen)
        >>> queen.action(colony)
        >>> # Add ant and buff
        >>> ant = ants.ThrowerAnt()
        >>> colony.places['tunnel_0_1'].add_insect(ant)
        >>> queen.action(colony)
        >>> # Attack a bee
        >>> bee = ants.Bee(3)
        >>> colony.places['tunnel_0_4'].add_insect(bee)
        >>> ant.action(colony)
        >>> bee.armor # Queen should buff new ants
        1
        """,
        'type': 'doctest'
      }
    ]
  ]
}