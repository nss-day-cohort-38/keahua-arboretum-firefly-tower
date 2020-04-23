from interfaces import IAquatic

class IFreshwater(IAquatic):

    def __init__(self):
        super().__init__()
        self.freshwater = True
        self.tolerate_stagnant = False
        self.tolerate_fresh = False
