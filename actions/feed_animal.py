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

        try:

            if choice == "1":
                animal = GoldDustDayGecko
            

            if choice == "2":
                animal = HawaiianHappyFaceSpider
            

            if choice == "3":
                animal = Kikakapu
            

            if choice == "4":
                animal = NeneGoose
            

            if choice == "5":
                animal = Opeapea
            

            if choice == "6":
                animal = Pueo
            

            if choice == "7":
                animal = RiverDolphin
            

            if choice == "8":
                animal = Ulae

            for index, instance in enumerate(animal.instances):
                print(f"{index + 1}. {instance.name} the {instance.species}")

        except AttributeError:
            input("\n\nAnimal does not exist. Please press enter to try again...")
            step_one()
    

        print("Choose which individual to feed")
        choice = int(input("> "))

        animal = animal.instances[choice -1]

        for index, prey in enumerate(animal.prey):
            print(f'{index + 1}. {prey}')        
        
        print("Choose what to feed it")
        choice = int(input("> "))
        print("\n")
        animal.feed(animal.prey[choice - 1])

        input("\n\nPress enter key to continue...")

    step_one()


        
        


    

