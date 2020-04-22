from animals import Animal
from interfaces import ITerrestrial, Identifiable, IWalking

class HawaiianHappyFaceSpider(Animal, ITerrestrial, Identifiable, IWalking):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        IWalking.__init__(self)
        self.name = name
        self.__species = "Hawaiian Happy Face Spider"
        self.__min_release_age = .5
        self.age = age
        self.__prey = { "Flies", "Ants" }


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
            print(f'The spider ate {prey} for a meal')
        else:
            print(f'The spider rejects the {prey}')

    def move(self):
        print(f"The {self. species} walks")

    def __str__(self):
        return f'Hawaiian Happy Face Spider {self.id}'