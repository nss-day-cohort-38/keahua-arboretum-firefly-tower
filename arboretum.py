class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__rivers = []
        self.__grasslands = []
        self.__coastlines = []
        self.__mountains = []
        self.__swamps = []
        self.__forests = []

    @property
    def rivers(self):
        return self.__rivers

    def annex_river(self, river):
        self.__rivers.append(river)

    @property
    def grasslands(self):
        return self.__grasslands

    def annex_grassland(self, grassland):
        self.__grasslands.append(grassland)

    @property
    def coastline(self):
        return self.__coastlines

    def annex_coastline(self, coastline):
        self.__coastlines.append(coastline)

    @property
    def mountains(self):
        return self.__mountains

    def annex_mountain(self, mountains):
        self.__mountains.append(mountains)

    @property
    def swamps(self):
        return self.__swamps

    def annex_swamp(self, swamp):
        self.__swamps.append(swamp)

    @property
    def forests(self):
        return self.__forest

    def annex_forest(self, forest):
        self.__forest.append(forest)
