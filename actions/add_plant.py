import os
from plants import RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine

def add_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
        
    # Choosing a plant to cultivate
    def step_one():
        # Build a list of appropriate environment instances
        # based on the duck-type checks of the environments'
        # add_plant methods
        def determine_environs(plant_instance):
            appropriate_environs = []                
            if len(arboretum.coastlines) > 0:
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
        print("1. Mountain Apple Tree")
        print("2. Silversword")
        print("3. Rainbow Eucalyptus Tree")
        print("4. Blue Jade Vine")
        
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
            
        else: 
            step_one()
            
        environs = determine_environs(plant)
        step_two(environs, plant)        
            
    # Choosing an environment for the plant        
    def step_two(list_of_instance_lists, plant_instance): 
        os.system('cls' if os.name == 'nt' else 'clear')
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
        
        choice = input(f"Choose environment to plant {plant_instance} > ")
        index = int(choice) - 1 
        environment = possible_environ_instances[index]
        confirm = input(f"Add {plant_instance} to {environment}: y/n ?")
        if confirm == "y":
            environment.add_plant(plant_instance)
            print(f"{plant_instance} added to {environment}")
        
    step_one()