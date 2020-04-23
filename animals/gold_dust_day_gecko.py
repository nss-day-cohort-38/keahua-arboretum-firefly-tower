from animals import Animal
from interfaces import ITerrestrial, IWalking

class GoldDustDayGecko(Animal, ITerrestrial, IWalking):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        IWalking.__init__(self)
        self.name = name
        self.__species = "Gold Dust Day Gecko"
        self.__min_release_age = 2
        self.age = age
        self.__prey = { "Fly", "Ants" }

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gecko ate {prey} for a meal')
        else:
            print(f'The gecko rejects the {prey}')

    def move(self):
        print(f"The {self. species} walks")

    def __str__(self):
        return f'Gecko {self.id}'