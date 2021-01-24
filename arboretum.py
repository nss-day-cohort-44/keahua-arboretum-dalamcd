class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__rivers = []
        self.__grasslands = []
        self.__mountains = []
        self.__forests = []
        self.__coastlines = []
        self.__swamps = []

        def add_river(river):
            self.__rivers.append(river)

        def add_grassland(grassland):
            self.__grasslands.append(grassland)
    
        def add_mountain(mountain):
            self.__mountains.append(mountain)
            
        def add_forest(forest):
            self.__forests.append(forest)
            
        def add_coastline(coastline):
            self.__coastlines.append(coastline)
            
        def add_swamp(swamp):
            self.__swamps.append(swamp)