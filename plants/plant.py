from interfaces import Identifiable

class Plant(Identifiable):

    def __init__(self, species):
      self.__species = species
      self.tolerate_shade = False
      self.tolerate_sun = False
      self.high_elevation = False
      self.__rainfall = ""
      self.__seeds_produced = 0
      self.__insecticide_resistance = 0
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season

      @property
      def species(self):
          return self.__species

      # @property
      # def tolerate_shade(self):
      #     return self.__tolerate_shade
        
      # @property
      # def tolerate_sun(self):
      #     return self.__tolerate_sun
        
      # @property
      # def high_elevation(self):
      #     return self.__high_elevation
        
      @property
      def rainfall(self):
          return self.__rainfall
                
      @property
      def seeds_produced(self):
          return self.__seeds_produced
        
      @property
      def insecticide_resistance(self):
          return self.__insecticide_resistance