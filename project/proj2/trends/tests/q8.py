test = {
  'names': [
    'q8',
    '8'
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
        'answer': 'keys are strings (state names), values are numbers (average sentiment values)',
        'choices': [
          'keys are strings (state names), values are numbers (average sentiment values)',
          'keys are strings (state names), values are sentiment objects',
          'keys are strings (state names), values are lists of sentiment objects',
          'keys are tweet objects, values are sentiment objects',
          'keys are tweet objects, values are numbers (average sentiment values)'
        ],
        'question': """
        average_sentiments returns a dictionary. What are the keys
        and values of this dictionary?
        """,
        'type': 'concept'
      },
      {
        'answer': 'the state should not be included in the dictionary',
        'choices': [
          'the state should not be included in the dictionary',
          'the state should be included in the dictionary with a value of 0',
          'the state should be included in the dictionary with a value of None',
          'the state should be included in the dictionary with an empty list'
        ],
        'question': 'What should average_sentiments do if a state has no tweets with sentiments?',
        'type': 'concept'
      },
      {
        'answer': 'analyze_tweet_sentiment, which returns a sentiment object',
        'choices': [
          'analyze_tweet_sentiment, which returns a sentiment object',
          'analyze_tweet_sentiment, which returns a number',
          'tweet_words, which returns a list of words',
          'get_word_sentiment, which returns a number',
          'get_word_sentiment, which returns a sentiment object'
        ],
        'question': """
        What function computes the sentiment of a tweet, and what type of
        object does it return?
        """,
        'type': 'concept'
      },
      {
        'never_lock': True,
        'test': """
        >>> # Begin tests
        >>> tweets_by_state = test_functions.make_average_sentiments_tests(make_tweet)
        >>> groups = average_sentiments(tweets_by_state)
        >>> groups['MT']
        -0.08333333333333333
        >>> groups['MI']
        0.325
        >>> groups['FL']
        0.5
        >>> groups['ND']
        0.020833333333333332
        >>> len(groups)
        4
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'teardown': """
        # restore original sentiment adt
        trends.make_sentiment, trends.has_sentiment, trends.sentiment_value = trends.sentiment_adt
        trends.make_tweet, trends.tweet_text, trends.tweet_time, trends.tweet_location = trends.tweet_adt
        """,
        'test': """
        >>> # Testing for abstraction violations
        >>> make_tweet = trends.make_tweet = Tweet
        >>> trends.tweet_text = Tweet.text
        >>> trends.tweet_time = Tweet.time
        >>> trends.tweet_location = Tweet.location
        >>> trends.make_sentiment = Sentiment
        >>> trends.has_sentiment = Sentiment.has_sentiment
        >>> trends.sentiment_value = Sentiment.sentiment_value
        >>> group_tweets_by_state = trends.group_tweets_by_state
        >>> # Begin tests
        >>> tweets_by_state = test_functions.make_average_sentiments_tests(make_tweet)
        >>> groups = average_sentiments(tweets_by_state)
        >>> groups['MT']
        -0.08333333333333333
        >>> groups['MI']
        0.325
        >>> groups['FL']
        0.5
        >>> groups['ND']
        0.020833333333333332
        >>> len(groups)
        4
        """,
        'type': 'doctest'
      }
    ]
  ]
}