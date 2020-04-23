import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Mountain
from environments import Forest


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")
    choice = input("Choose your habitat > ")
    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
        pass
    if choice == "2":
        swamp = Swamp()
        arboretum.rivers.append(swamp)
        pass
    if choice == "3":
        coastline = Coastline()
        arboretum.coastline.append(coastline)
        pass
    if choice == "4":
        grassland = Grassland()
        arboretum.grassland.append(grassland)
        pass
    if choice == "5":
        mountain = Mountain()
        arboretum.mountain.append(mountain)
        pass
    if choice == "6":
        forest = Forest()
        arboretum.forest.append(forest)
        pass
