import os
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.add_plant import add_plant
from actions.report import build_facility_report
from actions.feed_animal import feed_animal
from actions.save_state import read_text, write_text, clear_text
from tester import mass_add_to_environs
from actions.header import header

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    header("Keahua Arboretum")

    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Save and Exit")
    print("0. Clear Data and Exit")
    #"Secret Seven": Seed Data with Tester Script


def main_menu():
    """Show Keahua Action Options
    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        add_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)

    if choice == "6":
        write_text(keahua)

    #"Secret Seven": seed data with tester script
    if choice == "7":
        mass_add_to_environs(keahua)
        
    if choice == "0":
        clear_text()
        
    if choice != "6" and choice != "0":
        main_menu()
        
read_text(keahua)
main_menu()
