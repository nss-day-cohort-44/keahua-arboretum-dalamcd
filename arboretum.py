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

    @property
    def mountains(self):
        arr = []
        for biome in self.__biomes:
            if(biome.biome_type == "mountain"):
                arr.append(biome)
        return arr

    @property
    def swamps(self):
        arr = []
        for biome in self.__biomes:
            if(biome.biome_type == "swamp"):
                arr.append(biome)
        return arr
        
    @property
    def coastlands(self):
        arr = []
        for biome in self.__biomes:
            if(biome.biome_type == "coastland"):
                arr.append(biome)
        return arr

    @property
    def grasslands(self):
        arr = []
        for biome in self.__biomes:
            if(biome.biome_type == "grassland"):
                arr.append(biome)
        return arr