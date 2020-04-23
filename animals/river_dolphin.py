from animals import Animal
from interfaces import IFreshwater, ISwimming, ISaltwater

class RiverDolphin(Animal, IFreshwater, ISwimming, ISaltwater):

    def __init__(self, age, name):
        Animal.__init__(self)
        IFreshwater.__init__(self)
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
        self.name = name
        self.__species = "River Dolphin"
        self.__min_release_age = 13
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
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')

    def move(self):
        print(f"The {self. species} swims")

    def __str__(self):
        return f'River Dolphin {self.id}'
