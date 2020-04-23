from environments import Environment

class Swamp(Environment):
    def __init__(self): 
        super().__init__(self)
        self.animal_cap = 8
        self.plant_cap = 12
        
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.tolerate_stagnant == True:
                right_animal = True 
        except AttributeError:
            raise AttributeError("Cannot add animals that cannot live in stagnant fresh waters to a swamp.")
        if right_animal: 
            try:
                if self.get_animal_count < self.animal_cap:
                    self.animals.append(animal) 
            except AttributeError: 
                raise AttributeError("There are too many animals to add another one")
    def add_plant(self, plant):
        right_plant = False
        try:
            if plant.tolerate_stagnant == True:
                right_plant = True 
        except AttributeError:
            raise AttributeError("Cannot add plants that cannot live in stagnant fresh waters to a swamp.")
        if right_plant: 
            try:
                if self.get_plant_count < self.plant_cap:
                    self.plants.append(plant) 
            except AttributeError: 
                raise AttributeError("There are too many plants to add another one")
