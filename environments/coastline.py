from environments import Environment

class Coastline(Environment):
    def __init__(self):
      super().__init__(self)
      self.characteristics = "Saltwater"
      self.animal_cap = 15
      self.plant_cap = 3
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.aquatic and animal.saltwater:
                right_animal = True
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or freshwater animals to a coastline")
        if right_animal:
            try:
                if self.get_animal_count < self.animal_cap:
                    self.animals.append(animal)
            except AttributeError:
                raise AttributeError("There are too many animals to add another one")
    def add_plant(self, plant):
        try:
            if plant.saltwater:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Too salty to plant stuff here")