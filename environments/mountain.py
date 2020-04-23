from environments import Environment

class Mountain(Environment): 
    def __init__(self): 
        super().__init__(self)
        animal_cap = 6
        plant_cap = 4

    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.high_elevation == True:
                self.right_animal = True 
        except AttributeError:
            raise AttributeError("Cannot add animals without ability to withstand high elevations to a mountain.")
        if right_animal: 
            try:
                if self.get_animal_count < self.animal_cap:
                    self.animals.append(animal) 
            except AttributeError: 
                raise AttributeError("Cannot add more than six animals.")
    def add_plant(self, plant):
        right_plant = False
        try:
            if plant.high_elevation == True:
                self.right_plant = True 
        except AttributeError:
            raise AttributeError("Cannot add plants without ability to withstand high elevations to a mountain.")
        if right_plant: 
            try:
                if self.get_animal_count < self.animal_cap:
                    self.plants.append(plant) 
            except AttributeError: 
                raise AttributeError("Cannot add more than four plants.")
    


