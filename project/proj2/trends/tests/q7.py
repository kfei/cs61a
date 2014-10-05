test = {
  'names': [
    'q7',
    '7'
  ],
  'params': {
    'doctest': {
      'cache': """
      # Storing original implementations of ADTs
      trends.tweet_adt = (make_tweet, tweet_text, tweet_time, tweet_location)
      trends.tweet_fn_adt = (make_tweet_fn, tweet_text_fn, tweet_time_fn, tweet_location_fn)
      trends.sentiment_adt = (make_sentiment, has_sentiment, sentiment_value)
      trends.position_adt = (make_position, latitude, longitude)
      round5 = lambda args: tuple(round(arg, 5) for arg in args)
      geo.us_states_adt = us_states
      """
    }
  },
  'points': 2,
  'suites': [
    [
      {
        'answer': 'e0f88c90b471237f90e98da46a54f352',
        'choices': [
          'geo_distance',
          'find_state_center',
          'make_position'
        ],
        'locked': True,
        'question': 'What function calculates the distance between two positions?',
        'type': 'concept'
      },
      {
        'answer': 'daee5bcea6287836fd0bb4b8f1006850',
        'choices': [
          'A list of tweet objects',
          'A list of position objects',
          'A dictionary of tweet objects',
          'A dictionary of position objects'
        ],
        'locked': True,
        'question': 'What type of object is the parameter tweets?',
        'type': 'concept'
      },
      {
        'answer': '99ec032ad11b60bd13b53364e87f17bc',
        'choices': [
          'A dictionary whose keys are strings (state names) and values are lists of tweet objects',
          'A dictionary whose keys are strings (state names) and values are tweet objects',
          'A dictionary whose keys are tweet objects and values are strings (state names)',
          'A dictionary whose keys are tweet objects and values are position objects'
        ],
        'locked': True,
        'question': 'What type of object does group_tweets_by_state return?',
        'type': 'concept'
      },
      {
        'never_lock': True,
        'test': """
        >>> sf = trends.make_tweet("welcome to san francisco", None, 38, -122)
        >>> ny = trends.make_tweet("welcome to new york", None, 41, -74)
        >>> two_tweets_by_state = group_tweets_by_state([sf, ny])
        >>> len(two_tweets_by_state)
        2
        >>> california_tweets = two_tweets_by_state['CA']
        >>> len(california_tweets)
        1
        >>> tweet_string(california_tweets[0])
        '"welcome to san francisco" @ (38, -122)'
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'teardown': """
        # restore original tweet adt
        trends.make_tweet, trends.tweet_text, trends.tweet_time, trends.tweet_location = trends.tweet_adt
        """,
        'test': """
        >>> # Testing for abstraction violations
        >>> trends.make_tweet = Tweet
        >>> trends.tweet_text = Tweet.text
        >>> trends.tweet_time = Tweet.time
        >>> trends.tweet_location = Tweet.location
        >>> group_tweets_by_state = trends.group_tweets_by_state
        >>> sf = trends.make_tweet("welcome to san francisco", None, 38, -122)
        >>> ny = trends.make_tweet("welcome to new york", None, 41, -74)
        >>> # Begin tests
        >>> two_tweets_by_state = group_tweets_by_state([sf, ny])
        >>> len(two_tweets_by_state)
        2
        >>> california_tweets = two_tweets_by_state['CA']
        >>> len(california_tweets)
        1
        >>> ak_1 = trends.make_tweet("came to find my rubber ducky *o*", None, 100, 8)
        >>> ak_2 = trends.make_tweet("couldn't find one :((((( such sadness", None, 90, 10)
        >>> me_1 = trends.make_tweet("i heard that rubber duckies were made here!", None, 50, -74)
        >>> me_2 = trends.make_tweet("they put ducks in clam chowder! >.<", None, 55, -73)
        >>> two_tweets_by_state = group_tweets_by_state([ak_1, ak_2, me_1, me_2])
        >>> len(two_tweets_by_state)
        2
        >>> alaska_tweets = two_tweets_by_state['AK']
        >>> len(alaska_tweets)
        2
        >>> maine_tweets = two_tweets_by_state['ME']
        >>> len(maine_tweets)
        2
        """,
        'type': 'doctest'
      }
    ]
  ]
}