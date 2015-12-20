from osnovniDelec import osnovniDelec
from okolje import okolje
from podlaga import podlaga
import pygame
import sys
from pygame.locals import *
ura = pygame.time.Clock()


# OKOLJE
glavnoOkolje = okolje(400,450,"Osnova")
okolje.lastnostiOkolja(glavnoOkolje)

# PODLAGA
trenutnaPodlaga = podlaga(glavnoOkolje)

# DELEC
prviDelec = osnovniDelec(glavnoOkolje, 10, (0,0,0))
prviDelec.lokacijaDelca()

pygame.init()
ZASLON = pygame.display.set_mode((glavnoOkolje.sirina, glavnoOkolje.visina))

pygame.display.set_caption(glavnoOkolje.naslov)



def ukazTipkovniceDelec(keys, trenutni):
    if keys[K_LEFT]:
        trenutni.pojdiLevo(1)

    if keys[K_RIGHT]:
        trenutni.pojdiDesno(1)

    if keys[K_UP]:
        trenutni.pojdiGor(1)

    if keys[K_DOWN]:
        trenutni.pojdiDol(1)

    if keys[K_ESCAPE]:
        exit()

def posodobitevDelca(delec):
    delec.popraviLokacijo(delec.lokacijaX,delec.lokacijaY)
    print delec.lokacija





while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.circle(ZASLON, prviDelec.barva, prviDelec.lokacija,5)
    keys = pygame.key.get_pressed()

    ukazTipkovniceDelec(keys,prviDelec)
    posodobitevDelca(prviDelec)


    pygame.draw.line(ZASLON, trenutnaPodlaga.barvaPodlage,  (trenutnaPodlaga.leviX,trenutnaPodlaga.leviY),(trenutnaPodlaga.desniX,trenutnaPodlaga.desniY),trenutnaPodlaga.debelinaCrte)

    ura.tick(glavnoOkolje.tikataka)
    pygame.display.update()
    ZASLON.fill(glavnoOkolje.ozadje)
