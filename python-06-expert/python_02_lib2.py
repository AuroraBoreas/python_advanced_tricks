# Catch building of subclass, method 02
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if not 'bar' in body:
            raise TypeError("bad user class")
        print("BaseMeta.__new__", cls, name, bases, body)
        return super().__new__(cls, name, bases, body)
    
class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
    def __init_subclass__(cls, *a, **kw):
        print('init_subclass ->', a, kw)
        return super().__init_subclass__(cls, *a, **kw)