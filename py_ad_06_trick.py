data = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(data), key=data.count))

# or collections.Counter
from collections import Counter

c = Counter(data)
print(c.most_common(3))
