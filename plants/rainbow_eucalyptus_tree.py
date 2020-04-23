from interfaces import ITerrestrial
from plants import Plant

class RainbowEucalyptusTree(ITerrestrial, Plant):

    def __init__(self):
      ITerrestrial.__init__(self)
      Plant.__init__(self)
      
      self.species = "Rainbow Eucalyptus Tree"
      self.tolerate_shade = True
      self.tolerate_sun = False
      self.rainfall = "Rainy"
      self.seeds_produced = 8
      self.insecticide_resistance = "Low"
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season