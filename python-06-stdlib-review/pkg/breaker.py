def addBreaker(func):
    def inner(*args, **kwargs):
        Breaker = '\n{:-^50}'
        print(Breaker.format(''))
        func(*args, **kwargs)
    return inner