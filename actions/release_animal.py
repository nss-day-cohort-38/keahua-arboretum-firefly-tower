from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import HawaiianHappyFaceSpider
from animals import Kikakapu
from animals import NeneGoose
from animals import Opeapea
from animals import Ulae
from animals import Pueo


def release_animal(arboretum):
    animal = None
    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Hawaiian Happy Face Spider")
    print("4. Kikakapu")
    print("5. Nene Goose")
    print("6. Ope Ape A")
    print("7. Pueo")
    print("8. Ulae")


    choice = input("Choose animal to release > ")


    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        animal = GoldDustDayGecko(5, "Looser")

    if choice == "3":
        animal = HawaiianHappyFaceSpider()

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = NeneGoose()

    if choice == "6":
        animal = Opeapea()

    if choice == "7":
        animal = Pueo()

    if choice == "8":
        animal = Ulae()

    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')
    print("Release the animal into which biome?")
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")
    choice = input("> ")
    if choice == "1":
      arboretum.rivers[int(choice) - 1].animals.append(animal)
