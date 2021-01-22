class ContainsAnimals():

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, uuid):
        for animal in self.animals:
            if uuid == animal["id"]:
                self.animals.remove[animal]

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"
