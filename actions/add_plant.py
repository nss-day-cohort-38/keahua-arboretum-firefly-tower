import os
from plants import RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine

def add_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
        
    # Choosing a plant to cultivate
    def step_one():
        print("1. Mountain Apple Tree")
        print("2. Silversword")
        print("3. Rainbow Eucalyptus Tree")
        print("4. Blue Jade Vine")
        
        choice = input("Choose plant to cultivate > ")
        
        def cultivate_plant(environment):
            plant = environment()
            print(f"{plant} cultivated")
        
        if choice == "1":
            #TODO: fix this to be duck-typed
            cultivate_plant(MountainAppleTree)
            step_two([arboretum.mountains], plant)        
        
        if choice == "2":
            #TODO: fix this to be duck-typed
            cultivate_plant(Silversword)
            step_two([arboretum.grasslands], plant)
        
        if choice == "3":
            #TODO: fix this to be duck-typed
            cultivate_plant(RainbowEucalyptusTree)
            step_two([arboretum.forests], plant)
        
        if choice == "4":
            #TODO: fix this to be duck-typed
            cultivate_plant(BlueJadeVine)
            step_two([arboretum.forests, arboretum.swamps], plant)
            
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
                print(f"{index + 1}. {instance}")
                    
        build_instance_list()
        print_instance_list()
        
        choice = input(f"Choose environment to plant {plant_instance} > ")
        index = int(choice) - 1 
        environment = possible_environ_instances[index]
        environment.add_plant(plant_instance)
        print(f"{plant_instance} added to {environment}")
        
    step_one()