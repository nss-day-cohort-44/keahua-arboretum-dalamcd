from plants import Plant
from animals import Identifiable

class Apple(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", ["mountain"])
        Identifiable.__init__(self)

    def __str__(self):
        return f"{self.species} ({self.id.hex[0:8]})."
