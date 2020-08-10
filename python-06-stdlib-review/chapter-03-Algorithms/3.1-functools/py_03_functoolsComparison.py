import functools, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@functools.total_ordering
class MyObject:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return self.val == other.val
    def __gt__(self, other):
        return self.val > other.val


@addBreaker
def functools_total_ordering():
    pass

if __name__ == "__main__":
    functools_total_ordering()