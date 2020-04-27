## FOR TESTING PURPOSES, DELETE OR GITIGNORE

from animals import Animal, GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae
# from plants import RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine

animal_classes = [GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae]

# plant_classes = [RainbowEucalyptusTree, Silversword, MountainAppleTree, BlueJadeVine]

names = ["Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin", "Charlotte"]  

#Print all of the attributes of an instance
def printAttrs(instance):
    for attr in dir(instance):
        if(attr[:2] != "__"): # don't print anything starting with dunderscore
            print(attr, getattr(instance, attr))

#Loop through a list of classes
def classLoop(class_list):
  for clss in class_list:
      print()
      #Get an index
      i = class_list.index(clss)
      #Use the index to claim a name
      name = names[i]
      #Create an instance
      instance_name = clss(5, name)
      #Print attributes of the instance
      printAttrs(instance_name)

#Call the function and pass in class list        
classLoop(animal_classes)