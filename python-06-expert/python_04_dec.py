### decorator in Python
import time

def activate(flag=True): # decorator factory
    def timer(func): # true decoractor
        def inner(*a, **kw): # decorated function
            if flag:
                start  = time.perf_counter()
                result = func(*a, **kw)
                end    = time.perf_counter()
                print("elapsed: {}".format(end - start))
                return result
            else:
                return func(*a, **kw)
        return inner
    return timer

@activate(False)
def add(x, y):
    return x + y

@activate(True)
def subs(x, y):
    return x - y

a = add(10, 1000)
print(a)
a = subs(10, 1000)
print(a)

