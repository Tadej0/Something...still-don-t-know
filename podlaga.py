from okolje import okolje

class podlaga:
    def __init__(self, okolje):
        self.dvignjeno = 10
        self.leviX = 0
        self.leviY = okolje.visina - self.dvignjeno
        self.desniX = okolje.sirina
        self.desniY = okolje.visina - self.dvignjeno
        self.barvaPodlage = (0,0,0)
        self.debelinaCrte = 1

