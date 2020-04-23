from interfaces import ITerrestrial, IFreshwater
from plants import Plant

class BlueJadeVine(ITerrestrial, IFreshwater, Plant):

    def __init__(self):
      self.species = "Blue Jade Vine"
      
      ITerrestrial.__init__(self)
      IFreshwater.__init__(self)
      Plant.__init__(self, self.species)
      
      self.tolerate_shade = True
      
      #Technically, the "Sunlight" entry on the readme says "Partial", 
      # but it also says it lives in grasslands, 
      # which are labeled as having "No Shade"
      self.tolerate_sun = True 
      
      # This being set to false by IFreshwater 
      # is not true for this plant if it lives in a swamp
      self.tolerate_stagnant = True
      
      self.__seeds_produced = 0
      self.__insecticide_resistance = "Medium"
      self.__rainfall = "Little"
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season
        
      @property
      def is_stagnant(self):
          return self.__is_stagnant