from interfaces import ITerrestrial
from plants import Plant

class MountainAppleTree(ITerrestrial, Plant):

    def __init__(self):
      ITerrestrial.__init__(self)
      Plant.__init__(self)
      
      self.species = "Mountain Apple Tree"
      self.tolerate_shade = True
      self.tolerate_sun = False
      self.high_elevation = True
      self.seeds_produced = 17
      self.insecticide_resistance = "High"
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season