from environments import Environment
class River(Environment):
    def __init__(self):
      super().__init__(self)
      self.characteristics = "Fresh Water"
      self.animal_cap = 12
      self.plant_cap = 6
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.aquatic and animal.tolerate_current and animal.freshwater:
                right_animal = True
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater, or stagnant water animals to a river")
        if right_animal:
            try:
                if self.get_animal_count < self.animal_cap:
                    self.animals.append(animal)
            except AttributeError:
                raise AttributeError("There are too many animals to add another one")
    def add_plant(self, plant):
        try:
            if plant.freshwater:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require stagnant water to a river biome")