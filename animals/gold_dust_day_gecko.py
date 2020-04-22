from animals import Animal
from interfaces import ITerrestrial, Identifiable, IWalking

class GoldDustDayGecko(Animal, ITerrestrial, Identifiable, IWalking):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        IWalking.__init__(self)
        self.name = name
        self.__species = "Gold Dust Day Gecko"
        self.__min_release_age = 2
        self.age = age
        self.__prey = { "Fly", "Ants" }


    @property
    def prey(self):
        return self.__prey

    @prey.setter
    def prey(self, new_prey):
        if new_prey is not self.__prey:
            print("Cannot change prey items")

    @property 
    def species(self):
        return self.__species

    @species.setter
    def species(self, new_species):
        if new_species is not self.__species:
            print("Cannot change species")

    @property
    def min_release_age(self):
        return self.__min_release_age

    @min_release_age.setter
    def min_release_age(self, new_age):
        if new_age is not self.__min_release_age:
            print("Cannot change minimum release age")

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gecko ate {prey} for a meal')
        else:
            print(f'The gecko rejects the {prey}')

    def move(self):
        print(f"The {self. species} walks")

    def __str__(self):
        return f'Gecko {self.id}'