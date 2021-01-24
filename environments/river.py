from environments import ContainsAnimals, ContainsPlants
from animals import Identifiable

class River(ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self, name):
      ContainsAnimals.__init__(self, 12)
      ContainsPlants.__init__(self, 6)
      Identifiable.__init__(self)
      self.name = name

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                super().add_animal(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                super().add_plant(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")

    def __str__(self):
        return self.name
