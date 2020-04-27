import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Mountain
from environments import Forest


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    # def countX(list, x):
    #     count = 0
    #     for ele in list:
    #         if (ele == x):
    #             count = count + 1
    #     return count

    def animal_list_func():
        new_animal_list = list()
        # new_plant_list = list()
        rivers_instances_list = arboretum.rivers

        def print_animal_count():
            for river in rivers_instances_list:
                animal_count = river.get_animal_count()
                print(animal_count)

            def animal_names():
                for animal in river.animals:
                    animal_species = animal.species
                    new_animal_list.append((animal_species))
                    print(animal_species)

            animal_names()
        print_animal_count()

        def count_animals():
            for animal in new_animal_list:
                count_number = new_animal_list.count(animal)
                print(count_number)



        count_animals()
        # print(new_animal_list)
        # print(new_plant_list)
        # print(number_of_animal)
        # print(number_of_plant)


    animal_list_func()

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
