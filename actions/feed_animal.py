import os
from animals import Animal, GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae


def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    def step_one():
        os.system('cls' if os.name == 'nt' else 'clear')

        animal = None

        print("1. Gold Dust Day Gecko")
        print("2. Hawaiian Happy Face Spider")
        print("3. Kikakapu")
        print("4. Nene Goose")
        print("5. Opeapea")
        print("6. Pueo")
        print("7. River Dolphin")
        print("8. Ulae")

        choice = input("Choose animal to feed > ")

        if choice == "1":
            animal = GoldDustDayGecko
        

        elif choice == "2":
            animal = HawaiianHappyFaceSpider
        

        elif choice == "3":
            animal = Kikakapu
        

        elif choice == "4":
            animal = NeneGoose
        

        elif choice == "5":
            animal = Opeapea
        

        elif choice == "6":
            animal = Pueo
        

        elif choice == "7":
            animal = RiverDolphin
        

        elif choice == "8":
            animal = Ulae

        else:
            input("\n\nAnimal species does not exist. Please press enter to try again...")
            step_one()

        step_two(animal)

    def step_two(animal):
        os.system('cls' if os.name == 'nt' else 'clear')

        for index, instance in enumerate(animal.instances):
                print(f"{index + 1}. {instance.name} the {instance.species}")
    
        print("Choose which individual to feed")
        
        choice = int(input("> "))

        try:
            animal = animal.instances[choice -1]
        except IndexError:
            input("\n\nIndividual animal does not exist. Please press enter to try again...")
            step_two(animal)

        for index, prey in enumerate(animal.prey):
            print(f'{index + 1}. {prey}')        
    
        print("Choose what to feed it")
        choice = int(input("> "))
        print("\n")

        try:
            animal.feed(animal.prey[choice - 1])
        except IndexError:
            input("\n\nPrey does not exist. Please press enter to try again...")
            step_one()

        input("\n\nPress enter key to continue...")

    step_one()


        
        


    

