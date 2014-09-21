# Homework url:
# http://inst.eecs.berkeley.edu/~cs61a/fa13/hw/hw3.html

# Q1.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3

    p1, p2, p3 = 3, 2, 1
    i, current = 4, 0
    while i <= n:
        current = p1 + 2 * p2 + 3 * p3
        p1, p2, p3 = current, p1, p2
        i += 1

    return current


# Q2.

def has_seven(k):
    """Has a has_seven
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


# Q3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    # Following is a tree-recursion (2-way) version,
    # which takes too much time when n is large.
    #
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # elif (n - 1) % 7 == 0 or has_seven(n - 1):
    #     return pingpong(n - 2)
    # else:
    #     return 2 * pingpong(n - 1) - pingpong(n - 2)

    # So re-implement a from-bottom-to-top recursion, using a helper fuction.
    def helper(k, direction, ret):
        if k == n:
            return ret + direction
        elif k % 7 == 0 or has_seven(k):
            return helper(k + 1, -direction, ret + direction)
        else:
            return helper(k + 1, direction, ret + direction)

    return helper(1, 1, 0)


# Q4.

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def count_digit(digit, number):
        if number < 10 and number == digit:
            return 1
        elif number < 10 and number != digit:
            return 0
        elif number % 10 == digit:
            return 1 + count_digit(digit, number // 10)
        else:
            return count_digit(digit, number // 10)

    def helper(n):
        if n < 10:
            return 0
        else:
            return count_digit(10 - n % 10, n // 10) + helper(n // 10)

    return helper(n)


# Q5.

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_partitions(number, at_most):
        if number < 0:
            # There is no way to represent a negative number
            return 0
        elif number == 0:
            # There is only one way to represent zero
            return 1
        elif at_most == 0:
            # There is only one way to represent a number using one (2^0)
            return 1
        else:
            # The representation may contains 2^at_most or not
            contains = count_partitions(number - pow(2, at_most), at_most)
            not_contains = count_partitions(number, at_most - 1)
            return contains + not_contains

    def find_at_most(number):
        k = 0
        while pow(2, k) <= number:
            k += 1
        return k - 1

    at_most = find_at_most(amount)

    return count_partitions(amount, at_most)


# Q6.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    # Idea: Pass lambda function to function F as an argument,
    # so that it can be refered within the scope of F in the future.
    return lambda n: (lambda f, v: f(f, v))(lambda f, v: 1 if v == 1 else mul(v, f(f, sub(v, 1))), n)
