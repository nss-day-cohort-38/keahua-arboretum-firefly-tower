import os

def add_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    
    def create_environ_options(instance_list, *args): 
        i = 1
        
        for instance in instance_list:
            print(f"{i}. {instance}")
            i += 1
        
        #If there is a second environment,
        #continue the list of options
        if len(args) > 0:
            #Note: args in this instance returns a single list within a tuple
            #so we're using this index to get that single list
            for instance in args[0]:
                print(f"{i}. {instance}")
                i+= 1
            
        new_choice = input("Choose environment to plant in > ")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        #TODO: fix this to be duck-typed
        create_environ_options(arboretum.mountains)        
        pass
      
    if choice == "2":
        #TODO: fix this to be duck-typed
        create_environ_options(arboretum.grasslands)
      
    if choice == "3":
        #TODO: fix this to be duck-typed
        create_environ_options(arboretum.forest)
    
    if choice == "4":
        #TODO: fix this to be duck-typed
        create_environ_options(arboretum.forests, arboretum.swamps)
