from lib.pkg import core
# from pkg import *

# object: dog
dog = core.Animal("dick", "dog")
dog.sound()
print(dog)
print("Animal instances:",core.Animal._qty)
# object: cat
cat = core.Animal("chat", "cat")
cat.sound()
print(cat)
print("Animal instances:",core.Animal._qty)
# object: squirrel
squirrel = core.Animal("nick", "squirrel")
squirrel.sound()
print(squirrel)
print("Animal instances:",core.Animal._qty)

# inheritance: Dog
class Dog(core.Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species)
        self.legs = legs
    def sound(self):
        print("wan wan!")
    def count_legs(self):
        return self.legs
# object: mydog
mydog = Dog("leftpaw", "dog", 4)
mydog.sound()
print(mydog)
print(mydog.count_legs())
print("Animal instances:",core.Animal._qty)
# dog vs mydog
print(dog == mydog)