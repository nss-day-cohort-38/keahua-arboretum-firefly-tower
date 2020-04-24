from environments import Environment
class River(Environment):
    def __init__(self):
      super().__init__()
      self.characteristics = "Fresh Water"
      self.animal_cap = 12
      self.plant_cap = 6
      self.name="River"
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.aquatic and animal.tolerate_current and animal.freshwater:
                right_animal = True
                print(f"{animal} successfully added!")
            else: 
                print(f"Cannot add {animal}: non-aquatic, or saltwater, or stagnant water animals to a river")
        except AttributeError:
            print(f"Cannot add {animal}: non-aquatic, or saltwater, or stagnant water animals to a river")
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
                
    def test_animal(self, animal):
        right_animal = False
        try:
            if animal.aquatic and animal.tolerate_current and animal.freshwater:
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
        try:
            if plant.freshwater and plant.tolerate_stagnant == False:
                self.plants.append(plant)
            else:
                print(f"Cannot add {plant} that require stagnant water to a river biome")
        except AttributeError:
            print(f"Cannot add {plant} that require stagnant water to a river biome")