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
            step_two(animal)
        

        elif choice == "2":
            animal = HawaiianHappyFaceSpider
            step_two(animal)
        

        elif choice == "3":
            animal = Kikakapu
            step_two(animal)
        

        elif choice == "4":
            animal = NeneGoose
            step_two(animal)
        

        elif choice == "5":
            animal = Opeapea
            step_two(animal)
        

        elif choice == "6":
            animal = Pueo
            step_two(animal)
        

        elif choice == "7":
            animal = RiverDolphin
            step_two(animal)
        

        elif choice == "8":
            animal = Ulae
            step_two(animal)

        else:
            input("\n\nAnimal species does not exist. Please press enter to try again...")
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
    
        print("Choose which individual to feed")
        
        choice = input("> ")
        try:
            choice = int(choice)
        except ValueError:
            pass

        try:
            if isinstance(choice, int):
                if choice <= 0:
                    input("\n\nIndividual animal does not exist. Please press enter to try again...")
                    step_two(animal)
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

        print("Choose what to feed it")

        choice = input("> ")
        try:
            choice = int(choice)
        except ValueError:
            pass

        print("\n")

        try:
            if isinstance(choice, int):
                if choice <= 0:
                    input("\n\nIndividual animal does not exist. Please press enter to try again...")
                    step_three(animal)
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


        
        


    

