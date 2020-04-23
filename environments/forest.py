from environments import Environment
class Forest(Environment):
    def _init_(self):
      super()._init_(self)
      self.characteristics = "Rainy, Shady"
      self.animal_cap = 20
      self.plant_cap = 32
    def add_animal(self, animal):
        right_animal = False
        try:
            if animal.terrestrial and animal.tolerate_shade:
                right_animal = True
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or terrestrial animals that can't tolerate shade to a forest")
        if right_animal:
            try:
                if self.get_animal_count < self.animal_cap:
                    self.animals.append(animal)
            except AttributeError:
                raise AttributeError("There are too many animals to add another one")
    def add_plant(self, plant):
        right_plant = False
        try:
            if plant.terrestrial and plant.tolerate_shade:
                right_plant = True
        except AttributeError:
            raise AttributeError("Cannot add plants that can't tolerate shade to a forest")
        if right_plant:
            try:
                if self.get_plant_count < self.plant_cap:
                    self.plants.append(plant)
            except AttributeError:
                raise AttributeError("There are too many plants to add another one")