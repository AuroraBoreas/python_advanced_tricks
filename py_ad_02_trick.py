a = [i**2 for i in range(10) if i%2 == 0]

print(a)
import sys
print(sys.getsizeof(a))
