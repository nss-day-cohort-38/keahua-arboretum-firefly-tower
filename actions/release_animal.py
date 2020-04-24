from animals import GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae
def release_animal(arboretum):
    animal = None

    print('1. Gold Dust Day Gecko')
    print('2. River Dolphin')
    print('3. Nene Goose')
    print('4. Kīkākapu')
    print('5. Pueo')
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release > ")

    if choice == "1":
        print("Enter age for Gold Dust Day Gecko : ")
        answer1=int(input())
        print("Enter name for Gold Dust Day Gecko : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = GoldDustDayGecko(answer1, answer2)

    if choice == "2":
        print("Enter age for River Dolphin : ")
        answer1=int(input())
        print("Enter name for River Dolphin : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = RiverDolphin(answer1, answer2)
    
    if choice == "3":
        print("Enter age for Nene Goose : ")
        answer1=int(input())
        print("Enter name for Nene Goose : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = NeneGoose(answer1, answer2)
    
    if choice == "4":
        print("Enter age for Kikakapu : ")
        answer1=int(input())
        print("Enter name for Kikakapu : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = Kikakapu(answer1, answer2)
    
    if choice == "5":
        print("Enter age for Pueo : ")
        answer1=int(input())
        print("Enter name for Pueo : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = Pueo(answer1, answer2)

    if choice == "6":
        print("Enter age for Ulae : ")
        answer1=int(input())
        print("Enter name for Ulae : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = Ulae(answer1, answer2)

    if choice == "7":
        print("Enter age for Opeapea : ")
        answer1=int(input())
        print("Enter name for Opeapea : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = Opeapea(answer1, answer2) 
    
    if choice == "8":
        print("Enter age for Hawaiian Happy Face Spider : ")
        answer1=int(input())
        print("Enter name for Hawaiian Happy Face Spider : ")
        answer2=input()
        if answer1 is not "" and answer2 is not "":
            animal = HawaiianHappyFaceSpider(answer1, answer2)
            
    
    def environment_loop(): 
        index = 0 
        environments = []
        environments.append(arboretum.rivers)
        environments.append(arboretum.swamps)
        environments.append(arboretum.coastlines)
        environments.append(arboretum.grasslands)
        environments.append(arboretum.mountains)
        environments.append(arboretum.forests)
        for environment in environments: 
            for i in environment: 
                print(f'{index + 1}. {i} {i.get_animal_count()} animals')
                index += 1       
    environment_loop()

    print("Release the animal into which biome?") 
    print(f"1. River")
    print(f"2. Swamp")
    print(f"3. Coastline")
    print(f"4. Grassland")
    print(f"5. Mountain")
    print(f"6. Forest")

    choice = input("> ")
       
                
    if choice == "1":
        try: 
            for river in arboretum.rivers: 
                if len(river.animals) < river.animal_cap: 
                    river.add_animal(animal)
                else: 
                    print("****   That biome is not large enough   **** ****     Please choose another one      ****")
        except AttributeError: 
             print("****   That biome is not large enough   **** ****     Please choose another one      ****")
    if choice == "2":
        try: 
            for swamp in arboretum.swamps: 
                if len(swamp.animals) < swamp.animal_cap: 
                    swamp.add_animal(animal)
                    
                else: 
                    print("****   That biome is not large enough   **** ****     Please choose another one      ****")
        except AttributeError: 
             print("****   That biome is not large enough   **** ****     Please choose another one      ****")
    if choice == "3":
        try: 
            for coastline in arboretum.coastlines: 
                if len(coastline.animals) < coastline.animal_cap: 
                    coastline.add_animal(animal)
                    
                else: 
                    print("****   That biome is not large enough   **** ****     Please choose another one      ****")
        except AttributeError: 
             print("****   That biome is not large enough   **** ****     Please choose another one      ****")
    if choice == "4":
        try: 
            for grassland in arboretum.grasslands: 
                if len(grassland.animals) < grassland.animal_cap: 
                    grassland.add_animal(animal)
                    
                else: 
                    print("****   That biome is not large enough   **** ****     Please choose another one      ****")
        except AttributeError: 
             print("****   That biome is not large enough   **** ****     Please choose another one      ****")
    if choice == "5":
        try: 
            for mountain in arboretum.mountains: 
                if len(mountain.animals) < mountain.animal_cap: 
                    mountain.add_animal(animal)
                    
                else: 
                    input("****   That biome is not large enough   **** ****     Please choose another one      ****")
        except AttributeError: 
             print("****   That biome is not large enough   **** ****     Please choose another one      ****")
    if choice == "6":
        try: 
            for forest in arboretum.forests: 
                if len(forest.animals) < forest.animal_cap: 
                    forest.add_animal(animal)
                    
                else: 
                    print("****   That biome is not large enough   **** ****     Please choose another one      ****")
        except AttributeError: 
             print("****   That biome is not large enough   **** ****")
             print("****     Please choose another one      ****")

    input("\n\nPress enter key to continue...")