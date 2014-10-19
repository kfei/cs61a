test = {
  'names': [
    'q3',
    '3'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> # Simple test for Place
        >>> exit = Place('Test Exit')
        >>> exit.exit
        39bf9133062430f919b45aa38441a719
        # locked
        # choice: None
        # choice: exit
        # choice: hive
        # choice: colony.queen
        >>> exit.entrance
        39bf9133062430f919b45aa38441a719
        # locked
        # choice: None
        # choice: exit
        # choice: hive
        # choice: colony.queen
        >>> place = Place('Test Place', exit)
        >>> place.exit
        52a90476639bfd566293fe0ceb92146f
        # locked
        # choice: None
        # choice: exit
        # choice: hive
        # choice: colony.queen
        # choice: place
        >>> exit.entrance
        2d02cc78eb2a9ec7632d5858754a9bc8
        # locked
        # choice: None
        # choice: exit
        # choice: hive
        # choice: colony.queen
        # choice: place
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing if entrances are properly initialized
        >>> passed = True
        >>> for entrance in colony.bee_entrances:
        ...     place = entrance
        ...     while place:
        ...         passed = passed and (place.entrance is not None)
        ...         place = place.exit
        >>> passed
        True
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> # Testing if exits and entrances are different
        >>> passed = True
        >>> for place in colony.places.values():
        ...     passed = passed and \
        ...              (place is not place.exit) and \
        ...              (place is not place.entrance)
        ...     if place.exit and place.entrance:
        ...         passed = passed and (place.exit is not place.entrance)
        >>> passed
        True
        """,
        'type': 'doctest'
      }
    ]
  ]
}