import os
from animals import GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae
from .header import header


def release_animal(arboretum):
    def step_1():
        os.system('cls' if os.name == 'nt' else 'clear')
        header("Release Animal")

    print('1. Gold Dust Day Gecko')
    print('2. River Dolphin')
    print('3. Nene Goose')
    print('4. Kīkākapu')
    print('5. Pueo')
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    animal = None
        arboretum_biome_selection = []

        arboretum_biome_selection.append(arboretum.rivers)
        arboretum_biome_selection.append(arboretum.swamps)
        arboretum_biome_selection.append(arboretum.coastlines)
        arboretum_biome_selection.append(arboretum.forests)
        arboretum_biome_selection.append(arboretum.mountains)
        arboretum_biome_selection.append(arboretum.grasslands)

        def all(arboretum_biome_selection):
            for biome in arboretum_biome_selection:
                if len(biome) == 0:
                    return False
                else:
                    return True
        all(arboretum_biome_selection)
        if all(arboretum_biome_selection) == False:
            input("No habitats annexed. Press enter to return to the main menu...")
            return 0
        else:
            print('1. Gold Dust Day Gecko')
            print('2. River Dolphin')
            print('3. Nene Goose')
            print('4. Kīkākapu')
            print('5. Pueo')
            print("6. 'Ulae")
            print("7. Ope'ape'a")
            print("8. Happy-Face Spider")
            print("0. Return to main menu")

            animal = None

    if choice == "1":
        print("Enter age for Gold Dust Day Gecko : ")
        answer1 = int(input())
        print("Enter name for Gold Dust Day Gecko : ")
        answer2 = input()
        if answer1 is not "" and answer2 is not "":
            animal = GoldDustDayGecko(answer1, answer2)

    if choice == "2":
        print("Enter age for River Dolphin : ")
        answer1 = int(input())
        print("Enter name for River Dolphin : ")
        answer2 = input()
        if answer1 is not "" and answer2 is not "":
            animal = RiverDolphin(answer1, answer2)

    if choice == "3":
        print("Enter age for Nene Goose : ")
        answer1 = int(input())
        print("Enter name for Nene Goose : ")
        answer2 = input()
        if answer1 is not "" and answer2 is not "":
            animal = NeneGoose(answer1, answer2)

    if choice == "4":
        print("Enter age for Kikakapu : ")
        answer1 = int(input())
        print("Enter name for Kikakapu : ")
        answer2 = input()
        if answer1 is not "" and answer2 is not "":
            animal = Kikakapu(answer1, answer2)

    if choice == "5":
        print("Enter age for Pueo : ")
        answer1 = int(input())
        print("Enter name for Pueo : ")
        answer2 = input()
        if answer1 is not "" and answer2 is not "":
            animal = Pueo(answer1, answer2)

    if choice == "6":
        print("Enter age for Ulae : ")
        answer1 = int(input())
        print("Enter name for Ulae : ")
        answer2 = input()
        if answer1 is not "" and answer2 is not "":
            animal = Ulae(answer1, answer2)

    if choice == "7":
        print("Enter age for Opeapea : ")
        answer1 = int(input())
        print("Enter name for Opeapea : ")
        answer2 = input()
        if answer1 is not "" and answer2 is not "":
            animal = Opeapea(answer1, answer2)

    if choice == "8":
        print("Enter age for Hawaiian Happy Face Spider : ")
        answer1 = int(input())
        print("Enter name for Hawaiian Happy Face Spider : ")
        answer2 = input()
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
            choice = input("Choose animal to release > ")

        if choice == "0": 
            return 0

        if choice == "1":
            print("Enter age for Gold Dust Day Gecko : ")
            answer1=int(input())
            print("Enter name for Gold Dust Day Gecko : ")
            answer2=input()
            if answer1 is not "" and answer2 is not "":
                animal = GoldDustDayGecko(answer1, answer2)
                step_2(animal)  

        if choice == "2":
            print("Enter age for River Dolphin : ")
            answer1=int(input())
            print("Enter name for River Dolphin : ")
            answer2=input()
            if answer1 is not "" and answer2 is not "":
                animal = RiverDolphin(answer1, answer2)
                step_2(animal)  
        
        if choice == "3":
            print("Enter age for Nene Goose : ")
            answer1=int(input())
            print("Enter name for Nene Goose : ")
            answer2=input()
            if answer1 is not "" and answer2 is not "":
                animal = NeneGoose(answer1, answer2)
                step_2(animal)  
        
        if choice == "4":
            print("Enter age for Kikakapu : ")
            answer1=int(input())
            print("Enter name for Kikakapu : ")
            answer2=input()
            if answer1 is not "" and answer2 is not "":
                animal = Kikakapu(answer1, answer2)
                step_2(animal)  
        
        if choice == "5":
            print("Enter age for Pueo : ")
            answer1=int(input())
            print("Enter name for Pueo : ")
            answer2=input()
            if answer1 is not "" and answer2 is not "":
                animal = Pueo(answer1, answer2)
                step_2(animal)  

        if choice == "6":
            print("Enter age for Ulae : ")
            answer1=int(input())
            print("Enter name for Ulae : ")
            answer2=input()
            if answer1 is not "" and answer2 is not "":
                animal = Ulae(answer1, answer2)
                step_2(animal)  

        if choice == "7":
            print("Enter age for Opeapea : ")
            answer1=int(input())
            print("Enter name for Opeapea : ")
            answer2=input()
            if answer1 is not "" and answer2 is not "":
                animal = Opeapea(answer1, answer2)
                step_2(animal)  
        
        if choice == "8":
            print("Enter age for Hawaiian Happy Face Spider : ")
            answer1=int(input())
            print("Enter name for Hawaiian Happy Face Spider : ")
            answer2=input()
            if answer1 is not "" and answer2 is not "":
                animal = HawaiianHappyFaceSpider(answer1, answer2)
                step_2(animal)   

    # def environment_loop(): 
    def step_2(animal):
        os.system('cls' if os.name == 'nt' else 'clear')
        header("Release Animal")
        environments = []
        # if len(arboretum.rivers) > 0:
        #     if arboretum.rivers[0].test_animal(animal):
        environments.append(arboretum.rivers)
        # if len(arboretum.swamps) > 0:
        #     if arboretum.swamps[0].test_animal(animal):
        environments.append(arboretum.swamps)
        # if len(arboretum.coastlines) > 0:
        #     if arboretum.coastlines[0].test_animal(animal):
        environments.append(arboretum.coastlines)
        # if len(arboretum.grasslands) > 0:
        #     if arboretum.grasslands[0].test_animal(animal):
        environments.append(arboretum.grasslands)
        # if len(arboretum.mountains) > 0:
        #     if arboretum.mountains[0].test_animal(animal):
        environments.append(arboretum.mountains)
        # if len(arboretum.forests) > 0:
        #     if arboretum.forests[0].test_animal(animal):
        environments.append(arboretum.forests)
        for environment in environments: 
            index = 0 
            for i in environment:        
                    print(f'{index + 1}. {i} ({i.get_animal_count()} animals)')
                    index += 1 
        print('0. Return to main menu')
        # return environments
                       
        # environments = environment_loop()
        applicable_index = 0 
        if len(environments) == 0: 
                input("No applicable biomes, try again")
                release_animal(arboretum)
        else: 
                choice = input(f"Choose environment to release {animal} > ")
                try:
                    if choice == "0": 
                        return 0 
                    elif int(choice) > 0:  
                        applicable_environments = environments[applicable_index]
                        index = int(choice) - 1 
                        chosen_environment = applicable_environments[index]
                        confirm = input(f"Add {animal} to {chosen_environment}: y/n? > ")
                        if confirm == "y":
                            chosen_environment.add_animal(animal) 
                    else: 
                        print("Selected environment does not exist. Please press enter to try again...")
                except IndexError:
                        input("Selected environment does not exist. Please press enter to try again...")
                        step_2(animal)             

    # input("\n\nPress enter key to continue...")
    step_1()
