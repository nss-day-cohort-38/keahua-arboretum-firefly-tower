## FOR TESTING PURPOSES, DELETE PLEASE

from plants import RainbowEucalyptusTree
from plants import Silversword
from plants import MountainAppleTree
from plants import BlueJadeVine

def printAttrs(instance):
  for attr in dir(instance):
    if(attr[:2] != "__"): # don't print anything starting with dunderscore
      print(attr, getattr(instance, attr))

charlie = BlueJadeVine()
printAttrs(charlie)

