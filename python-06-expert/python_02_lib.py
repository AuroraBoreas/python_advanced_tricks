### lib.py only provides classes, and can't see user.py

# class for user.py to assert
class Base:
    def foo(self):
        return 'foo'
    pass

# Catch Building of Classes, method 01
# class Base:
#     def foo(self):
#         return self.bar()

old_bc = __build_class__

# Catch building of classes 01
# def my_bc(*a, **kw):
#     print("my buildclass ->", a, kw)
#     return old_bc(*a, **kw)

# Catch building of classes 02
def my_bc(func, name, base=None, **kw):
    if base is Base:
        print("check if bar method defined")
    if base is not None:
        return old_bc(func, name, base, **kw)
    return old_bc(func, name, **kw)

import builtins
builtins.__build_class__ = my_bc