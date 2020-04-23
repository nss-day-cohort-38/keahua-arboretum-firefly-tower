from animals import Animal
from interfaces import IFreshwater, ISwimming

class Kikakapu(Animal, IFreshwater, ISwimming):

    def __init__(self, age, name):
        Animal.__init__(self)
        IFreshwater.__init__(self)
        ISwimming.__init__(self)
        self.name = name
        self.species = "Kikakapu"
        self.min_release_age = 1
        self.age = age
        self.prey = { "Trout", "Mackarel", "Salmon", "Sardine" }
        self.tolerate_stagnant = True

    def feed(self, prey):
        if prey in self.prey:
            print(f'The butterfly fish ate {prey} for a meal')
        else:
            print(f'The butterfly fish rejects the {prey}')

    def move(self):
        print(f"The {self.species} swims")

    def __str__(self):
        return f'Kikakapu {self.id}'