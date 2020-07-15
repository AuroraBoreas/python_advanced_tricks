def addone(number):
    """return *number* + 1

    :param number: a number
    :type number: float or integer
    :return: a number
    :rtype: float or integer

    >>> addone(1)
    2
    >>> addone(-0.1)
    0.9
    >>> addone(10000000)
    10000001
    """
    return number + 1

def square(number):
    """return the square of *number*

    :param number: a number
    :type number: float or integer
    :return: a number
    :rtype: float or integer

    >>> square(3)
    9
    >>> square(-4)
    16
    >>> square(1.2)
    1.44
    """
    return number * number

def sqrt(number):
    """return the squre root of *number*

    :param number: a number which must > 0
    :type number: float or integer
    :return: a number
    :rtype: float
    
    >>> sqrt(4)
    2.0
    >>> sqrt(9)
    3.0
    """
    if number < 0:
        raise ValueError("illegal number")
    return number ** 0.5

def mean(seq):
    """return the mean of *seq*

    :param seq: a list that contains numbers
    :type seq: list
    :return: mean
    :rtype: float

    >>> mean([1, 2, 3])
    2.0
    >>> mean([-1, 0, 1])
    0.0
    >>> mean([10, 20, 30])
    20.0
    """
    return sum(seq) / len(seq)

def mode(seq):
    """return the mode of *seq*

    :param seq: a list that contains numbers
    :type seq: list
    :return: mode
    :rtype: float or integer

    >>> mode([1, 1, 3, 4, 5, 7, 6])
    1
    >>> mode([2, 3, 4, 5, 7, 6, 9, 0, -1, 0, 1, 3, 3, 4])
    3
    """
    return max(set(seq), key=seq.count)

def devsq(seq):
    """return the square deviation of *seq*

    :param seq: a list that contains numbers
    :type seq: list
    :return: square variance
    :rtype: float or integer

    >>> devsq([1, 2, 3, 4])
    5.0
    >>> devsq([3, 4, 5, 4])
    2.0
    """
    m = mean(seq)
    t = 0
    for i in seq:
        t = t + square(i - m)
    return round(t, 6)

def stdev(seq):
    """return the standard deviation of *seq*

    :param seq: a list that contains numbers
    :type seq: list
    :return: standard deviation
    :rtype: float or integer

    >>> stdev([1, 2, 3, 4])
    1.290994
    >>> stdev([3, 4, 5, 4])
    0.816497
    """
    sqdev = devsq(seq)
    dimen = len(seq) - 1
    return round(sqrt(sqdev / dimen), 6)