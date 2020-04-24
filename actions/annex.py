import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Mountain
from environments import Forest


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    rivers = set([i for i in arboretum.rivers])
    rivers_dict = dict()
    for river in rivers:
      rivers_dict[f"{river}"] = []
      for i in rivers:
        rivers_dict[f"{i.type}"].append(i.name.capitalize())
        final_sentence = [f"{a.capitalize()}s ({' and '.join([', '.join(v[:-1]),v[-1]] if len(v) > 2 else v)})" for a in rivers for k, v in rivers_dict.items() if k == a]

        animals_plants_str = ' and '.join([', '.join(final_sentence[:-1]), final_sentence[-1]] if len(final_sentence) > 2 else final_sentence)
        print(f"\n 1. River {animals_plants_str} \n")

    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")

    choice = input("Choose a KILLER habitat > ")
    if choice == "1":
        river = River()
        arboretum.rivers.append(river)

    if choice == "2":
        swamp = Swamp()
        arboretum.swamps.append(swamp)

    if choice == "3":
        coastline = Coastline()
        arboretum.coastlines.append(coastline)

    if choice == "4":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)

    if choice == "5":
        mountain = Mountain()
        arboretum.mountains.append(mountain)

    if choice == "6":
        forest = Forest()
        arboretum.forests.append(forest)
