from animals import GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae

def feed_animal(arboretum):
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
        for index, prey in enumerate(GoldDustDayGecko.prey):
            print(f'{index + 1}. {prey}')

    if choice == "2":
        pass

    if choice == "3":
        pass

    if choice == "4":
        pass

    if choice == "5":
        pass

    if choice == "6":
        pass

    if choice == "7":
        pass

    if choice == "8":
        pass