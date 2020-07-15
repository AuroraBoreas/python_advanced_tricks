import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.util import maths
import doctest

if __name__ == "__main__":
    doctest.testmod(m=maths, name="addone")
    doctest.testmod(m=maths, name="square")
    doctest.testmod(m=maths, name="sqrt")
    doctest.testmod(m=maths, name="mean")
    doctest.testmod(m=maths, name="mode")
    doctest.testmod(m=maths, name="devsq")
    doctest.testmod(m=maths, name="stdev")