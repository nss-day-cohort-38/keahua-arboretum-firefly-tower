from environments import Environment

class Grassland(Environment): 
    def __init__(self): 
        super().__init__()
        self.animal_cap = 22
        self.plant_cap = 15
        self.name="Grassland"
        
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.high_elevation == False and animal.tolerate_sun == True:
                right_animal = True 
                print(f"{animal} successfully added!")
            else: 
                print(f"Cannot add {animal} that does not tolerate sun or high elevation to a grassland.")
        except AttributeError:
                print(f"Cannot add {animal} that does not tolerate sun or high elevation to a grassland.")

        if right_animal:
            if animal.min_release_age <= animal.age:
                right_animal = True
            else:
                print(f"{animal} is not old enough to be released")
                right_animal = False

        if right_animal: 
            try:
                if self.get_animal_count() < self.animal_cap:
                    self.animals.append(animal) 
                else: 
                    print("There are too many animals to add another one")
            except AttributeError: 
                    print("There are too many animals to add another one")
    
    def test_animal(self, animal):
        right_animal = False
        try:
            if animal.high_elevation == False and animal.tolerate_sun == True:
                right_animal = True
            else:
                right_animal = False
        except AttributeError:
            right_animal = False
        if right_animal:
            if animal.min_release_age <= animal.age:
                right_animal = True
            else:
                right_animal = False
        if self.get_animal_count() == self.animal_cap:
            right_animal = False
        return right_animal

    def add_plant(self, plant):
        right_plant = False
        try:
            if plant.high_elevation  == False and plant.tolerate_sun == True:
                right_plant = True 
            else: 
                print(f"Cannot add {plant} that does not tolerate sun or high elevation to a grassland.")
        except AttributeError:
                print(f"Cannot add {plant} that does not tolerate sun or high elevation to a grassland.")
        if right_plant: 
            try:
                if self.get_plant_count() < self.plant_cap:
                    self.plants.append(plant) 
                else: 
                    print("There are too many plants to add another one")
            except AttributeError: 
                    print("There are too many plants to add another one")

    def test_plant(self, plant):
        right_plant = False
        try:
            if plant.high_elevation  == False and plant.tolerate_sun == True:
                right_plant = True
        except AttributeError:
            right_plant = False
        if self.get_plant_count() == self.plant_cap:
            right_plant = False
        return right_plant