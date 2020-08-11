import functools, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from typing import Any

@functools.singledispatch
def myfunc(arg: Any):
    print('default myfunc({!r})'.format(arg))
@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))
@myfunc.register(list)
def myfunc_list(arg):
    print('myrfunc_list()')
    for item in arg:
        print(' {}'.format(item))

@addBreaker
def functools_singledispatch():
    myfunc('string argument')
    myfunc(1)
    myfunc(2.3)
    myfunc(list('abc'))    

if __name__ == "__main__":
    # using signledispatch to perform function overload
    functools_singledispatch()
