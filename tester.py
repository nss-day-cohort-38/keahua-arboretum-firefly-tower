## FOR TESTING PURPOSES
import random
from animals import Animal, GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae
from plants import RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine
from environments import River, Swamp, Forest, Mountain, Coastline, Grassland 

animal_classes = [GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae]
plant_classes = [RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine]
environment_classes = [Coastline, Forest, Grassland, Mountain, River, Swamp]

names = ["Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin", "Charlotte", "Tegan", "Darby", "Eisley", "Furlough", "Anthony", "Stuck", "Beef"]  

def mass_add_to_environs(arboretum):
  
    def annex(environment_instance):
      annex_method = ""
      #Depending on what class the instance is, 
      #change the annex_method
      if isinstance(environment_instance, River):
          annex_method = arboretum.rivers.append
      elif isinstance(environment_instance, Grassland):
          annex_method = arboretum.grasslands.append
      elif isinstance(environment_instance, Coastline):
          annex_method = arboretum.coastlines.append
      elif isinstance(environment_instance, Mountain):
          annex_method = arboretum.mountains.append
      elif isinstance(environment_instance, Swamp):
          annex_method = arboretum.swamps.append
      elif isinstance(environment_instance, Forest):
          annex_method = arboretum.forests.append
      annex_method(environment_instance)
  
    for environment_class in environment_classes:
      print("-----------------------------------")
      #create a new environment instance
      environment_instance = environment_class()
      annex(environment_instance)
      # annex(environment_instance)
      #loop through all animal classes
      for animal_class in animal_classes:
          #Choose a random name:
          name  = random.choice(names)
          #create an animal instance, pass in an age and name
          age = 0
          animal_instance = animal_class(age, name)
          #add the animal instance to the current environment instance
          environment_instance.add_animal(animal_instance)
      #print the list of animals in the environment
      print(f"Animals in {environment_instance}", environment_instance.animals)
      print()
      #loop through every plant class
      for plant_class in plant_classes:
          #create a plant instance
          plant_instance = plant_class()
          #add the plant to the current environment instance
          environment_instance.add_plant(plant_instance)
      #print the list of plants in the environment
      print(f"Plants in {environment_instance}", environment_instance.plants)




#Loop through a list of classes, initialize instances of them, and then print all that instances attributes
def printAllClassesAttributes(class_list):
  def printAttrs(instance):
    for attr in dir(instance):
        if(attr[:2] != "__"): # don't print anything starting with dunderscore
            print(attr, getattr(instance, attr))
  
  for clss in class_list:
      print()
      #Get an index
      i = class_list.index(clss)
      #Use the index to claim a name
      name = names[i]
      #Create an instance
      #if animals
      instance_name = clss(5, name)
    #   instance_name = clss()
      #Print attributes of the instance
      print("Species", instance_name.species)
    #   print("Seeds Produced", instance_name.seeds_produced)
      print("All Attributes:")
      printAttrs(instance_name)

#Call the function and pass in class list        
# classLoop(plant_classes)
# classLoop(animal_classes)

# mass_add_to_environs()