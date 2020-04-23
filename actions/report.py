def build_facility_report(arboretum):
    for river in arboretum.rivers:
        key = str(river.id)
        print(f'River [{key[:8]}]')
        for animal in river.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in river.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for swamp in arboretum.swamps:
        key = str(swamp.id)
        print(f'Swamp [{key[:8]}]')
        for animal in swamp.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in swamp.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for coastline in arboretum.coastline:
        key = str(coastline.id)
        print(f'Coastline [{key[:8]}]')
        for animal in coastline.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in coastline.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for mountain in arboretum.mountains:
        key = str(mountain.id)
        print(f'Mountain [{key[:8]}]')
        for animal in mountain.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in mountain.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for grassland in arboretum.grasslands:
        key = str(grassland.id)
        print(f'Grassland [{key[:8]}]')
        for animal in grassland.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in grassland.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    for forest in arboretum.forest:
        key = str(forest.id)
        print(f'Forest [{key[:8]}]')
        for animal in forest.animals:
            animal_key = str(animal.id)
            print(f'    {animal} ({animal_key[:8]})')
        for plant in forest.plants:
            plant_key = str(plant.id)
            print(f'    {plant} ({plant_key[:8]})')
        print("\n")

    input("\n\nPress enter key to continue...")
