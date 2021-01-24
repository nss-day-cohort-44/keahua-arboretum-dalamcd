class ContainsAnimals():

    def __init__(self, max):
        self.animals = []
        self.__max_animals = max

    def add_animal(self, animal):
        if len(self.animals) < self.max_animals:
            self.animals.append(animal)
        else:
            raise OverflowError("This biome already contains the maximum number of supported animals.")

    def remove_animal(self, uuid):
        for animal in self.animals:
            if uuid == animal["id"]:
                self.animals.remove[animal]

    def animal_count(self):
        return len(self.animals)

    @property
    def max_animals(self):
        return self.__max_animals