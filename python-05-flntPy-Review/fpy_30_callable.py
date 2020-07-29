### any object can also behave like funtion when implemented __call__
# random
try:
    import random
except:
    random = None

# a simple class
class BingoCage:
    def __init__(self, items):
        if hasattr(items, '__iter__'):
            self._items = list(items)
            print(self._items)
            random.shuffle(self._items)
        else:
            raise ValueError("items must be an iterable")
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCase')
    def __call__(self):
        return self.pick()

b = BingoCage("hello world! my name is ZL. God bless me!".split())
print(b())
b = BingoCage(range(3)) 
print(b())