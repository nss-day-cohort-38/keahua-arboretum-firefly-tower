from animals import Animal
from interfaces import ITerrestrial, Identifiable, ISwimming, IWalking

class NeneGoose(Animal, ITerrestrial, Identifiable, ISwimming, IWalking):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        ISwimming.__init__(self)
        IWalking.__init__(self)
        self.name = name
        self.__species = "Nene Goose"
        self.__min_release_age = 7
        self.age = age
        self.__prey = { "grass", "plant", "leaves" }


    @property
    def prey(self):
        return self.__prey

    @property 
    def species(self):
        return self.__species

    @property
    def min_release_age(self):
        return self.__min_release_age

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The goose ate {prey} for a meal')
        else:
            print(f'The goose rejects the {prey}')

    def walk(self):
        print(f"{self. species} walks")

    def swim(self):
        print("The {self. species} swims")

    def __str__(self):
        return f'Nene Goose {self.id}'