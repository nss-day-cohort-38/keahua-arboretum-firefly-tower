from interfaces import Identifiable

class Plant(Identifiable):

    def __init__(self):
      self.species = ""
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season
