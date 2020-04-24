from environments import Environment

class Swamp(Environment):
    def __init__(self): 
        super().__init__()
        self.animal_cap = 8
        self.plant_cap = 12
        self.name="Swamp"
        
    def add_animal(self, animal):
        right_animal = False

        try: 
            if animal.tolerate_stagnant == True:
                right_animal = True 
                print(f"{animal} successfully added!")
            else:
                print(f"Cannot add {animal} that cannot live in stagnant fresh waters to a swamp.")
        except AttributeError:
            print(f"Cannot add {animal} that cannot live in stagnant fresh waters to a swamp.")

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
                    print(f"{animal} successfully added!")
                else: 
                    print("There are too many animals to add another one")
            except AttributeError: 
                    print("There are too many plants to add another one")

    def add_plant(self, plant):
        right_plant = False

        try:
            if plant.tolerate_stagnant == True:
                right_plant = True 
                print(f"{plant} found new home")
            else: 
                print(f"Cannot add {plant} that cannot live in stagnant fresh waters to a swamp.")
        except AttributeError:
            print(f"Cannot add {plant} that cannot live in stagnant fresh waters to a swamp.")   

        if right_plant: 
            try:
                if self.get_plant_count() < self.plant_cap:
                    self.plants.append(plant) 
                else: 
                    print("There are too many plants to add another one")
            except AttributeError: 
                    print("There are too many plants to add another one")
