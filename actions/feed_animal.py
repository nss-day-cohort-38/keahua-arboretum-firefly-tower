from animals import GoldDustDayGecko, HawaiianHappyFaceSpider, Kikakapu, NeneGoose, Opeapea, Pueo, RiverDolphin, Ulae

def feed_animal(arboretum):
    animal = None

    gecko = GoldDustDayGecko(5, "Simon")
    spider = HawaiianHappyFaceSpider(5, "George")
    kikakapu = Kikakapu(5, "Nancy")
    goose = NeneGoose(5, "Bob")
    opeapea = Opeapea(5, "Jenny")
    pueo = Pueo(5, "Izzy")
    dolphin = RiverDolphin(5, "Denny")
    ulae = Ulae(5, "Sarah")

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
        animal = gecko
        for index, prey in enumerate(gecko.prey):
            print(f'{index + 1}. {prey}')

    if choice == "2":
        animal = spider
        for index, prey in enumerate(spider.prey):
            print(f'{index + 1}. {prey}')

    if choice == "3":
        animal = kikakapu
        for index, prey in enumerate(kikakapu.prey):
            print(f'{index + 1}. {prey}')

    if choice == "4":
        animal = goose
        for index, prey in enumerate(goose.prey):
            print(f'{index + 1}. {prey}')

    if choice == "5":
        animal = opeapea
        for index, prey in enumerate(opeapea.prey):
            print(f'{index + 1}. {prey}')

    if choice == "6":
        animal = pueo
        for index, prey in enumerate(pueo.prey):
            print(f'{index + 1}. {prey}')

    if choice == "7":
        animal = dolphin
        for index, prey in enumerate(dolphin.prey):
            print(f'{index + 1}. {prey}')

    if choice == "8":
        animal = ulae
        for index, prey in enumerate(ulae.prey):
            print(f'{index + 1}. {prey}')
        print("Choose what to feed it")
        choice = input("> ")
        
        print(ulae.prey(choice))

    

