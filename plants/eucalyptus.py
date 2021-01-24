from plants import Plant
from animals import Identifiable

class Eucalyptus(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", ["forest"])
        Identifiable.__init__(self)

    def __str__(self):
        return f"{self.species} ({self.id.hex[0:8]})."
