from interfaces import ITerrestrial
from plants import Plant

class Silversword(ITerrestrial, Plant):

    def __init__(self):
      self.__species = "Silversword"
      
      ITerrestrial.__init__(self)
      Plant.__init__(self)
      
      self.tolerate_shade = False
      self.tolerate_sun = True
      self.__seeds_produced = 22
      self.__insecticide_resistance = "High"
      self.__rainfall = "Little"
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season