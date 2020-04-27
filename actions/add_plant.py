import os
from plants import RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine
from .header import header

def add_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    title = "Cultivate Plant"
        
    # Choosing a plant to cultivate
    def step_one():
        os.system('cls' if os.name == 'nt' else 'clear')

        # Build a list of appropriate environment instances
        # based on the duck-type checks of the environments'
        # add_plant methods
        def determine_environs(plant_instance):
            # Starting a list of appropriate environments
            appropriate_environs = []
            # check if there are instances of the environment
            if len(arboretum.coastlines) > 0:
                # use the test_plant method, which will return true if
                # the plant is valid for that environment
                if arboretum.coastlines[0].test_plant(plant_instance):
                    appropriate_environs.append(arboretum.coastlines)
            if len(arboretum.forests) > 0:
                if arboretum.forests[0].test_plant(plant_instance):
                    appropriate_environs.append(arboretum.forests)
            if len(arboretum.grasslands) > 0:
                if arboretum.grasslands[0].test_plant(plant_instance):
                    appropriate_environs.append(arboretum.grasslands)
            if len(arboretum.mountains) > 0:
                if arboretum.mountains[0].test_plant(plant_instance):
                    appropriate_environs.append(arboretum.mountains)
            if len(arboretum.rivers) > 0:
                if arboretum.rivers[0].test_plant(plant_instance):
                    appropriate_environs.append(arboretum.rivers)
            if len(arboretum.swamps) > 0:
                if arboretum.swamps[0].test_plant(plant_instance):
                    appropriate_environs.append(arboretum.swamps)
            return appropriate_environs
        
        #Present menu options
        header(title)
        
        print("1. Mountain Apple Tree")
        print("2. Silversword")
        print("3. Rainbow Eucalyptus Tree")
        print("4. Blue Jade Vine")
        print("0. Return to main menu")
        
        #Present and handle choice
        choice = input("Choose plant to cultivate > ")
        plant = ""
        if choice == "1":
            plant = MountainAppleTree()
        
        elif choice == "2":
            plant = Silversword()
        
        elif choice == "3":
            plant = RainbowEucalyptusTree()    
        
        elif choice == "4":
            plant = BlueJadeVine()
            
        elif choice == "0":
            return 0
            
        else: 
            input(f"Choose a valid option. Hit ENTER to try again. >")
            step_one()
        
        #build a list of environment appropriate environ instances    
        environs = determine_environs(plant)
        
        # move on to step two, with 
        # the appropriate environ instances 
        # and selected plant instance 
        if len(environs) > 0:       
            step_two(environs, plant) 
        else:
            input("There are no appropriate environments for that plant. Press ENTER to choose a new plant. > ")
            step_one()
                
    # Choosing an environment for the plant        
    def step_two(list_of_instance_lists, plant_instance): 
        os.system('cls' if os.name == 'nt' else 'clear')
        header(title)
        # Start an empty list to put the environments in
        possible_environ_instances = []      
            
        def build_instance_list():
            for instance_list in list_of_instance_lists:
                for instance in instance_list:
                    possible_environ_instances.append(instance)
        
        def print_instance_list():
            for instance in possible_environ_instances:
                index = possible_environ_instances.index(instance)
                plant_count = instance.get_plant_count()
                print(f"{index + 1}. {instance} ({plant_count} plants)")
                    
        build_instance_list()
        print_instance_list()
        print("0. Return to main menu")
        
        choice = input(f"Choose environment to plant {plant_instance} > ")
        # If choice is not an integer, it will trigger the exception
        if choice == "0":
            return 0
        try: 
            index = int(choice) - 1
            # If index is between 0 and 1- the list length:
            #Checking if the choice is within the correct index range:
            if index >= 0 and index < len(possible_environ_instances):
                # Choose the matching environment index
                environment = possible_environ_instances[index]
                confirm = input(f"Add {plant_instance} to {environment}: y/n? > ")
                if confirm == "y":
                    environment.add_plant(plant_instance)
                    print(f"{plant_instance} added to {environment}")
                else:
                    step_two(list_of_instance_lists, plant_instance)
            else:
                input(f"Choose a valid option. Hit ENTER to try again. >")
                step_two(list_of_instance_lists, plant_instance)
        except ValueError:
            input(f"Choose a valid option. Hit ENTER to try again. >")
            step_two(list_of_instance_lists, plant_instance)

        
    step_one()