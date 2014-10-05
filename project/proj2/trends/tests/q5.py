test = {
  'names': [
    'q5',
    '5'
  ],
  'params': {
    'doctest': {
      'cache': """
      # Storing original implementations of ADTs
      trends.position_adt = (make_position, latitude, longitude)
      """
    }
  },
  'points': 2,
  'suites': [
    [
      {
        'answer': 'The latitude, longitude, and area',
        'choices': [
          'The latitude, longitude, and area',
          'The area of the polygon',
          'A position object with the calculated latitude and longitude',
          'latitude and longitude'
        ],
        'question': 'What should find_centroid return?',
        'type': 'concept'
      },
      {
        'answer': 'x is the latitude, y is the longitude',
        'choices': [
          'x is the latitude, y is the longitude',
          'x is the longitude, y is the latitude'
        ],
        'question': 'The formula on Wikipedia uses variables x and y. What do these represent?',
        'type': 'concept'
      },
      {
        'answer': 'They should be the latitude and longitude of the first position',
        'choices': [
          'They should be the latitude and longitude of the first position',
          'They should both be 0',
          'They should be the latitude and longitude calculated by the formula'
        ],
        'question': """
        If the area of the polygon is 0, what should the
        latitude and longitude be?
        """,
        'type': 'concept'
      },
      {
        'answer': 'After calculating latitude and longitude with the negative area, take the absolute value of the area',
        'choices': [
          'After calculating latitude and longitude with the negative area, take the absolute value of the area',
          'Before calculating latitude and longitude with the negative area, take the absolute value of the area',
          'Leave the area as a negative number',
          'This will never happen given the formula'
        ],
        'question': 'How would you handle a negative area?',
        'type': 'concept'
      },
      {
        'never_lock': True,
        'test': """
        >>> p1, p2, p3 = make_position(1, 2), make_position(3, 4), make_position(5, 0)
        >>> triangle = [p1, p2, p3, p1]  # First vertex is also the last vertex
        >>> round5 = lambda x: round(x, 5) # Rounds floats to 5 digits
        >>> list(map(round5, find_centroid(triangle)))
        [3.0, 2.0, 6.0]
        >>> list(map(round5, find_centroid([p1, p3, p2, p1])))
        [3.0, 2.0, 6.0]
        >>> list(map(float, find_centroid([p1, p2, p1]))) # A zero-area polygon
        [1.0, 2.0, 0.0]
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'teardown': """
        # restore original position adt
        trends.make_position, trends.latitude, trends.longitude = trends.position_adt
        """,
        'test': """
        >>> # Testing for abstraction violations
        >>> make_posiion = trends.make_position = Position
        >>> trends.latitude = Position.latitude
        >>> trends.longitude = Position.longitude
        >>> find_centroid = trends.find_centroid
        >>> make_position = trends.make_position
        >>> p1, p2, p3 = make_position(1, 2), make_position(3, 4), make_position(5, 0)
        >>> triangle = [p1, p2, p3, p1]  # First vertex is also the last vertex
        >>> round5 = lambda x: round(x, 5) # Rounds floats to 5 digits
        >>> list(map(round5, find_centroid(triangle)))
        [3.0, 2.0, 6.0]
        >>> list(map(round5, find_centroid([p1, p3, p2, p1])))
        [3.0, 2.0, 6.0]
        >>> list(map(float, find_centroid([p1, p2, p1]))) # A zero-area polygon
        [1.0, 2.0, 0.0]
        """,
        'type': 'doctest'
      }
    ]
  ]
}