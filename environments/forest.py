from environments import Environment
class Forest(Environment):
    def __init__(self):
      super().__init__()
      self.characteristics = "Rainy, Shady"
      self.name = "Forest"
      self.animal_cap = 20
      self.plant_cap = 32
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.terrestrial and animal.tolerate_shade:
                right_animal = True
                print(f"{animal} successfully added!")
            else:
                print(f"Cannot add {animal}: aquatic, or terrestrial animals that can't tolerate shade to a forest")
        except AttributeError:
            print(f"Cannot add {animal}: aquatic, or terrestrial animals that can't tolerate shade to a forest")
        if right_animal:
            if animal.min_release_age <= animal.age:
                right_animal = True
            else:
                print(f"{animal} is not old enough to be released")
                right_animal = False
        if right_animal:
            if self.get_animal_count() < self.animal_cap:
                self.animals.append(animal)
            else:
                print("There are too many animals to add another one")
    def add_plant(self, plant):
        right_plant = False
        try:
            if plant.terrestrial and plant.tolerate_shade:
                right_plant = True
            else:
                print(f"Cannot add {plant} that can't tolerate shade to a forest")
        except AttributeError:
            print(f"Cannot add {plant} that can't tolerate shade to a forest")
        if right_plant:
            if self.get_plant_count() < self.plant_cap:
                self.plants.append(plant)
            else:
                print("There are too many plants to add another one")

    def test_plant(self, plant):
        right_plant = False
        try:
            if plant.terrestrial and plant.tolerate_shade:
                right_plant = True
        except AttributeError:
            right_plant = False
        if self.get_plant_count() == self.plant_cap:
            right_plant = False
        return right_plant