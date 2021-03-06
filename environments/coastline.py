from environments import Environment

class Coastline(Environment):
    def __init__(self):
      super().__init__()
      self.characteristics = "Saltwater"
      self.name = "Coastline"
      self.animal_cap = 15
      self.plant_cap = 3
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.aquatic and animal.saltwater:
                right_animal = True
                print(f"{animal} successfully added!")
            else:
                print(f"Cannot add {animal}: non-aquatic, or freshwater animals to a coastline")
        except AttributeError:
            print(f"Cannot add {animal}: non-aquatic, or freshwater animals to a coastline")
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
            if animal.aquatic and animal.saltwater:
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
            if plant.saltwater:
                self.plants.append(plant)
            else:
                print("Too salty to plant {plant} here")
        except AttributeError:
            print("Too salty to plant {plant} here")
            
    def test_plant(self, plant):
        try:
            if plant.saltwater:
                return True
            else:
                return False
        except AttributeError:
            return False
