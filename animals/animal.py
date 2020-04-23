from interfaces import Identifiable

class Animal(Identifiable):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.species = ""
        self.age = 0
        self.min_release_age = 0
        self.prey = {}

    def move(self):
        print(f"{self.species} moves")

    def feed(self, prey):
        return f"The {self.species} ate a {prey} for a meal"

    def __str__(self):
        return f'{self.species}'

    
