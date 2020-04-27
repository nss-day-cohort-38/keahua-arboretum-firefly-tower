import os
from animals import Animal, GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae
from plants import RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine
from environments import River, Swamp, Forest, Mountain, Coastline, Grassland 

animal_classes = [GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae]
plant_classes = [RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine]
environment_classes = [Coastline, Forest, Grassland, Mountain, River, Swamp]

path = "/home/kroogz/workspace/keahua-arboretum-firefly-tower/keahua.txt"

def annex(arboretum, environment_instance):
      """Annex an environment to the Arboretum

      Arguments: the environment instance to annex
      """
      
      #Depending on what class the instance is, 
      #change the annex_method to the appropriate append
      if isinstance(environment_instance, River):
          arboretum.rivers.append(environment_instance)
      elif isinstance(environment_instance, Grassland):
          arboretum.grasslands.append(environment_instance)
      elif isinstance(environment_instance, Coastline):
          arboretum.coastlines.append(environment_instance)
      elif isinstance(environment_instance, Mountain):
          arboretum.mountains.append(environment_instance)
      elif isinstance(environment_instance, Swamp):
          arboretum.swamps.append(environment_instance)
      elif isinstance(environment_instance, Forest):
          arboretum.forests.append(environment_instance)

def read_animal(biome, text):
    animal_from_text = text.readline()[:-1]
    name  = text.readline()[:-1]
    age = int(text.readline()[:-1])
    for animal in animal_classes:
        temp_animal = animal(age, name)
        if temp_animal.species == animal_from_text:
            animal_instance = animal(age, name)
            biome.add_animal(animal_instance)

def read_plant(biome, text):
    plant_from_text = text.readline()[:-1]
    for plant in plant_classes:
        temp_plant = plant()
        if temp_plant.species == plant_from_text:
            plant_instance = plant()
            biome.add_plant(plant_instance)

def read_text(arboretum):
    text = open(path, "r")
    environment_instance = ""
    current_line = text.readline()[:-1]
    while current_line != "":
        if current_line == "Biome":
            current_line = text.readline()[:-1]
            for biome in environment_classes:
                temp_biome = biome()
                if temp_biome.name == current_line:
                    environment_instance = biome()
            annex(arboretum, environment_instance)
        if current_line == "Animal":
            read_animal(environment_instance, text)
        if current_line == "Plant":
            read_plant(environment_instance, text)
        current_line = text.readline()[:-1]
    text.close()

def clear_text():
    open(path, 'w').close()

def write_text(arboretum):
    clear_text()
    text = open(path, 'a')
    for river in arboretum.rivers:
        text.write('Biome\n')
        text.write('River\n')
        for animal in river.animals:
            text.write('Animal\n')
            species = animal.species
            name = animal.name
            age = animal.age
            text.write(f'{species}\n')
            text.write(f'{name}\n')
            text.write(f'{age}\n')
        for plant in river.plants:
            text.write('Plant\n')
            text.write(f'{plant.species}\n')

    for swamp in arboretum.swamps:
        text.write('Biome\n')
        text.write('Swamp\n')
        for animal in swamp.animals:
            text.write('Animal\n')
            species = animal.species
            name = animal.name
            age = animal.age
            text.write(f'{species}\n')
            text.write(f'{name}\n')
            text.write(f'{age}\n')
        for plant in swamp.plants:
            text.write('Plant\n')
            text.write(f'{plant.species}\n')

    for coastline in arboretum.coastlines:
        text.write('Biome\n')
        text.write('Coastline\n')
        for animal in coastline.animals:
            text.write('Animal\n')
            species = animal.species
            name = animal.name
            age = animal.age
            text.write(f'{species}\n')
            text.write(f'{name}\n')
            text.write(f'{age}\n')
        for plant in coastline.plants:
            text.write('Plant\n')
            text.write(f'{plant.species}\n')

    for mountain in arboretum.mountains:
        text.write('Biome\n')
        text.write('Mountain\n')
        for animal in mountain.animals:
            text.write('Animal\n')
            species = animal.species
            name = animal.name
            age = animal.age
            text.write(f'{species}\n')
            text.write(f'{name}\n')
            text.write(f'{age}\n')
        for plant in mountain.plants:
            text.write('Plant\n')
            text.write(f'{plant.species}\n')

    for grassland in arboretum.grasslands:
        text.write('Biome\n')
        text.write('Grassland\n')
        for animal in grassland.animals:
            text.write('Animal\n')
            species = animal.species
            name = animal.name
            age = animal.age
            text.write(f'{species}\n')
            text.write(f'{name}\n')
            text.write(f'{age}\n')
        for plant in grassland.plants:
            text.write('Plant\n')
            text.write(f'{plant.species}\n')

    for forest in arboretum.forests:
        text.write('Biome\n')
        text.write('Forest\n')
        for animal in forest.animals:
            text.write('Animal\n')
            species = animal.species
            name = animal.name
            age = animal.age
            text.write(f'{species}\n')
            text.write(f'{name}\n')
            text.write(f'{age}\n')
        for plant in forest.plants:
            text.write('Plant\n')
            text.write(f'{plant.species}\n')
    text.close()
