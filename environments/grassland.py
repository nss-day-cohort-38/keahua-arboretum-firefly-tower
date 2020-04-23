from environments import Environment

class Grassland(Environment): 
    def __init__(self): 
        super().__init__(self)
        animal_cap = 22
        plant_cap = 15
        
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.high_elevation == False and animal.tolerate_sun == True:
                right_animal = True 
        except AttributeError:
            raise AttributeError("Cannot add animals that do not tolerate sun or high elevation to a grassland.")
        if right_animal: 
            try:
                if self.get_animal_count < self.animal_cap:
                    self.animals.append(animal) 
            except AttributeError: 
                raise AttributeError("There are too many animals to add another one")
    def add_plant(self, plant):
        right_plant = False
        try:
            if plant.high_elevation  == False and plant.tolerate_sun == True:
                right_plant = True 
        except AttributeError:
            raise AttributeError("Cannot add plants that do not tolerate sun or high elevation to a grassland.")
        if right_plant: 
            try:
                if self.get_plant_count < self.plant_cap:
                    self.plants.append(plant) 
            except AttributeError: 
                raise AttributeError("There are too many plants to add another one")
