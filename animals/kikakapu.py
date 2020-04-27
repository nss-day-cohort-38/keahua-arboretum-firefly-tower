from animals import Animal
from interfaces import IFreshwater, ISwimming

class Kikakapu(Animal, IFreshwater, ISwimming):
    instances = []

    def __init__(self, age, name):
        Animal.__init__(self)
        IFreshwater.__init__(self)
        ISwimming.__init__(self)
        self.instances.append(self)
        self.name = name
        self.species = "Kikakapu"
        self.min_release_age = 1
        self.age = age
        self.prey = [ "trout", "mackarel", "salmon", "sardine" ]
        self.tolerate_stagnant = True

    def feed(self, prey):
        if prey in self.prey:
            print(f'{self.name} the {self.species} ate {prey} for a meal')
        else:
            print(f'{self.name} the {self.species} rejects the {prey}')

    def move(self):
        print(f"The {self.species} swims")