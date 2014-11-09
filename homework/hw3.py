# There is only one different question from hw3 (Fall 2013)


def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"

    def print_step(from_pole, to_pole):
        print("Move the top disk from rod %s to rod %s" % (from_pole, to_pole))

    def helper(n, from_pole, by_pole, to_pole):
        if n == 1:
            print_step(from_pole, to_pole)
        # Assume that we already have the solution for disk number n - 1
        else:
            helper(n - 1, from_pole, to_pole, by_pole)
            print_step(from_pole, to_pole)
            helper(n - 1, by_pole, from_pole, to_pole)

    return helper(n, start, start + 1, end)
