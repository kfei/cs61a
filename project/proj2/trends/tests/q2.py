test = {
  'names': [
    'q2',
    '2'
  ],
  'points': 2,
  'suites': [
    [
      {
        'test': """
        >>> extract_words("anything else.....not my job")
        ['anything', 'else', 'not', 'my', 'job']
        # choice: ['anything', 'else', 'not', 'my', 'job']
        # choice: ['anything', 'else', '.....', 'not', 'my', 'job']
        # choice: ['anything', 'else.....not', 'my', 'job']
        # choice: ['anything', 'else', '.', '.', '.', '.', '.', 'not', 'my', 'job']
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> extract_words('i love my job. #winning')
        ['i', 'love', 'my', 'job', 'winning']
        # choice: ['i', 'love', 'my', 'job', 'winning']
        # choice: ['i', 'love', 'my', 'job.', '#winning']
        # choice: ['i', 'love', 'my', 'job', '.', '#', 'winning']
        # choice: ['i', 'love', 'my', 'job']
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> extract_words('make justin # 1 by tweeting #vma #justinbieber :)')
        ['make', 'justin', 'by', 'tweeting', 'vma', 'justinbieber']
        # choice: ['make', 'justin', 'by', 'tweeting', 'vma', 'justinbieber']
        # choice: ['make', 'justin', '#', '1', 'by', 'tweeting', '#', 'vma', '#', 'justinbieber']
        # choice: ['make', 'justin', '#', '1', 'by', 'tweeting', '#vma', '#justinbieber']
        # choice: ['make', 'justin', '1', 'by', 'tweeting']
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> extract_words("paperclips! they're so awesome, cool, & useful!")
        ['paperclips', 'they', 're', 'so', 'awesome', 'cool', 'useful']
        # choice: ['paperclips', 'they', 're', 'so', 'awesome', 'cool', 'useful']
        # choice: ['paperclips!', "they're", 'so', 'awesome,', 'cool,', 'useful!']
        # choice: ['paperclips!', "they're", 'so', 'awesome', 'cool', '&', 'useful']
        # choice: ['paperclips!', 'they', 'so', 'awesome', 'cool', 'and', 'useful']
        """,
        'type': 'doctest'
      },
      {
        'test': """
        >>> extract_words('@(cat$.on^#$my&@keyboard***@#*')
        ['cat', 'on', 'my', 'keyboard']
        # choice: ['cat', 'on', 'my', 'keyboard']
        # choice: ['@', '(', 'cat', '$', '.', 'on', '^', '#', '$', 'my', '&', '@', 'keyboard', '***', '@', '#', '*']
        # choice: ['catonmykeyboard']
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'never_lock': True,
        'test': """
        >>> extract_words("This.is separated!by@only#non$letter%characters^so&you*need(to)use-white+listing{instead}of black/listing:or'else<you'll>get~the wrong answer")
        ['This', 'is', 'separated', 'by', 'only', 'non', 'letter', 'characters', 'so', 'you', 'need', 'to', 'use', 'white', 'listing', 'instead', 'of', 'black', 'listing', 'or', 'else', 'you', 'll', 'get', 'the', 'wrong', 'answer']
        """,
        'type': 'doctest'
      }
    ]
  ]
}