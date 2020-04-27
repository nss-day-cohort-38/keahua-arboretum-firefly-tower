import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Mountain
from environments import Forest
from .header import header

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    # def sentence(build_list_func):
    #     def full_biome_description(*args, **kwargs):
    #         full_data = build_list_func(*args, **kwargs)
    #         return f"{full_data}"
    #     return full_biome_description



    rivers_instances_list = arboretum.rivers
    grasslands_instances_list = arboretum.grasslands
    coastlines_instances_list = arboretum.coastlines
    mountains_instances_list = arboretum.mountains
    swamps_instances_list = arboretum.swamps
    forests_instances_list = arboretum.forests



    # @sentence
    def build_list_func(biome_instance_list):
        new_animal_list = list()
        new_plant_list = list()

        def get_animal_plant_count():
            for biome in biome_instance_list:
                animal_count = biome.get_animal_count()
                plant_count = biome.get_plant_count()
                print(biome.name)

            def animal_plant_names():
                for animal in biome.animals:
                    animal_species = animal.species
                    new_animal_list.append((animal_species))
                for plant in biome.plants:
                    plant_species = plant.species
                    new_plant_list.append((plant_species))

            animal_plant_names()
        get_animal_plant_count()

        def count_animals_plants():
            for animal in new_animal_list:
                count_number_animal = new_animal_list.count(animal)
                print(count_number_animal, animal)

            for plant in new_plant_list:
                count_number_plant = new_plant_list.count(plant)
                print(count_number_plant, plant)


        count_animals_plants()

    build_list_func(rivers_instances_list)
    build_list_func(grasslands_instances_list)
    build_list_func(coastlines_instances_list)
    build_list_func(mountains_instances_list)
    build_list_func(swamps_instances_list)
    build_list_func(forests_instances_list)








    # def animal_list_func():
    #     new_animal_list = list()
    #     new_plant_list = list()
    #     # rivers_instances_list = arboretum.rivers

    #     def print_animal_count():
    #         for river in rivers_instances_list:
    #             animal_count = river.get_animal_count()
    #             # print(animal_count)

    #         def animal_names():
    #             for animal in river.animals:
    #                 animal_species = animal.species
    #                 new_animal_list.append((animal_species))
    #                 # print(animal_species)

    #         animal_names()
    #     print_animal_count()

    #     def count_animals():
    #         for animal in new_animal_list:
    #             count_number = new_animal_list.count(animal)
    #             print(count_number, animal)

    #     count_animals()

    # animal_list_func()



    header("Annex Habitat")

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


    # for river in arboretum.rivers:
    #     for animal in river.animals:
            # number_of_animal = len(river.animals)
            # print(number_of_animal)
            # animal_species = animal.species
            # number_of_animal = countX(animal_list, animal)
            # print(number_of_animal)
            # animals_dict[animal_species] = number_of_animal
            # animals_dict["number of animal"] = number_of_animal
            # print(animals_dict)

            # animals_values = animals_dict.values()
            # animals_values_list = list(animals_values)
            # print(animals_values_list)

            # print(number_of_animal, animal_species)
            # animals_plants_str = ', ' .join(number_of_animal), animal_species if len(number_of_animal) > 1 else animal

            # print(f"1. River   {animals_plants_str} ")
