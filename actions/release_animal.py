from animals import GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae

def release_animal(arboretum):
    animal = None

    print('1. Gold Dust Day Gecko')
    print('2. RiverDolphin')
    print('3. Nene Goose')
    print('4. Kīkākapu')
    print('5. Pueo')
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release > ")


    if choice == "1":
        print("Enter name for Gold Dust Day Gecko : ")
        answer1=input()
        print("Enter age for Gold Dust Day Gecko : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = GoldDustDayGecko(answer1, answer2)

    if choice == "2":
        animal = RiverDolphin()
    
    if choice == "3":
        animal = NeneGoose()
    
    if choice == "4":
        animal = Kikakapu()
    
    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal = Opeapea() 
    
    if choice == "8":
        animal = HawaiianHappyFaceSpider()
    

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = NeneGoose()

    if choice == "6":
        animal = Opeapea()

    if choice == "7":
        animal = Pueo()

    if choice == "8":
        animal = Ulae()

    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')
    
    for index, swamp in enumerate(arboretum.swamps):
        print(f'{index + 1}. Swamp {swamp.id}')
    
    for index, coastline in enumerate(arboretum.coastlines):
        print(f'{index + 1}. Coastline {coastline.id}')
    
    for index, grassland in enumerate(arboretum.grasslands):
        print(f'{index + 1}. Grassland {grassland.id}')

    for index, mountain in enumerate(arboretum.mountains):
        print(f'{index + 1}. Mountain {mountain.id}')
    
    for index, forest in enumerate(arboretum.forests):
        print(f'{index + 1}. Forest {forest.id}')
    
    print("Release the animal into which biome?")
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")
    choice = input("> ")
    if choice == "1":
      arboretum.rivers[int(choice) - 1].animals.append(animal)
    if choice == "2":
      arboretum.swamps[int(choice) - 1].animals.append(animal)
    if choice == "3":
      arboretum.coastlines[int(choice) - 1].animals.append(animal)
    if choice == "4":
      arboretum.grasslands[int(choice) - 1].animals.append(animal)
    if choice == "5":
      arboretum.mountains[int(choice) - 1].animals.append(animal)
    if choice == "6":
      arboretum.forests[int(choice) - 1].animals.append(animal)
