# CS 61A Fall 2014
# Name:
# Login:


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    if a == b and b == c:
        return False
    if a == b or b == c or c == a:
        return True
    else:
        return False


def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    def hailstone(n, match):
        if n == match:
            return True
        if n == 1:
            return False
        elif n % 2 == 0:
            return hailstone(n / 2, match)
        else:
            return hailstone(3 * n + 1, match)

    return hailstone(a, b) or hailstone(b, a)


def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    assert perimeter % 2 == 0, "Perimeter is not even!"

    def difference(h, w):
        return abs((h / w) - (w / h - 1))

    h = 1
    ret, min_difference = h, difference(h, perimeter / 2 - h)
    while h < perimeter / 4:
        w = perimeter / 2 - h
        if difference(h, w) < min_difference:
            ret, min_difference = h, difference(h, w)
        h += 1

    return ret
