class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__biomes = []

    def add_biome(self, biome):
        self.__biomes.append(biome)

    @property
    def biomes(self):
        return self.__biomes
    
    @property
    def rivers(self):
        arr = []
        for biome in self.__biomes:
            if(biome.biome_type == "river"):
                arr.append(biome)
        return arr