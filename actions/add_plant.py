from plants import Eucalyptus, Silversword, Apple, BlueJade

def add_plant(arboretum):
	animal = None

	print("1. Rainbow Eucalyptus Tree")
	print("2. Silversword")
	print("3. Mountain Apple Tree")
	print("4. Blue Jade Fine")

	choice = input("Choose plant to cultivate > ")

	if choice == "1":
		plant = Eucalyptus()
	elif choice == "2":
		plant = Silversword()
	elif choice == "3":
		plant = Apple()
	elif choice == "4":
		plant = BlueJade()
	else:
		plant = None
		print("Not a valid option.")
		add_plant(arboretum)
		return

	if plant:
		avail = []
		for biome in arboretum.biomes:
			if biome.check_suitability(plant):
				avail.append(biome)
				print(f"{len(avail)}. {biome.biome_type.capitalize()}: {biome.name} ({biome.plant_count} plants)")

		option = input("Select biome > ")
		try:
			avail[int(option) - 1].add_plant(plant)
		except OverflowError:
			print(f"{avail[int(option) -1].name} already has the maximum number of plants.")
			add_plant(arboretum)
			return
		except IndexError:
			print("Not a valid option.")
			add_plant(arboretum)
			return
		else:
			print(f"Added {plant.species} to {avail[int(option) - 1].name}!")

