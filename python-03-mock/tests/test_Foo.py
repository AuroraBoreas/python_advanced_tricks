import unittest
from unittest import mock
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.module import Foo

class SomeClass:
    pass

real = SomeClass()
real.method = mock.MagicMock(name='method')
real.method(3, 4, 5, key='value')

class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass
    def closer(self, something):
        something.close()
        
real = ProductionClass()
mck = mock.Mock()
real.closer(mck)
mck.close.assert_called_with()

def some_function():
    instance = Foo()
    return instance.method()

with mock.patch('lib.module.Foo') as mock_Foo:
    instance = mock_Foo.return_value
    instance.method.return_value = 'the result'
    result = some_function()
    assert result == 'the result', 'failed..'