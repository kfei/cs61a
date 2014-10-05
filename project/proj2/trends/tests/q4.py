test = {
  'names': [
    'q4',
    '4'
  ],
  'params': {
    'doctest': {
      'cache': """
      # Storing original implementations of ADTs
      trends.tweet_adt = (make_tweet, tweet_text, tweet_time, tweet_location)
      trends.tweet_fn_adt = (make_tweet_fn, tweet_text_fn, tweet_time_fn, tweet_location_fn)
      trends.sentiment_adt = (make_sentiment, has_sentiment, sentiment_value)
      round5 = lambda args: tuple(round(arg, 5) for arg in args)
      """
    }
  },
  'points': 1,
  'suites': [
    [
      {
        'answer': 'get_word_sentiment',
        'choices': [
          'get_word_sentiment',
          'make_sentiment',
          'sentiment_value',
          'extract_words',
          'make_tweet'
        ],
        'question': """
        What function will take a string (a word) and return
        the associated sentiment?
        """,
        'type': 'concept'
      },
      {
        'answer': 'A sentiment object',
        'choices': [
          'A sentiment object',
          'A number from -1 to 1',
          'A number from -1 to 1, or None if no sentiment',
          'A tweet'
        ],
        'question': 'What type of object does analyze_tweet_sentiment return?',
        'type': 'concept'
      },
      {
        'answer': 'make_sentiment(None)',
        'choices': [
          'make_sentiment(None)',
          '0',
          'sentiment_value(None)'
        ],
        'question': """
        If a tweet has no words with sentiments, what should
        analyze_tweet_sentiment return?
        """,
        'type': 'concept'
      },
      {
        'never_lock': True,
        'test': """
        >>> positive = make_tweet('i love my job. #winning', None, 0, 0)
        >>> negative = make_tweet("saying, 'i hate my job'", None, 0, 0)
        >>> no_sentiment = make_tweet("berkeley golden bears!", None, 0, 0)
        >>> round(sentiment_value(analyze_tweet_sentiment(positive)), 5)
        0.29167
        >>> sentiment_value(analyze_tweet_sentiment(negative))
        -0.25
        >>> has_sentiment(analyze_tweet_sentiment(no_sentiment))
        False
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> trends.make_sentiment = Sentiment
        >>> trends.sentiment_value = Sentiment.sentiment_value
        >>> trends.has_sentiment = Sentiment.has_sentiment
        >>> t1 = trends.make_tweet("Help, I'm trapped in an autograder factory and I can't get out!".lower(), None, 0, 0)
        >>> t2 = trends.make_tweet('The thing that I love about hating things that I love is that I hate loving that I hate doing it.'.lower(), None, 0, 0)
        >>> t3 = trends.make_tweet('Peter Piper picked a peck of pickled peppers'.lower(), None, 0, 0)
        >>> round(trends.sentiment_value(analyze_tweet_sentiment(t1)), 5)
        -0.41667
        >>> trends.sentiment_value(analyze_tweet_sentiment(t2))
        0.075
        >>> trends.has_sentiment(analyze_tweet_sentiment(t3))
        False
        >>> # restore original sentiment adt
        >>> trends.make_sentiment, trends.has_sentiment, trends.sentiment_value = trends.sentiment_adt
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> trends.make_tweet = Tweet
        >>> trends.tweet_text = Tweet.text
        >>> trends.tweet_time = Tweet.time
        >>> trends.tweet_location = Tweet.location
        >>> t1 = trends.make_tweet("Help, I'm trapped in an autograder factory and I can't get out!".lower(), None, 0, 0)
        >>> t2 = trends.make_tweet('The thing that I love about hating things that I love is that I hate loving that I hate doing it.'.lower(), None, 0, 0)
        >>> t3 = trends.make_tweet('Peter Piper picked a peck of pickled peppers'.lower(), None, 0, 0)
        >>> round(trends.sentiment_value(analyze_tweet_sentiment(t1)), 5)
        -0.41667
        >>> trends.sentiment_value(analyze_tweet_sentiment(t2))
        0.075
        >>> trends.has_sentiment(analyze_tweet_sentiment(t3))
        False
        >>> # restore original tweet adt
        >>> trends.make_tweet, trends.tweet_text, trends.tweet_time, trends.tweet_location = trends.tweet_adt
        """,
        'type': 'doctest'
      }
    ]
  ]
}