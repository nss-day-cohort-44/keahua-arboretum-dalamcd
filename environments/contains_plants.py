class ContainsPlants():

    def __init__(self, max):
        self.__plants = []
        self.__max_plants = max

    def add_plant(self, plant):
        if(len(self.__plants) < self.max_plants):
            self.__plants.append(plant)
        else:
            raise OverflowError("This biome already contains the maximum number of supported plants.")

    def remove_plant(self, uuid):
        for plant in self.__plants:
            if uuid == plant["id"]:
                self.__plants.remove[plant]

    @property
    def plant_count(self):
        return len(self.__plants)

    @property
    def max_plants(self):
        return self.__max_plants

    @property
    def plants(self):
        return self.__plants

    @property
    def plants_by_name(self):
        names = []
        for plant in self.__plants:
            names.append(plant.species)
        return names