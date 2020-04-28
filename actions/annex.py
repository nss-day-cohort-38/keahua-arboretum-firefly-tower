import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Mountain
from environments import Forest
from .header import header
import pprint


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    rivers_instances_list = arboretum.rivers
    grasslands_instances_list = arboretum.grasslands
    coastlines_instances_list = arboretum.coastlines
    mountains_instances_list = arboretum.mountains
    swamps_instances_list = arboretum.swamps
    forests_instances_list = arboretum.forests

    def build_list_func(biome_instance_list):
        new_animal_list = list()
        new_plant_list = list()
        sentence = list()
        choices = dict()

        for biome in biome_instance_list:

            animal_count = biome.get_animal_count()
            plant_count = biome.get_plant_count()
            # sentence.append(biome.name)

            for animal in biome.animals:
                animal_species = animal.species
                new_animal_list.append((animal_species))
                # sentence.append(animal_species)

            for plant in biome.plants:
                plant_species = plant.species
                new_plant_list.append((plant_species))
                # sentence.append(plant_species)

        for animal in new_animal_list:
            count_number_animal = new_animal_list.count(animal)
            # print(count_number_animal, animal)
            animal_tuple = (count_number_animal, animal)
            sentence.append(animal_tuple)

        for plant in new_plant_list:
            count_number_plant = new_plant_list.count(plant)
            plant_tuple = (count_number_plant, plant)
            sentence.append(plant_tuple)

        choices[biome.name] = sentence
        # pprint.pprint(choices)

        for (key, value) in choices.items():
            print(f'{key}: {tuple(v for v in value)}')

    print('\n')
    print("+-++-++-++-++-++-++-++-++-++-++-++-+")
    print(r"  Currently in your Biomes ")
    print("+-++-++-++-++-++-++-++-++-++-++-++-+")
    print('\n')


    build_list_func(rivers_instances_list)
    build_list_func(grasslands_instances_list)
    build_list_func(coastlines_instances_list)
    build_list_func(mountains_instances_list)
    build_list_func(swamps_instances_list)
    build_list_func(forests_instances_list)

    print('\n')

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
