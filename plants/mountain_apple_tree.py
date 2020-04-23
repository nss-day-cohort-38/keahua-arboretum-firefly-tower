from interfaces import ITerrestrial
from plants import Plant

class MountainAppleTree(ITerrestrial, Plant):

    def __init__(self):
      self.__species = "Mountain Apple Tree"
      
      ITerrestrial.__init__(self)
      Plant.__init__(self, self.species)
      
      self.tolerate_shade = True
      self.tolerate_sun = False
      self.high_elevation = True
      self.__seeds_produced = 17
      self.__insecticide_resistance = "High"
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season
      
