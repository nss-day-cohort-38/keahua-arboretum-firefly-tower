from animals import Animal
from interfaces import IFreshwater, IWalking

class HawaiianHappyFaceSpider(Animal, IFreshwater, IWalking):

    def __init__(self, age, name):
        Animal.__init__(self)
        IFreshwater.__init__(self)
        IWalking.__init__(self)
        self.name = name
        self.species = "Hawaiian Happy Face Spider"
        self.min_release_age = .5
        self.age = age
        self.prey = { "Flies", "Ants" }
        self.tolerate_stagnant = True
        self.tolerate_current = False

    def feed(self, prey):
        if prey in self.prey:
            print(f'The spider ate {prey} for a meal')
        else:
            print(f'The spider rejects the {prey}')

    def move(self):
        print(f"The {self.species} walks")