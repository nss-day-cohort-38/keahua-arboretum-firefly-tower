from animals import Animal
from interfaces import ITerrestrial, IWalking

class GoldDustDayGecko(Animal, ITerrestrial, IWalking):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        IWalking.__init__(self)
        self.name = name
        self.species = "Gold Dust Day Gecko"
        self.min_release_age = 2
        self.age = age
        self.prey = [ "flies", "ants" ]
        self.tolerate_shade = True

    def feed(self, prey):
        if prey in self.prey:
            print(f'The gecko ate {prey} for a meal')
        else:
            print(f'The gecko rejects the {prey}')

    def move(self):
        print(f"The {self.species} walks")

    def __str__(self):
        return f'Gecko {self.id}'