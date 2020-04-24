from environments import Environment

class Mountain(Environment): 
    def __init__(self): 
        super().__init__()
        self.animal_cap = 6
        self.plant_cap = 4
        self.name="Mountain"
        
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.high_elevation == True:
                right_animal = True 
                print(f"{animal} successfully added!")
            else: 
                print(f"Cannot add {animal} without ability to withstand high elevations to a mountain.")
        except AttributeError:
                print(f"Cannot add {animal} without ability to withstand high elevations to a mountain.")

        if right_animal:
            if animal.min_release_age <= animal.age:
                right_animal = True
                print(f"{animal} successfully added!")
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
    def add_plant(self, plant):
        right_plant = False
        try:
            if plant.high_elevation == True:
                right_plant = True 
            else: 
                print(f"Cannot add {plant} without ability to withstand high elevations to a mountain.")
        except AttributeError:
                print(f"Cannot add {plant} without ability to withstand high elevations to a mountain.")
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
            if plant.high_elevation  == True:
                right_plant = True
        except AttributeError:
            right_plant = False
        if self.get_plant_count() == self.plant_cap:
            right_plant = False
        return right_plant
