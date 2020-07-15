class Animal:
    _qty = 0
    def __init__(self, name, species):
        self.name    = name
        self.species = species
        Animal._qty += 1
    def sound(self):
        print("woah")
    def __repr__(self):
        return "name:{0},species:{1}".format(self.name, self.species)
    def disposal(self):
        pass