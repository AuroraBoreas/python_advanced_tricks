"""A module displays some common statistics

It has the following functionalities.
- generates a list of random integers
- calculates common statistics of the list

Changelog
- v0.0.1, inital release

About
- author: @ZL, 20200715
"""

from lib.util import maths
import random, os, datetime
random.seed = 12345

class RndStatistics:
    """a class generates a list of random integers and calculates common statistics of the list
    note: it's a toy
    """
    __base_dir      = os.path.dirname(__file__)
    __timer         = datetime.datetime.now
    __log_file_name = "log\\log_app.txt"
    __log_file_path = os.path.join(__base_dir, __log_file_name)
    __headers       = "list, mean, mode, devsq, stdev"
    def __init__(self, rndstart=1, rndend=10, n=10):
        """constructs a list of random integers

        :param rndstart: start integer of random integers, defaults to 1
        :type rndstart: int, optional
        :param rndend: end integer of random integers, defaults to 10
        :type rndend: int, optional
        :param n: how many numbers, defaults to 10
        :type n: int, optional
        :raises ValueError: raise illagel numbers when parameters are negative
        """
        if rndstart < 0 or rndend < 0 or n < 0:
            raise ValueError("illegal numbers")
        self._a = [random.randint(rndstart, rndend) for _ in range(n)]
    def __repr__(self):
        fmt = "{0},mean={1},mode={2},devsq={3},stdev={4}"
        return fmt.format(self._a, 
                        maths.mean(self._a),
                        maths.mode(self._a),
                        maths.devsq(self._a),
                        maths.stdev(self._a))
    def log(self):
        """calculates mean, mode, square deviation, and standard deviation(sample)
        """
        with open(self.__log_file_path, 'a+') as f:
            f.writelines("{0:%Y%m%d %H:%M:%S} {1}\n".format(self.__timer(), self.__headers))
            f.writelines("{0}, ".format(self._a))
            f.writelines("{0}, ".format(maths.mean(self._a)))
            f.writelines("{0}, ".format(maths.mode(self._a)))
            f.writelines("{0}, ".format(maths.devsq(self._a)))
            f.writelines("{0}\n".format(maths.stdev(self._a)))
        return

def main():
    n = 10
    for _ in range(n):
        stat = RndStatistics(rndstart=10, rndend=100, n=10)
        print(stat)
        stat.log()

if __name__ == "__main__":
    main()