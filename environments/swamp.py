from environments import ContainsAnimals, ContainsPlants
from animals import Identifiable

class Swamp(ContainsPlants, ContainsAnimals, Identifiable):

    def __init__(self, name):
      ContainsAnimals.__init__(self, 8)
      ContainsPlants.__init__(self, 12)
      Identifiable.__init__(self)
      self.name = name

    def add_animal(self, animal):
        try:
            if animal.aquatic and not animal.requires_current:
               super().add_animal(animal)
            else:
                print("Cannot add non-aquatic, saltwater, or creatues which require non-stagnant water to a swamp.")
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, saltwater, or creatues which require non-stagnant water to a swamp.")

    def __str__(self):
        return self.name
