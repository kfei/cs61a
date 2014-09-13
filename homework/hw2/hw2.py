# CS 61A Fall 2014
# Name:
# Login:

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    def ret(x):
        if x < 0:
            return f(x)
        else:
            return g(x)
    return ret

def intersects(f, x):
    """Returns a function that returns whether f intersects g at x.

    >>> at_three = intersects(square, 3)
    >>> at_three(triple) # triple(3) == square(3)
    True
    >>> at_three(increment)
    False
    >>> at_one = intersects(identity, 1)
    >>> at_one(square)
    True
    >>> at_one(triple)
    False
    """
    def ret(g):
        if g(x) == f(x):
            return True
        return False
    return ret

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    def nth(x):
        i = n # Or specify a nonlocal
        while i > 0:
            x = f(x)
            i -= 1
        return x
    return nth

###################
# Church Numerals #
###################

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    def ret(x):
        return f(x)
    return ret

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    def ret(x):
        return f(f(x))
    return ret

three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    def increase(x):
        assert x >= 0
        if x == 0:
            return 1
        else:
            return x + 1

    return n(increase)(0)

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    def ret(f):
        def _add(x):
            return m(f)(x) + n(f)(x)
        return _add
    return ret

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    def ret(f):
        return m(n(f))
    return ret

def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    return n(m)
