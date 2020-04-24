from animals import Animal
from interfaces import ITerrestrial, ISwimming, IWalking

class NeneGoose(Animal, ITerrestrial, ISwimming, IWalking):
    instances = []

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        ISwimming.__init__(self)
        IWalking.__init__(self)
        self.instances.append(self)
        self.name = name
        self.species = "Nene Goose"
        self.min_release_age = 7
        self.age = age
        self.prey = [ "grass", "plant", "leaves" ]
        self.tolerate_sun = True

    def feed(self, prey):
        if prey in self.prey:
            print(f'{self.name} the {self.species} ate {prey} for a meal')
        else:
            print(f'{self.name} the {self.species} rejects the {prey}')

    def walk(self):
        print(f"{self.species} walks")

    def swim(self):
        print(f"The {self.species} swims")