from interfaces import Identifiable

class Animal(Identifiable):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.__species = ""
        self.age = 0
        self.__min_release_age = 0
        self.__prey = {}

    @property
    def prey(self):
        return self.__prey

    @property 
    def species(self):
        return self.__species

    @property
    def min_release_age(self):
        return self.__min_release_age

    def move(self):
        print(f"{self.__species} moves")

    def feed(self, prey):
        return f"The {self.__species} ate a {prey} for a meal"

    def __str__(self):
        return f'{self.__species} {self.id}'

    
