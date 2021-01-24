class Animal:

    def __init__(self, species, biomes):
        self.species = species
        self.age = 0
        self.biome_types = biomes

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
