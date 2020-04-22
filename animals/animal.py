class Animal:

    def __init__(self):
        self.name = ""
        self.__species = ""
        self.age = 0
        self.__min_release_age = 0
        self.__prey = {}

    def move(self):
        print(f"{self. species} moves")

    def feed(self, prey):
        return f"{self.species} was fed a {prey}"
