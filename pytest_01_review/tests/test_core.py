import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.pkg.core import Animal
import unittest
print(Animal._qty)

class AnimalTestCase(unittest.TestCase):
    def setUp(self):
        self.squirrel = Animal("nick", "squirrel")
        self.dog = Animal("mini", "dog")
        self.cat = Animal("max", "cat")
    def tearDown(self):
        self.squirrel = None
        self.dog = None
        self.cat = None
    def test_qty(self):
        self.assertEqual(Animal._qty, 3*2)
    def test_description(self):
        self.assertEqual(repr(self.squirrel), "name:nick,species:squirrel")
        self.assertEqual(repr(self.dog), "name:mini,species:dog")
        self.assertEqual(repr(self.cat), "name:max,species:cat")

if __name__ == "__main__":
    unittest.main()