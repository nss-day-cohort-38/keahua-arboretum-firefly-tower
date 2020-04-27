import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Mountain
from environments import Forest


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')


    def countX(list, x):
        count = 0
        for ele in list:
            if (ele == x):
                count = count + 1
        return count

    def animal_list_func():
        new_animal_list = list()
        new_plant_list = list()

        for river in arboretum.rivers:
            for animal in river.animals:
                animal_species = animal.species
                new_animal_list.append(str(animal_species))
                # number_of_animal = countX(new_animal_list, animal)


            for plant in river.plants:
                plant_species = plant.species
                new_plant_list.append(str(plant_species))
                # number_of_plant = countX(new_plant_list, plant)


        print(new_animal_list)
        print(new_plant_list)
        # print(number_of_animal)
        # print(number_of_plant)



    print(animal_list_func())
    # animal_list()

    # def animal_species_func():
    #     for river in arboretum.rivers:
    #         for animal in river.animals:


    animals_dict = dict()
    for river in arboretum.rivers:
        for animal in river.animals:
            # number_of_animal = len(river.animals)
            # print(number_of_animal)
            # animal_species = animal.species
            # number_of_animal = countX(animal_list, animal)
            # print(number_of_animal)
            # animals_dict[animal_species] = number_of_animal
            # animals_dict["number of animal"] = number_of_animal
            # print(animals_dict)

            animals_values = animals_dict.values()
            animals_values_list = list(animals_values)
            # print(animals_values_list)

            # print(number_of_animal, animal_species)
            # animals_plants_str = ', ' .join(number_of_animal), animal_species if len(number_of_animal) > 1 else animal

            # print(f"1. River   {animals_plants_str} ")


# print("1. River (1 animal, 1 plant. etc...."))
# have empty list
# itereate over river then animals and plants in the biome
# put the pairs in thier own tuple
# put the tuples back into the list
# loop and count number of occurances and have that be the number(value)

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
