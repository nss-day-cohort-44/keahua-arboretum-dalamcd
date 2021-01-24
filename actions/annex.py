import os
from environments import River, Swamp, Coastline, Grassland, Forest, Mountain

def annex_habitat(arboretum):
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain")

    biome = input("Choose your habitat > ")
    name = input("Name > ")

    if biome == "1":
        new_biome = River(name)
        arboretum.add_biome(new_biome)
        for river in arboretum.rivers:
            print(river)
    if biome == "2":
        new_biome = Swamp(name)
        arboretum.add_biome(new_biome)
    if biome == "3":
        new_biome = Coastline(name)
        arboretum.add_biome(new_biome)
    if biome == "4":
        new_biome = Grassland(name)
        arboretum.add_biome(new_biome)
    if biome == "5":
        new_biome = Forest(name)
        arboretum.add_biome(new_biome)
    if biome == "6":
        new_biome = Mountain(name)
        arboretum.add_biome(new_biome)
    
    print(f"Successfully annexed {name} to the arboretum.")
