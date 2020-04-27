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
        if len(arboretum.rivers) > 0:
            if arboretum.rivers[0].test_animal(animal):
                environments.append(arboretum.rivers)
        if len(arboretum.swamps) > 0:
            if arboretum.swamps[0].test_animal(animal):
                environments.append(arboretum.swamps)
        if len(arboretum.coastlines) > 0:
            if arboretum.coastlines[0].test_animal(animal):
                environments.append(arboretum.coastlines)
        if len(arboretum.grasslands) > 0:
            if arboretum.grasslands[0].test_animal(animal):
                environments.append(arboretum.grasslands)
        if len(arboretum.mountains) > 0:
            if arboretum.mountains[0].test_animal(animal):
                environments.append(arboretum.mountains)
        if len(arboretum.forests) > 0:
            if arboretum.forests[0].test_animal(animal):
                environments.append(arboretum.forests)
        for environment in environments: 
            for i in environment: 
                    print(f'{index + 1}. {i} ({i.get_animal_count()} animals)')
                    index += 1 
        return environments
                          
    environments = environment_loop()
    applicable_index = 0 
    if len(environments) == 0: 
        input("No applicable biomes, try again")
        release_animal(arboretum)
    else: 
        choice = input(f"Choose environment to release {animal} > ")
        try:
                choice_index = int(choice) - 1 
                applicable_environments = environments[applicable_index]
                for a in applicable_environments:
                    a.add_animal(animal)
        except ValueError:
                pass

    input("\n\nPress enter key to continue...")