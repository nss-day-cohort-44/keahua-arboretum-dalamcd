from typing import Counter


def build_facility_report(arboretum):

    print("Rivers:")
    for biome in arboretum.rivers:
        tmp = "         ("
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for (species, num) in Counter(biome.animals_by_name + biome.plants_by_name).most_common():
            tmp += f"{num} {species}, "
        if len(tmp) > 10:
            print(f"{tmp[0:-2]})")

    print("\nMountains:")
    for biome in arboretum.mountains:
        tmp = "         ("
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for (species, num) in Counter(biome.animals_by_name + biome.plants_by_name).most_common():
            tmp += f"{num} {species}, "
        if len(tmp) > 10:
            print(f"{tmp[0:-2]})")

    print("\nGrasslands:")
    for biome in arboretum.grasslands:
        tmp = "         ("
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for (species, num) in Counter(biome.animals_by_name + biome.plants_by_name).most_common():
            tmp += f"{num} {species}, "
        if len(tmp) > 10:
            print(f"{tmp[0:-2]})")

    print("\nSwamps:")
    for biome in arboretum.swamps:
        tmp = "         ("
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for (species, num) in Counter(biome.animals_by_name + biome.plants_by_name).most_common():
            tmp += f"{num} {species}, "
        if len(tmp) > 10:
            print(f"{tmp[0:-2]})")

    print("\nCoastlines:")
    for biome in arboretum.coastlands:
        tmp = "         ("
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for (species, num) in Counter(biome.animals_by_name + biome.plants_by_name).most_common():
            tmp += f"{num} {species}, "
        if len(tmp) > 10:
            print(f"{tmp[0:-2]})")

    print("\nForests:")
    for biome in arboretum.forests:
        tmp = "         ("
        print(f'    {biome.name} [{biome.id.hex[0:8]}]:')
        for (species, num) in Counter(biome.animals_by_name + biome.plants_by_name).most_common():
            tmp += f"{num} {species}, "
        if len(tmp) > 10:
            print(f"{tmp[0:-2]})")

    input("\n\nPress any key to continue...")