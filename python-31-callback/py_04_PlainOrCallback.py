"""
what if conditions changes to wholly divied by 19, max=1000?
copy-paste then change conditions inside fibonacci()?

Makes it DRY
"""
from __future__ import print_function

def fibonacci(callback):
    values = []
    while True:
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]

        result = callback(values[-1], 31, 1000000)
        if result[0]:
            return result[-1]
# better
def check_17(n):
    if not n % 17:
        return (True, n)
    if n > 10_000:
        return (True, None)
    return (False,)
# much better
def check_number(n, *args):
    if len(args) < 2:
        args = (17, 10000)
    if not n % args[0]:
        return (True, n)
    if n > args[-1]:
        return (True, None)
    return (False,)

if __name__ == "__main__":
    result = fibonacci(check_number)
    if result != None:
        print(result)