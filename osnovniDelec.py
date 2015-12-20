from okolje import okolje

class osnovniDelec:
    def __init__(self, lastnostiOkolja, polmer, barva):
        self.lokacijaX = (lastnostiOkolja.sirina/2)
        self.lokacijaY = (lastnostiOkolja.visina/2)
        self.lokacija = (self.lokacijaX,self.lokacijaY)
        self.polmer = polmer
        self.barva = barva
        print "Osnovni delec ustvarjen..."

    def lokacijaDelca(self):
        print self.lokacijaX, self.lokacijaY

    def pojdiLevo(self,korak):
        self.lokacijaX -=korak

    def pojdiDesno(self, korak):
        self.lokacijaX += korak

    def pojdiGor(self, korak):
        self.lokacijaY -= korak

    def pojdiDol(self, korak):
        self.lokacijaY += korak

    def popraviLokacijo(self, lokacijax, lokacijay):
        self.lokacija = (lokacijax,lokacijay)
