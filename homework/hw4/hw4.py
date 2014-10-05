# CS 61A Fall 2014
# Name:
# Login:

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert 0 < lower_bound(y) or uppder_bound(y) < 0
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
""" a, b = interval(99, 101), interval(99, 101) """

def multiple_references_explanation():
    exp = """ Yes. Since interval is an uncertain value, the more times it
          has been referenced, the larger error bound it will produced. """
    return exp

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    def f(t):
        return a * t * t + b * t + c

    extreme_point = -b / (2 * a)
    extreme_f = f(extreme_point)
    lower_f = f(lower_bound(x))
    upper_f = f(upper_bound(x))

    if lower_bound(x) <= extreme_point <= upper_bound(x):
        return interval(min(lower_f, upper_f, extreme_f),
                        max(lower_f, upper_f, extreme_f))
    else:
        return interval(min(lower_f, upper_f), max(lower_f, upper_f))

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """

    # Define f, df and ddf with coefficients c
    def f(t):
        order, ret = len(c), c[0]
        while order > 1:
            ret += c[order - 1] * pow(t, order - 1)
            order -= 1
        return ret

    def df(t):
        order, ret = len(c) - 1, c[1]
        while order > 1:
            ret += order * c[order] * pow(t, order - 1)
            order -= 1
        return ret

    def ddf(t):
        order, ret = len(c) - 2, 2 * c[2]
        while order > 1:
            ret += order * (order + 1) * c[order + 1] * pow(t, order - 1)
            order -= 1
        return ret

    # Define Newton's Method
    def improve(update, close, guess):
        while not close(guess):
            guess = update(guess)
        return guess

    def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update

    def approx_eq(x, tolerance=1e-5):
        return abs(df(x)) < tolerance

    def middle(x):
        return (lower_bound(x) + upper_bound(x)) / 2

    # Define a function which returns zero of g within interval x
    def find_zero(g, x):
        lower = lower_bound(x)
        upper = upper_bound(x)
        if g(lower) * g(upper) <= 0:
            # Now call Newton's Method to compute the zero
            zero = improve(newton_update(df, ddf), approx_eq, middle(x))
            return [round(zero, 5)]
        else:
            return []

    # Slice the interval x into len(c) sub-intervals
    step = (upper_bound(x) - lower_bound(x)) / len(c)
    extreme_points = []
    for i in range(len(c)):
        lower = lower_bound(x) + i * step
        upper = lower + step
        extreme_points += find_zero(df, interval(lower, upper))

    extremas = [f(t) for t in extreme_points]
    boundary_values = [f(lower_bound(x)), f(upper_bound(x))]
    all_possibles = extremas + boundary_values

    return interval(min(all_possibles), max(all_possibles))

    """ Note that I'm not sure this approximation works for all polynomials
    over all intervals (though I think it will), just an implementation that
    passes the doctests. Still looking for a mathematically better solution.
    """
