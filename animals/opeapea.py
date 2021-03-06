from animals import Animal
from interfaces import ITerrestrial, IFlying

class Opeapea(Animal, ITerrestrial, IFlying):
    instances = []

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        IFlying.__init__(self)
        self.instances.append(self)
        self.name = name
        self.species = "Opeapea"
        self.min_release_age = 5
        self.age = age
        self.prey = [ "ants", "flies", "grass", "plants", "leaves"]
        self.high_elevation = True
        self.tolerate_shade = True

    def feed(self, prey):
        if prey in self.prey:
            print(f'{self.name} the {self.species} ate {prey} for a meal')
        else:
            print(f'{self.name} the {self.species} rejects the {prey}')

    def move(self):
        print(f"The {self.species} flies")