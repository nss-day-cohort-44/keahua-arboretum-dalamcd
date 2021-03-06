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
    elif choice == "2":
        animal = OpeApeA()
    elif choice == "3":
        animal = Pueo()
    elif choice == "4":
        animal = Ulae()
    elif choice == "5":
        animal = Gecko()
    elif choice == "6":
        animal = NeneGoose()
    elif choice == "7":
        animal = Kikakapu()
    elif choice == "8":
        animal = HappySpider()
    else:
        animal = None
        print("Not a valid choice")
        release_animal(arboretum)
        return

    avail = []
    for biome in arboretum.biomes:
        if biome.check_suitability(animal):
            if biome.animal_count < biome.max_animals:
                avail.append(biome)
                print(f"{len(avail)}. {biome.biome_type.capitalize()}: {biome.name} ({biome.animal_count} animals)")
    
    option = input("Select biome > ")
    try:
        avail[int(option) - 1].add_animal(animal)
    except OverflowError:
        print(f"{avail[int(option) -1].name} already has the maximum number of animals.")
        release_animal(arboretum)
        return
    except IndexError:
        print("Not a valid option.")
        release_animal(arboretum)
        return
    else:
        print(f"Added {animal.species} to {avail[int(option) - 1].name}!")


    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.append(animal)


