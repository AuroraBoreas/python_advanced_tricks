def g(n):
    for i in range(n):
        yield i

# result = g(5)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

### generator not only yield result, but yiled 'control'
for i in g(10):
    print(i)

def first():
    print("first")
def second():
    print("second")
def last():
    print("last")

def api():
    first()
    yield
    second()
    yield
    last()
# this api must be sequential first -> second -> last
