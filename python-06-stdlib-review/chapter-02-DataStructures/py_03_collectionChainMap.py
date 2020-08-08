import collections, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def collections_chainmap_read():
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}
    # ! look into the behavior of 'c' ..
    m = collections.ChainMap(a, b)
    # ? 'c' value has been overwritten?
    # A: No
    # ? why not? for example, normal dict value will be overwritten if key(hashable) are same, and its value got updated from latter paris with the same key.
    # A: it's not case in collections.ChainMap(). collections.ChainMap is a class which constructs its dict in sequence of arguments(dict obj) passing into it.
    # that's the reason that 'c' in dict obj(b) is omitted.
    print('Individual Values')
    print('a = {}'.format(m['a']))
    print('b = {}'.format(m['b']))
    print('c = {}'.format(m['c']))
    print()
    print('Keys   = {}'.format(list(m.keys())))
    print('Values = {}'.format(list(m.values())))
    print()
    print('Items:')
    for k, v in m.items():
        print('{} = {}'.format(k, v))
        print()
        print('"d" in m: {}'.format(('d' in m)))


def main():
    collections_chainmap_read()

if __name__ == "__main__":
    main()