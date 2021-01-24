class ContainsPlants():

    def __init__(self, max):
        self.plants = []
        self.__max_plants = max

    def add_plant(self, plant):
        if(len(self.plants) < self.max_plants):
            self.plants.append(plant)
        else:
            raise OverflowError("This biome already contains the maximum number of supported plants.")

    def remove_plant(self, uuid):
        for plant in self.plants:
            if uuid == plant["id"]:
                self.plants.remove[plant]

    def plant_count(self):
        return len(self.plants)

    @property
    def max_plants(self):
        return self.__max_plants