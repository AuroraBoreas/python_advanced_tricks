import weakref, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def weakref_ref():
    # assume we have an expensive class
    class ExpensiveObj:
        def __del__(self):
            print('(Deleting {}'.format(self))
    
    obj = ExpensiveObj()
    r   = weakref.ref(obj)

    print('obj:', obj)
    print('ref:', r)
    print('r():', r())
    print('deleting obj')
    del obj
    print('r():', r())

    # I need comparison between a normal reference vs weakref.reference to see:
    # - reference count on the obj
    # - prevent garbage collecting
    # TODO: P160

if __name__ == "__main__":
    weakref_ref()