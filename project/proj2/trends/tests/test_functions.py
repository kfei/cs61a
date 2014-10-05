def pirate_tweets(make_tweet):
    return [
      make_tweet('I am the very model of a modern Major-General'.lower(), None, 43, -84),
      make_tweet("I've information vegetable, animal, and mineral".lower(), None, 58, -112),
      make_tweet('I know the kings of England, and I quote the fights historical'.lower(), None, 49, -104),
      make_tweet('From Marathon to Waterloo, in order categorical'.lower(), None, 19, -87),
      make_tweet("I'm very well acquainted, too, with matters mathematical".lower(), None, 44, -85),
      make_tweet('I understand equations, both the simple and quadratical'.lower(), None, 59, -110),
      make_tweet("About binomial theorem I'm teeming with a lot o' news".lower(), None, 50, -100),
      make_tweet('With many cheerful facts about the square of the hypotenuse'.lower(), None, 15, -87),
      ]

def make_average_sentiments_tests(make_tweet):
    tweets = pirate_tweets(make_tweet) \
        + [make_tweet('This tweet is without a sentiment', None, None, None)] \
        + [make_tweet('This tweet is also without a sentiment', None, None, None) ]
    tweets_by_state = {}
    tweets_by_state['MT'] = [tweets[1], tweets[5]]
    tweets_by_state['MI'] = [tweets[0], tweets[4]]
    tweets_by_state['FL'] = [tweets[3], tweets[7]]
    tweets_by_state['ND'] = [tweets[2], tweets[6]]
    tweets_by_state['AA'] = [tweets[8], tweets[9]]
    return tweets_by_state

# These classes test abstraction violations
class AbstractionViolation(Exception):
    pass

def datatype(obj):
    return type(obj).__name__

# Generic abstract data type
class Abstract(object):
    def __add__(self, other):
        raise AbstractionViolation("Can't add {} object to {}".format(datatype(self), datatype(other)))

    def __radd__(self, other):
        raise AbstractionViolation("Can't add {} object to {}".format(datatype(self), datatype(other)))

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return other is self
        raise AbstractionViolation("Can't use == on {} object and {}".format(datatype(self), datatype(other)))

    def __ne__(self, other):
        if isinstance(other, type(self)):
            return other is not self
        raise AbstractionViolation("Can't use != on {} object and {}".format(datatype(self), datatype(other)))

    def __bool__(self):
        raise AbstractionViolation("Can't use {} object as a boolean".format(datatype(self)))

    def __getitem__(self, index):
        raise AbstractionViolation("Can't use [] notation on {} object".format(datatype(self)))

    def __contains__(self, other):
        raise AbstractionViolation("Can't use contains notation on {} object".format(datatype(self)))

    def __delitem__(self, other):
        raise AbstractionViolation("Can't use del notation on {} object".format(datatype(self)))

    def __iter__(self):
        raise AbstractionViolation("Can't iterate on {} object".format(datatype(self)))

    def __len__(self):
        raise AbstractionViolation("Can't use len notation on {} object".format(datatype(self)))

    def __setitem__(self, key, item):
        raise AbstractionViolation("Can't use setitem notation on {} object".format(datatype(self)))

class Tweet(Abstract):
    def __init__(self, text, time, lat, lon):
        self._text = text
        self._time = time
        self._lat = lat
        self._lon = lon

    def text(self):
        return self._text

    def time(self):
        return self._time

    def location(self):
        import trends
        return trends.make_position(self._lat, self._lon)

class Sentiment(Abstract):
    def __init__(self, value):
        assert value is None or type(value) in (float, int), 'invalid value to sentiment constructor: {}'.format(datatype(value))
        self._value = value

    def sentiment_value(self):
        if type(self) != Sentiment:
            raise AbstractionViolation("Can't call sentiment_value on {}".format(self))
        assert self.has_sentiment(), 'No sentiment value'
        return self._value

    def has_sentiment(self):
        if type(self) != Sentiment:
            raise AbstractionViolation("Can't call has_sentiment on {}".format(self))
        return self._value != None

class Position(Abstract):
    def __init__(self, lat, lon):
        self._lat = lat
        self._lon = lon

    def latitude(self):
        if type(self) != Position:
            raise AbstractionViolation("Can't call latitude on {}".format(self))
        return self._lat

    def longitude(self):
        if type(self) != Position:
            raise AbstractionViolation("Can't call longitude on {}".format(self))
        return self._lon
