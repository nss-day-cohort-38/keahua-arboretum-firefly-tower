from interfaces import Identifiable

class Plant(Identifiable):

    def __init__(self):
      super().__init__()
      self.species = ""
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season

    def __str__(self):
        return f'{self.species}'