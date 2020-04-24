from animals import Animal
from interfaces import ISaltwater, ISwimming

class Ulae(Animal, ISaltwater, ISwimming):

    def __init__(self, age, name):
        Animal.__init__(self)
        ISaltwater.__init__(self)
        ISwimming.__init__(self)
        self.name = name
        self.species = "Ulae"
        self.min_release_age = 1
        self.age = age
        self.prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    def feed(self, prey):
        if prey in self.prey:
            print(f'The lizard fish ate {prey} for a meal')
        else:
            print(f'The lizard fish rejects the {prey}')

    def move(self):
        print(f"The {self.species} swims")