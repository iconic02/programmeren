# wk8ex1.py
# Practicum 8
#
# Naam:
#

# laat deze importregel staan...
from png import *


#
# een testfunctie...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image  test.png in the same directory
    """
    im = PNGImage(300, 200)  # maak een afbeelding met width=300, height = 200

    # Geneste lussen!
    for r in range(200):  # lust over de rijen met lusvariabele r
        for c in range(300):  # lust over de kolommen met c
            if c == r:
                im.plot_point(c, r, (255, 0, 0))
            # else:
            #    im.plot_point( c, r, (255,0,0))

    im.save_file()


def mult(c, n):
    """mult geeft c * n maar met gebruik van een for loop en addition

    Args:
        c (float): een float die we n keer gaan optellen
        n (int): positieve int
    """
    result = 0
    for i in range(n):
        result += c
    return result

assert mult(3, 5) == 15
assert mult(6, 7) == 42
assert mult(1.5, 28) == 42.0


def update(c, n):
    """update de basisstap van de mandelbrotverzameling

    Args:
        c (int): constante c
        n (int): aantal herhalingen
    """
    z = 0
    for i in range(n):
        z = z ** 2 + c 
    return z

assert update(1, 3) == 5
assert update(-1, 3) == -1
assert update(1, 10) == 3791862310265926082868235028027893277370233152247388584761734150717768254410341175325352026
assert update(-1, 10) == 0


def in_mset(c, n):
    """in_mset geeft true als c in mandelbrotverzamelings is, en false als niet.


    Args:
        c (float): complex getal
        n (int): integer n, hoe vaak we het uitvoeren
    """
    z = 0
    for i in range(n):
        z = z ** 2 + c 
        if abs(z) > 2:
            return False
    return True
    

def we_want_this_pixel(col, row):
    """
    Functie geeft true of false als pixel is tiental

    Col: int: pixel colomn
    Row: int: pixel row
    """
    if col % 10 == 0 and row % 10 == 0:
        return True
    else:
        return False


def test():
    """Laat zien hoe je een png maakt en opslaat

    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # maak een lus om wat pixels te tekenen

    for col in range(width):
        for row in range(height):
            if we_want_this_pixel(col, row):
                image.plot_point(col, row)

    # we hebben door alle pixels gelust; nu schrijven we het bestand

    image.save_file()

#Ik denk dat er lijnen ontstaan op de lijnen van 10 pixels.
#Dus een ruitjesveld met dezelfde ruimte tussen lijnen.


def scale(pix, pix_max, float_min, float_max):
    """scale Schaalt coördinaten op met een min en max float

    Args:
        pix (int): huidige pixelwaarde
        pix_max (int): maximum pixelwaarde
        float_min (float): minimale waarde, bij 0,200 pixel 0
        float_max (float): dit is wat terugkomt als pix = pix_max
    """
    if pix < 0 or pix_max <= 0:
        return
    waarde = (pix / pix_max) * (float_max - float_min) + float_min
    
    return waarde

assert scale(100, 200, -2.0, 1.0) == -0.5
assert scale(100, 200, -1.5, 1.5) == 0.0
assert scale(100, 300, -2.0, 1.0) == -1.0
assert scale(25, 300, -2.0, 1.0) == -1.75


def mset():
    """mset mandelbrot in zwart wit
    """
    #4k;  3840 2160 
    #8k;  7680 4320
    NUM_ITER = 25 #aantal updates
    width = 3840
    height = 2160
    XMIN = -2.0
    XMAX = 1.0
    YMIN = -1.0
    YMAX = 1.0

    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            #zet x waarde en y waarde
            x = scale(col, width, XMIN, XMAX)
            y = scale(row, height, YMIN, YMAX)
            #mandelbrot check
            c = x + y * 1j
            if in_mset(c, NUM_ITER):
                image.plot_point(col, row, (255, 175, 0))
            else:
                image.plot_point(col, row, (0,0,0))

    #en opslaan
    image.save_file()
