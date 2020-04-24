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

    def annex_rivers(self, river):
        self.__rivers.append(river)

    @property
    def grasslands(self):
        return self.__grasslands

    def annex_grasslands(self, grassland):
        self.__grasslands.append(grassland)

    @property
    def coastlines(self):
        return self.__coastlines

    def annex_coastlines(self, coastline):
        self.__coastlines.append(coastline)

    @property
    def mountains(self):
        return self.__mountains

    def annex_mountains(self, mountains):
        self.__mountains.append(mountains)

    @property
    def swamps(self):
        return self.__swamps

    def annex_swamps(self, swamp):
        self.__swamps.append(swamp)

    @property
    def forests(self):
        return self.__forests

    def annex_forests(self, forest):
        self.__forests.append(forest)
