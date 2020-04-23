from environments import Environment
from interfaces import ITerrestrial

class Grassland(Environment, ITerrestrial): 
    def __init__(self): 
        Environment.__init__(self)
        ITerrestrial.__init__(self)
        animal_cap = 22
        plant_cap = 15
        
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.high_elevation == False and animal.tolerate_shade == False:
                right_animal = True 
        except AttributeError:
            raise AttributeError("Cannot add animals that tolerate shade or high elevation to a grassland.")
        if right_animal: 
            try:
                if self.get_animal_count < self.animal_cap:
                    self.animals.append(animal) 
            except AttributeError: 
                raise AttributeError("Cannot add more than 22 animals.")
    def add_plant(self, plant):
        right_plant = False
        try:
            if plant.high_elevation  == False and plant.tolerate_shade == False:
                right_plant = True 
        except AttributeError:
            raise AttributeError("Cannot add plants that tolerate shade or high elevation to a grassland.")
        if right_plant: 
            try:
                if self.get_plant_count < self.plant_cap:
                    self.plants.append(plant) 
            except AttributeError: 
                raise AttributeError("Cannot add more than 15 plants.")
