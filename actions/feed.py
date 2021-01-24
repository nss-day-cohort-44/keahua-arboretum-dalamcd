from animals import RiverDolphin, Gecko, NeneGoose, Kikakapu, Pueo, Ulae, OpeApeA, HappySpider

def feed_animal(arboretum):

	choice = int(input("""1. Gold Dust Day Gecko
2. River Dolphin
3. Nene Goose
4. Kīkākapu
5. Pueo
6. 'Ulae
7. Ope'ape'a
8. Happy-Face Spider

Choose animal to feed.
> """))

	if choice == 1:
		animal = Gecko()
	elif choice == 2:
		animal = RiverDolphin()
	elif choice == 3:
		animal = NeneGoose()
	elif choice == 4:
		animal = Kikakapu()
	elif choice == 5:
		animal = Pueo()
	elif choice == 6:
		animal = Ulae()
	elif choice == 7:
		animal = OpeApeA()
	elif choice == 8:
		animal = HappySpider()
	else:
		animal = None
		print("Not a valid option.")

	if animal:
		for index, feed in enumerate(animal.prey):
			print(f"{index + 1}. {feed}")

		print(f"What is on the menu for the {animal.species} today?")
		choice = int(input("> "))

		if choice > 0 and choice <= len(animal.prey):
			animal.feed(animal.prey[choice - 1])
		else:
			print("Not a valid option.")