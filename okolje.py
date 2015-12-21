class okolje:
    visina = 0
    sirina = 0

    def __init__(self, visina, sirina, naslov):
        self.visina = visina
        self.sirina = sirina
        self.naslov = naslov
        self.ozadje = (255,255,255)
        self.tikataka = 100
        self.gravitacija = 10
        self.vrstaOkolja = 1

        '''
        Vrsta okolja:
        1... svet je omejen na robove
        2... svet je povezan levo desno
        '''

        print "Okolje ustvarjeno..."

    def lastnostiOkolja(trenutni):
        print trenutni.visina
        print trenutni.sirina
        print trenutni.ozadje
        print trenutni.naslov

    def popraviGravitacijo(self, popravek):
        self.gravitacija += popravek

    def definirajVrsto(self, vrednost):
        self.vrstaOkolja = vrednost
