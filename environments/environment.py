from interfaces import IContainsAnimals, IContainsPlants, Identifiable


class Environment(IContainsAnimals, IContainsPlants, Identifiable):
    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        # returns count of animals and plants based on length of list

    def get_animal_count(self):
        return len(self.animals)

    def get_plant_count(self):
        return len(self.plants)

    def __str__(self):
        return f"{self.name} [{str(self.id)[:8]}]"
