from animals import Animal
from interfaces import ITerrestrial, IFlying

class Pueo(Animal, ITerrestrial, IFlying):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        IFlying.__init__(self)
        self.name = name
        self.__species = "Pueo"
        self.__min_release_age = 8
        self.age = age
        self.__prey = { "Mouse", "Rat" }
        self.tolerate_shade = True
        self.tolerate_sun = True

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The owl ate {prey} for a meal')
        else:
            print(f'The owl rejects the {prey}')

    def move(self):
        print(f"The {self. species} flies")

    def __str__(self):
        return f'Pueo {self.id}'