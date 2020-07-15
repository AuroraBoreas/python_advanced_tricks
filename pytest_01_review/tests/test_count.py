a = list("hello world!")
print(a.count('e'))

b = set(a)
print(max(b, key=a.count))

# or collections.Counter
import collections
c = collections.Counter(a)
print(c.most_common(1)[0][0])