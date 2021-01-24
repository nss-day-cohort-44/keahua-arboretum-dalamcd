def build_facility_report(arboretum):
    print("Rivers:")
    for biome in arboretum.rivers:
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for animal in biome.animals:
            print("        " + str(animal))
        for plant in biome.plants:
            print("        " + str(plant))


    print("\nMountains:")
    for biome in arboretum.mountains:
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for animal in biome.animals:
            print("        " + str(animal))
        for plant in biome.plants:
            print("        " + str(plant))

    print("\nGrasslands:")
    for biome in arboretum.grasslands:
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for animal in biome.animals:
            print("        " + str(animal))
        for plant in biome.plants:
            print("        " + str(plant))

    print("\nSwamps:")
    for biome in arboretum.swamps:
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for animal in biome.animals:
            print("        " + str(animal))
        for plant in biome.plants:
            print("        " + str(plant))

    print("\nCoastlines:")
    for biome in arboretum.coastlands:
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for animal in biome.animals:
            print("        " + str(animal))
        for plant in biome.plants:
            print("        " + str(plant))

    print("\Forests:")
    for biome in arboretum.forests:
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for animal in biome.animals:
            print("        " + str(animal))
        for plant in biome.plants:
            print("        " + str(plant))

    input("\n\nPress any key to continue...")