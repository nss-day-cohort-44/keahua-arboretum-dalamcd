from .aquatic import Aquatic

class Stagnant(Aquatic):

    def __init__(self):
        super().__init__()
        self.requires_current = False
