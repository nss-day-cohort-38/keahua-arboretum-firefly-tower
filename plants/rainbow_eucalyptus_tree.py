from interfaces import ITerrestrial
from plants import Plant

class RainbowEucalyptusTree(ITerrestrial, Plant):

    def __init__(self):
      self.__species = "Rainbow Eucalyptus Tree"
      
      ITerrestrial.__init__(self)
      Plant.__init__(self)
      
      self.tolerate_shade = True
      self.tolerate_sun = False
      self.__rainfall = "Rainy"
      self.__seeds_produced = 8
      self.__insecticide_resistance = "Low"
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season