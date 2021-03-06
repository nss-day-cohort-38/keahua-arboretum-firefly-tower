from interfaces import ITerrestrial, IFreshwater
from plants import Plant

class BlueJadeVine(ITerrestrial, IFreshwater, Plant):

    def __init__(self):
      ITerrestrial.__init__(self)
      IFreshwater.__init__(self)
      Plant.__init__(self)
      
      self.species = "Blue Jade Vine"
      
      #Technically, the "Sunlight" entry on the readme says "Partial", 
      # but it also says it lives in grasslands, 
      # which are labeled as having "No Shade"
      self.tolerate_sun = True 
      
      # This being set to false by IFreshwater 
      # is not true for this plant if it lives in a swamp
      self.tolerate_stagnant = True
      
      self.seeds_produced = 0
      self.insecticide_resistance = "Medium"
      self.rainfall = "Little"
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season