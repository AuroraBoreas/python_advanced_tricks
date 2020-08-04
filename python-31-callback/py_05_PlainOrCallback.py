# iterator in Python
def fibonacci(n):
    values = [1, 1]
    for _ in range(n):
        yield values[-1]
        values.append(values[-1] + values[-2])

n = 100
f = fibonacci(n)
for _ in range(n):
    result = next(f)
    if not result % 17:
        print(result)
    if result > 10_000:
        break