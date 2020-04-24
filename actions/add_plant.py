import os
from arboretum import Arboretum


def add_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    def get_environ_instances(environ):
        environ_instances = Arboretum.environ
        i = 1
        for environ_instance in environ_instances:
            print(f"{i}. {environ_instance}")
            i += 1

        new_choice = input("> ")

    choice = input("Choose plant to cultivate > ")

    def what_environment(environment):
        pass

    if choice == "1":
        # TODO: fix this to be duck-typed
        pass

    if choice == "2":
        # TODO: fix this to be duck-typed
        return Arboretum.rivers

    if choice == "3":
        # TODO: fix this to be duck-typed
        return Arboretum.swamps

    if choice == "4":
        # TODO: fix this to be duck-typed
        return Arboretum.forests
