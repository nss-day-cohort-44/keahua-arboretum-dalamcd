class ContainsAnimals():

    def __init__(self, max):
        self.__animals = []
        self.__max_animals = max

    def add_animal(self, animal):
        if len(self.__animals) < self.max_animals:
            if self.check_suitability(animal):
                self.__animals.append(animal)
        else:
            raise OverflowError("This biome already contains the maximum number of supported animals.")

    def remove_animal(self, uuid):
        for animal in self.__animals:
            if uuid == animal["id"]:
                self.__animals.remove[animal]

    @property
    def animal_count(self):
        return len(self.__animals)

    @property
    def max_animals(self):
        return self.__max_animals
    
    @property
    def animals(self):
        return self.__animals
    
    @property
    def animals_by_name(self):
        names = []
        for animal in self.__animals:
            names.append(animal.species)
        return names