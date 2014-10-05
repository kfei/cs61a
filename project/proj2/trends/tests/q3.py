test = {
  'names': [
    'q3',
    '3'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': """
        >>> positive = make_sentiment(0.2)
        >>> neutral = make_sentiment(0)
        >>> unknown = make_sentiment(None)
        >>> has_sentiment(positive)
        True
        >>> has_sentiment(neutral)
        True
        >>> has_sentiment(unknown)
        False
        >>> sentiment_value(positive)
        0.2
        >>> sentiment_value(neutral)
        0
        """,
        'type': 'doctest'
      }
    ]
  ]
}