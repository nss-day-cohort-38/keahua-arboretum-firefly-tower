from interfaces import Identifiable

class Plant(Identifiable):

    def __init__(self):
      self.species = ""
      self.tolerate_shade = False
      self.tolerate_sun = False
      self.high_elevation = False
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season
