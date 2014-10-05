"""Functions for reading data from the sentiment dictionary and tweet files."""

import os
import re
import string
import sys
from datetime import datetime
from ucb import main, interact

# Look for data directory
PY_PATH = sys.argv[0]
if PY_PATH.endswith('doctest.py') and len(sys.argv) > 1:
    PY_PATH = sys.argv[1]
DATA_PATH = os.path.join(os.path.dirname(PY_PATH), 'data') + os.sep
if not os.path.exists(DATA_PATH):
    DATA_PATH = 'data' + os.sep

def load_sentiments(path=DATA_PATH + "sentiments.csv"):
    """Read the sentiment file and return a dictionary containing the sentiment
    score of each word, a value from -1 to +1.
    """
    with open(path, encoding='utf8') as sentiment_file:
        scores = [line.split(',') for line in sentiment_file]
        return {word: float(score.strip()) for word, score in scores}

word_sentiments = load_sentiments()

def file_name_for_term(term, unfiltered_name):
    """Return a valid file name for an arbitrary term string."""
    valid_characters = '-_' + string.ascii_letters + string.digits
    no_space_lower = term.lower().replace(' ', '_')
    valid_only = [c for c in no_space_lower if c in valid_characters]
    return ''.join(valid_only) + '_' +  unfiltered_name

def generate_filtered_file(unfiltered_name, term):
    """Return the path to a file containing tweets that match term, generating
    that file if necessary.
    """
    filtered_path = DATA_PATH + file_name_for_term(term, unfiltered_name)
    if not os.path.exists(filtered_path):
        msg = 'Generating filtered tweets file for "{0}" using tweets from {1}'
        print(msg.format(term, unfiltered_name))
        r = re.compile('\W' + term + '\W', flags=re.IGNORECASE)
        with open(filtered_path, mode='w', encoding='utf8') as out:
            with open(DATA_PATH + unfiltered_name, encoding='utf8') as full:
                matches = [line for line in full if term in line.lower()]
            for line in matches:
                if r.search(line):
                    out.write(line)
            print('Wrote {}.'.format(filtered_path))
    return filtered_path

def tweet_from_line(line, make_tweet):
    """Parse a line and call make_tweet on its contents."""
    loc, _, time_text, text = line.strip().split("\t")
    time = datetime.strptime(time_text, '%Y-%m-%d %H:%M:%S')
    lat, lon = [float(x) for x in loc[1:-1].split(',')]
    return make_tweet(text.lower(), time, lat, lon)

def load_tweets(make_tweet, term='cali', file_name='tweets2014.txt'):
    """Return the list of tweets in file_name that contain term.

    Arguments:
    make_tweet -- a constructor function that takes four arguments:
      1) a string containing the words in the tweet
      2) a datetime.datetime object representing the time of the tweet
      3) a longitude coordinate
      4) a latitude coordinate
    """
    filtered_path = generate_filtered_file(file_name, term)
    with open(filtered_path, encoding='utf8') as tweets:
        return [tweet_from_line(line, make_tweet) for line in tweets
                if len(line.strip().split("\t")) >= 4]
