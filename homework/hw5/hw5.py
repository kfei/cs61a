# CS 61A Fall 2014
# Name:
# Login:

def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['♡', '♢', '♤', '♧']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    >>> cards[26:30]
    ['7♤', '7♧', '8♡', '8♢']
    >>> shuffle(cards)[:12]
    ['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
    >>> shuffle(shuffle(cards))[:12]
    ['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
    >>> cards[:12]  # Should not be changed
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'

    half_length = len(cards) // 2
    first, second = cards[:half_length], cards[half_length:]
    ret = []
    for i in range(half_length):
        ret += [first[i], second[i]]

    return ret

def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1
    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])

    def helper():
        nonlocal m, n
        while m <= len(first) and n <= len(second):
            if sum(first[:m]) == sum(second[:n]):
                return
            elif sum(first[:m]) < sum(second[:n]):
                m += 1
            else:
                n += 1
    helper()

    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'

################################
# Linked list data abstraction #
################################

empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

def has_prefix(s, prefix):
    """Returns whether prefix appears at the beginning of linked list s.

    >>> x = link(3, link(4, link(6, link(6, empty))))
    >>> print_link(x)
    3 4 6 6
    >>> has_prefix(x, empty)
    True
    >>> has_prefix(x, link(3, empty))
    True
    >>> has_prefix(x, link(4, empty))
    False
    >>> has_prefix(x, link(3, link(4, empty)))
    True
    >>> has_prefix(x, link(3, link(3, empty)))
    False
    >>> has_prefix(x, x)
    True
    >>> has_prefix(link(2, empty), link(2, link(3, empty)))
    False
    """
    if prefix == empty:
        return True
    elif s == empty:
        return False
    return first(s) == first(prefix) and has_prefix(rest(s), rest(prefix))

def has_sublist(s, sublist):
    """Returns whether sublist appears somewhere within linked list s.

    >>> has_sublist(empty, empty)
    True
    >>> aca = link('A', link('C', link('A', empty)))
    >>> x = link('G', link('A', link('T', link('T', aca))))
    >>> print_link(x)
    G A T T A C A
    >>> has_sublist(x, empty)
    True
    >>> has_sublist(x, link(2, link(3, empty)))
    False
    >>> has_sublist(x, link('G', link('T', empty)))
    False
    >>> has_sublist(x, link('A', link('T', link('T', empty))))
    True
    >>> has_sublist(link(1, link(2, link(3, empty))), link(2, empty))
    True
    >>> has_sublist(x, link('A', x))
    False
    """
    if sublist == empty:
        return True
    elif s ==  empty:
        return False
    return has_prefix(s, sublist) or has_sublist(rest(s), sublist)

def has_61A_gene(dna):
    """Returns whether linked list dna contains the CATCAT gene.

    >>> dna = link('C', link('A', link('T', empty)))
    >>> dna = link('C', link('A', link('T', link('G', dna))))
    >>> print_link(dna)
    C A T G C A T
    >>> has_61A_gene(dna)
    False
    >>> end = link('T', link('C', link('A', link('T', link('G', empty)))))
    >>> dna = link('G', link('T', link('A', link('C', link('A', end)))))
    >>> print_link(dna)
    G T A C A T C A T G
    >>> has_61A_gene(dna)
    True
    >>> has_61A_gene(end)
    False
    """
    cat = link('C', link('A', link('T', empty)))
    catcat = link('C', link('A', link('T', cat)))

    return has_sublist(dna, catcat)

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    attempts = []
    def withdraw(amount, pwd):
        nonlocal balance, attempts
        if len(attempts) == 3:
            return "Your account is locked. Attempts: %s" % attempts

        if pwd != password:
            attempts.append(pwd)
            return 'Incorrect password'

        if amount > balance:
            return 'Insufficient funds'

        balance -= amount
        return balance

    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    test = withdraw(0, old_password)
    if type(test) == str:
        return test

    def joint_withdraw(amount, pwd):
        if pwd == old_password or pwd == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, pwd)

    return joint_withdraw


######################
# Challenge problems #
######################

def triangle_area(a, b, h):
    """Connect a, b, and h so that a is the area of a triangle with base b and
    height h.

    >>> a, b, h = [connector(n) for n in ('area', 'base', 'height')]
    >>> triangle_area(a, b, h)
    >>> a['set_val']('user', 75.0)
    area = 75.0
    >>> b['set_val']('user', 15.0)
    base = 15.0
    height = 10.0
    """
    "*** YOUR CODE HERE ***"

def squarer(a, b):
    """The constraint that a*a=b.

    >>> x, y = connector('X'), connector('Y')
    >>> s = squarer(x, y)
    >>> x['set_val']('user', 10)
    X = 10
    Y = 100
    >>> x['forget']('user')
    X is forgotten
    Y is forgotten
    >>> y['set_val']('user', 16)
    Y = 16
    X = 4.0
    """
    "*** YOUR CODE HERE ***"

def pythagorean(a, b, c):
    """Connect a, b, and c into a network for the Pythagorean theorem:
    a*a + b*b = c*c

    >>> a, b, c = [connector(name) for name in ('A', 'B', 'C')]
    >>> pythagorean(a, b, c)
    >>> a['set_val']('user', 5)
    A = 5
    >>> c['set_val']('user', 13)
    C = 13
    B = 12.0
    """
    "*** YOUR CODE HERE ***"

def connector(name=None):
    """A connector between constraints.

    >>> celsius = connector('Celsius')
    >>> fahrenheit = connector('Fahrenheit')
    >>> converter(celsius, fahrenheit)

    >>> celsius['set_val']('user', 25)
    Celsius = 25
    Fahrenheit = 77.0

    >>> fahrenheit['set_val']('user', 212)
    Contradiction detected: 77.0 vs 212

    >>> celsius['forget']('user')
    Celsius is forgotten
    Fahrenheit is forgotten

    >>> fahrenheit['set_val']('user', 212)
    Fahrenheit = 212
    Celsius = 100.0
    """
    informant = None  # The source of the current val
    constraints = []  # A list of connected constraints

    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}

    return connector

def inform_all_except(source, message, constraints):
    """Inform all constraints of the message, except source."""
    for c in constraints:
        if c != source:
            c[message]()

def ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b)=a."""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

from operator import add, sub, mul, truediv

def adder(a, b, c):
    """The constraint that a + b = c."""
    return ternary_constraint(a, b, c, add, sub, sub)

def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return ternary_constraint(a, b, c, mul, truediv, truediv)

def constant(connector, value):
    """The constraint that connector = value."""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def converter(c, f):
    """Connect c to f to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


