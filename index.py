import os
from arboretum import Arboretum
from environments import River, Swamp, Coastline, Forest, Grassland, Mountain
from animals import RiverDolphin, Gecko
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report
from actions.feed import feed_animal
from actions.add_plant import add_plant

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

keahua.add_biome(River("River 1"))
keahua.add_biome(River("River 2"))

keahua.add_biome(Coastline("Coastline 1"))
keahua.add_biome(Coastline("Coastline 2"))

keahua.add_biome(Swamp("Swamp 1"))
keahua.add_biome(Swamp("Swamp 2"))

keahua.add_biome(Forest("Forest 1"))
keahua.add_biome(Forest("Forest 2"))

keahua.add_biome(Grassland("Grassland 1"))
keahua.add_biome(Grassland("Grassland 2"))

keahua.add_biome(Mountain("Mountain 1"))
keahua.add_biome(Mountain("Mountain 2"))

gecko = Gecko()
print(gecko)

def build_menu():
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")


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
        pass

    if choice != "6":
        main_menu()

main_menu()
