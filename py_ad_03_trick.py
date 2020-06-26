import sys
#range
a = [i for i in range(10_000)]
print(sys.getsizeof(a))
#list comprehension
a = range(10_000)
print(sys.getsizeof(a))
