## FOR TESTING PURPOSES

from animals import Animal, GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae
from plants import RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine
# TODO: add all biomes
from environments import River

animal_classes = [GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae]
plant_classes = [RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine]
environment_classes = [River]

names = ["Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin", "Charlotte"]  

def mass_add_to_environs(class_list):
    for environment_class in environment_classes:
      print()
      #Get an index
      i = environment_class.index(environment_class)
      #Use the index to claim a name
      name = names[i]


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