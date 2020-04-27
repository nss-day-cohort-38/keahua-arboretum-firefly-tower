import os
from animals import Animal, GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae
from .header import header

def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    title = "Feed Animal"

    def step_one():
        os.system('cls' if os.name == 'nt' else 'clear')
        
        header(title)

        animal = None

        index = 0

        existingAnimals = []
        
        if len(GoldDustDayGecko.instances) != 0:
            index = index + 1
            existingAnimals.append(GoldDustDayGecko)
            print(f"{index}. Gold Dust Day Gecko")
        
        if len(HawaiianHappyFaceSpider.instances) != 0:
            index = index + 1
            existingAnimals.append(HawaiianHappyFaceSpider)
            print(f"{index}. Hawaiian Happy Face Spider")

        if len(Kikakapu.instances) != 0:
            index = index + 1
            existingAnimals.append(Kikakapu)
            print(f"{index}. Kikakapu")

        if len(NeneGoose.instances) != 0:
            index = index + 1
            existingAnimals.append(NeneGoose)
            print(f"{index}. Nene Goose")

        if len(Opeapea.instances) != 0:
            index = index + 1
            existingAnimals.append(Opeapea)
            print(f"{index}. Opeapea")

        if len(Pueo.instances) != 0:
            index = index + 1
            existingAnimals.append(Pueo)
            print(f"{index}. Pueo")
        
        if len(RiverDolphin.instances) != 0:
            index = index + 1
            existingAnimals.append(RiverDolphin)
            print(f"{index}. River Dolphin")

        if len(Ulae.instances) != 0:
            index = index + 1
            existingAnimals.append(Ulae)
            print(f"{index}. Ulae")

        if len(existingAnimals) != 0:
            print("0. Return to main menu\n\n")

        if len(existingAnimals) == 0:
            input("There are no animals to feed. Press enter to return to the main menu...")
            # returning 0 to stop the rest of the code from running
            return 0
        else:
            print("Choose animal species to feed")
            choice = input("> ")

        index = 0
        for choices in existingAnimals:
            if choice == str(index + 1):
                animal = existingAnimals[index]
                step_two(animal)
            index += 1

        try:
            if int(choice) < 0 or int(choice) > len(existingAnimals):
                input("\n\n Animal species does not exist. Please press enter to try again. ")
                step_one()
            elif int(choice) == 0:
                return 0
        except ValueError:
            input("\n\n Animal species does not exist. Please press enter to try again. ")
            step_one()

    def step_two(animal):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        header(title)

        if len(animal.instances) == 0:
            input("\n\nThere are no individuals of this species in your arboretum. Please press enter to try again...")
            step_one()
        else:
            for index, instance in enumerate(animal.instances):
                print(f"{index + 1}. {instance.name} the {instance.species}")

        print("0. Return to main menu\n\n")
    
        print("Choose which individual to feed")
        
        choice = input("> ")
        try:
            choice = int(choice)
        except ValueError:
            pass

        try:
            if isinstance(choice, int):
                if choice < 0:
                    input("\n\nIndividual animal does not exist. Please press enter to try again...")
                    step_two(animal)
                elif choice == 0:
                    return 0
                else:
                    animal = animal.instances[choice -1]
                    step_three(animal)
            else:
                input("\n\nIndividual animal does not exist. Please press enter to try again...")
                step_two(animal)
        except IndexError:
            input("\n\nIndividual animal does not exist. Please press enter to try again...")
            step_two(animal)

    def step_three(animal):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        header(title)

        for index, prey in enumerate(animal.prey):
            print(f'{index + 1}. {prey}')   

        print("0. Return to main menu\n\n")     

        print("Choose what to feed it")

        choice = input("> ")
        try:
            choice = int(choice)
        except ValueError:
            pass

        print("\n")

        try:
            if isinstance(choice, int):
                if choice < 0:
                    input("\n\nPrey does not exist. Please press enter to try again...")
                    step_three(animal)
                elif choice == 0:
                    return 0
                else:
                    animal.feed(animal.prey[choice - 1])
                    input("\n\nPress enter key to continue...")
            else: 
                input("\n\nPrey does not exist. Please press enter to try again...")
                step_three(animal)
        except IndexError:
            input("\n\nPrey does not exist. Please press enter to try again...")
            step_three(animal)
    
    step_one()


        
        


    

