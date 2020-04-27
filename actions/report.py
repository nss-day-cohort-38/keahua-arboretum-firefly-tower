import os
from .header import header 

def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    header("Facility Report")
    
    for river in arboretum.rivers:
        key = str(river.id)
        print(f'{river}')
        for animal in river.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in river.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for swamp in arboretum.swamps:
        key = str(swamp.id)
        print(f'{swamp}')
        for animal in swamp.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in swamp.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for coastline in arboretum.coastlines:
        key = str(coastline.id)
        print(f'{coastline}')
        for animal in coastline.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in coastline.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for mountain in arboretum.mountains:
        key = str(mountain.id)
        print(f'{mountain}')
        for animal in mountain.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in mountain.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for grassland in arboretum.grasslands:
        key = str(grassland.id)
        print(f'{grassland}')
        for animal in grassland.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in grassland.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for forest in arboretum.forests:
        key = str(forest.id)
        print(f'{forest}')
        for animal in forest.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in forest.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    input("\n\nPress enter key to continue...")
