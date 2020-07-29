### functions are first-class objects just like str, int, float, list, tuple, dict, set, class etc.

"""
function fact(n) returns n! if n > 1 or 1 if n < 1

    >>> fact(5)
    120
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> fact(0)
    1
    >>> [fact(n) for n in (1, 2, 3, 4, 5)]
    [1, 2, 6, 24, 120]

    >>> ['Chinese', 'English', 'Japanese', 'French'].sort(key=len)
    >>> sorted(['Chinese', 'English', 'Japanese', 'French'], key=len)
    ['French', 'Chinese', 'English', 'Japanese']

    >>> list(map(fact, range(6)))
    [1, 1, 2, 6, 24, 120]
    >>> functools.reduce(lambda x, y: x+y, range(1, 3))
    3
    >>> list(itertools.filterfalse(lambda x: x % 2, range(10)))
    [0, 2, 4, 6, 8]
    >>> tuple(filter(lambda x: x > 1, range(3)))
    (2,)

    >>> sorted(range(10), key=lambda x: x%2==1, reverse=False)
    [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
"""
# functools
import functools
import itertools
# factorial
def fact(n, product=1):
    if n < 0:
        raise ValueError("n must be >= 0")
    # 0! = 1 in math
    if n < 1:
        return product
    return fact(n-1, product * n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()