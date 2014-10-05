test = {
  'names': [
    'q6',
    '6'
  ],
  'params': {
    'doctest': {
      'cache': """
      # Storing original implementation of ADTs
      trends.position_adt = (make_position, latitude, longitude)
      """
    }
  },
  'points': 1,
  'suites': [
    [
      {
        'answer': 'A position object',
        'choices': [
          'A position object',
          'The latitude and longitude',
          'A list of polygons'
        ],
        'question': 'What type of object does find_state_center return?',
        'type': 'concept'
      },
      {
        'never_lock': True,
        'test': """
        >>> ca = find_state_center(us_states['CA']) # California
        >>> round(latitude(ca), 5)
        37.25389
        >>> round(longitude(ca), 5)
        -119.61439
        >>> hi = find_state_center(us_states['HI']) # Hawaii
        >>> round(latitude(hi), 5)
        20.1489
        >>> round(longitude(hi), 5)
        -156.21763
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'teardown': """
        # restore original position ADT
        trends.make_position, trends.latitude, trends.longitude = trends.position_adt
        geo.make_position, geo.latitude, geo.longitude = trends.position_adt
        """,
        'test': """
        >>> # Testing for abstraction violations
        >>> other = Position, Position.latitude, Position.longitude
        >>> trends.make_position, trends.latitude, trends.longitude = other
        >>> geo.make_position, geo.latitude, geo.longitude = other
        >>> us_states = geo.load_states()
        >>> ca = find_state_center(us_states['CA']) # California
        >>> round(trends.latitude(ca), 5)
        37.25389
        >>> round(trends.longitude(ca), 5)
        -119.61439
        >>> hi = find_state_center(us_states['HI']) # Hawaii
        >>> round(trends.latitude(hi), 5)
        20.1489
        >>> round(trends.longitude(hi), 5)
        -156.21763
        """,
        'type': 'doctest'
      }
    ]
  ]
}