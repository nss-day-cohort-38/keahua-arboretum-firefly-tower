from interfaces import ITerrestrial
from plants import Plant

class Silversword(ITerrestrial, Plant):

    def __init__(self):
      self.species = "Silversword"
      
      ITerrestrial.__init__(self)
      Plant.__init__(self, self.species)
      
      self.tolerate_shade = False
      self.tolerate_sun = True
      self.seeds_produced = 22
      self.insecticide_resistance = "High"
      self.rainfall = "Little"
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season