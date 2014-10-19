test = {
  'names': [
    'q4A',
    'qA4',
    '4A',
    'A4'
  ],
  'points': 2,
  'suites': [
    [
      {
        'answer': 'Always; after adding the insect, reduce its armor to 0 if it is not watersafe',
        'choices': [
          'Always; after adding the insect, reduce its armor to 0 if it is not watersafe',
          'Only if the insect is watersafe; if it is not watersafe, reduce its armor to 0',
          'Only if the insect is watersafe; if it is not watersafe, remove the insect from the place',
          'Never; no insect can be placed in a Water Place'
        ],
        'question': 'When should an insect be added to a Water Place?',
        'type': 'concept'
      },
      {
        'answer': 'class attribute',
        'choices': [
          'class attribute',
          'instance attribute',
          'local attribute',
          'global attribute'
        ],
        'question': 'What type of attribute should "watersafe" be?',
        'type': 'concept'
      },
      {
        'answer': 'reduce_armor, in the Insect class',
        'choices': [
          'reduce_armor, in the Insect class',
          'remove_insect, in the Place class',
          'sting, in the Bee class',
          'action, in the Insect class',
          'remove_ant, in the AntColony class'
        ],
        'question': r"""
        What method deals damage to an Insect and removes it from
        its Place? (You should use this method in your code.)
        """,
        'type': 'concept'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing water with soggy (non-watersafe) bees
        >>> test_ants = [Bee(1000000), HarvesterAnt(), Ant(), ThrowerAnt()]
        >>> test_ants[0].watersafe = False # Make Bee non-watersafe
        >>> test_water = Water('Water Test1')
        >>> passed = True
        >>> for test_ant in test_ants:
        ...    test_water.add_insect(test_ant)
        ...    passed = passed and \
        ...             test_ant is not test_water.ant and \
        ...             test_ant.armor == 0
        >>> passed
        True
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing water with watersafe bees
        >>> test_bee = Bee(1)
        >>> test_water = Water('Water Test2')
        >>> test_water.add_insect(test_bee)
        >>> test_bee.armor
        1
        >>> test_bee in test_water.bees
        True
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'never_lock': True,
        'teardown': 'Place.add_insect = old_add_insect',
        'test': r"""
        >>> # Testing water inheritance
        >>> old_add_insect = Place.add_insect
        >>> def new_add_insect(self, insect):
        ...     raise NotImplementedError()
        >>> Place.add_insect = new_add_insect
        >>> test_bee = Bee(1)
        >>> test_water = Water('Water Test3')
        >>> passed = False
        >>> try:
        ...     test_water.add_insect(test_bee)
        ... except NotImplementedError:
        ...     passed = True
        >>> passed
        True
        # explanation: Make sure to use inheritance!
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'teardown': 'Place.add_insect = old_add_insect',
        'test': r"""
        >>> ### Make sure to place the ant before watering it!
        >>> old_add_insect = Place.add_insect
        >>> def new_add_insect(self, insect):
        ...     raise NotImplementedError()
        >>> Place.add_insect = new_add_insect
        >>> test_ant = HarvesterAnt()
        >>> test_water = Water('Water Test4')
        >>> passed = False
        >>> try:
        ...     test_water.add_insect(test_ant)
        ... except NotImplementedError:
        ...     passed = True
        >>> passed
        True
        """,
        'type': 'doctest'
      }
    ]
  ]
}