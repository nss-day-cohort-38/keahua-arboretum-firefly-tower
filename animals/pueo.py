from animals import Animal
from interfaces import ITerrestrial, Identifiable, IFlying

class Pueo(Animal, ITerrestrial, Identifiable, IFlying):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        IFlying.__init__(self)
        self.name = name
        self.__species = "Pueo"
        self.__min_release_age = 8
        self.age = age
        self.__prey = { "Mouse", "Rat" }


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
            print(f'The owl ate {prey} for a meal')
        else:
            print(f'The owl rejects the {prey}')

    def move(self):
        print(f"The {self. species} flies")

    def __str__(self):
        return f'Pueo {self.id}'