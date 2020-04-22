from animals import Animal
from interfaces import ISaltwater, Identifiable, ISwimming

class Ulae(Animal, ISaltwater, Identifiable, ISwimming):

    def __init__(self, age, name):
        Animal.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        ISwimming.__init__(self)
        self.name = name
        self.__species = "Ulae"
        self.__min_release_age = 1
        self.age = age
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }


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
            print(f'The lizard fish ate {prey} for a meal')
        else:
            print(f'The lizard fish rejects the {prey}')

    def move(self):
        print(f"The {self. species} swims")

    def __str__(self):
        return f'Ulae {self.id}'