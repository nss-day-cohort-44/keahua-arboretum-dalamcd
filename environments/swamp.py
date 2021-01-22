from environments import ContainsAnimals, ContainsPlants
from animals import Identifiable
# from animals.


class Swamp(ContainsPlants, ContainsAnimals, Identifiable):

    def __init__(self, name):
      ContainsAnimals.__init__(self)
      ContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.name = name

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.stagnant_water:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, saltwater, or creatues which require non-stagnant water to a swamp.")

    def __str__(self):
        return self.name
