class Plant:

    def __init__(self, species):
      self.species = species
      self.tolerate_shade = False
      self.tolerate_sun = False
      self.high_elevation = False
      self.rainfall = ""
      self.seeds_produced = 0
      self.insecticide_resistance = 0
      
      # Was in the original code but doesn't appear to be used
      # self.peak_season = season

