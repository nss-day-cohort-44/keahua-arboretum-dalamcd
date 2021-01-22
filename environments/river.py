from animals import Identifiable
from environments import ContainsAnimals
from environments import ContainsPlants

class River(ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self, name):
      ContainsAnimals.__init__(self)
      ContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.name = name

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
