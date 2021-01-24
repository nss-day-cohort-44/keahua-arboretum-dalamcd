from animals import RiverDolphin, Gecko, HappySpider, Kikakapu, NeneGoose, OpeApeA, Pueo, Ulae

def release_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Ope'ape'a")
    print("3. Pueo")
    print("4. Ulae")
    print("5. Gold Dust Day Gecko")
    print("6. Nene Goose")
    print("7. Kikakapu")
    print("8. Hawaiian Happy-Face Spider")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()
    if choice == "2":
        animal = OpeApeA()
    if choice == "3":
        animal = Pueo()
    if choice == "4":
        animal = Ulae()
    if choice == "5":
        animal = Gecko()
    if choice == "6":
        animal = NeneGoose()
    if choice == "7":
        animal = Kikakapu()
    if choice == "8":
        animal = HappySpider()

    avail = []
    for biome in arboretum.biomes:
        if biome.check_suitability(animal):
            avail.append(biome)
            print(f"{len(avail)}. {biome.biome_type.capitalize()}: {biome.name}")
    
    option = input("Select biome > ")

    avail[int(option) - 1].add_animal(animal)

    print(f"Added {animal.species} to {avail[int(option) - 1].name}!")


    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.append(animal)


