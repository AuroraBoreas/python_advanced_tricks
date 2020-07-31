### user.py uses classes provided by lib.py only, and can't change anything in lib.py
from python_02_lib3 import Base

# ensure Base class has 'foo' attribute
assert hasattr(Base, 'foo'), "Base class does NOT have a 'foo' attribute"

# derived class from Base class
class Derived(Base):
    def bar(self):
        return 'bar'