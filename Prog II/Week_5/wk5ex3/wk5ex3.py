#
# wk5ex3.py
# https://web.stanford.edu/class/cs101/image-6-grayscale-adva.html
#

from png import *
from random import *


def change(p):
    """ change takes in a pixel (an [R,G,B] list)
        and returns a new pixel to take its place!
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    return [255 - red, 255 - green, 255 - blue]


def invert(image):
    """ run this function to read in the in.png image,
        change it, and write out the result to out.png
    """
    im_pix = get_rgb(image)  # lees het bestand in.png in
    print("De eerste twee pixels van de eerste rij zijn", im_pix[0][0:2])
    #
    # Onthoud dat im_pix een lijst (de afbeelding) van
    # lijsten (elke rij) van lijsten (elke pixel is [R,G,B]) is
    #
    new_pix = [[change(p) for p in row] for row in im_pix]
    # sla nu het bestand 'out.png' op
    save_rgb(new_pix, 'out.png')


def colorless(p):
    """colorless neemt een pixel en verandert dit

    Args:
        p (list): lijst met rgb waardes
    """
    red = int(p[0] * 0.21)
    green = int(p[1] * 0.72)
    blue = int(p[2] * 0.07)
    new_pix = red + green + blue
    return [new_pix, new_pix, new_pix]


def grayscale():
    """grayscale neemt een foto een maakt deze zwart-wit

    Args:
        image (image): een foto
    """
    im_pix = get_rgb('spam.png')

    new_pix = [[colorless(p) for p in row] for row in im_pix]

    save_rgb(new_pix, 'out.png')


def makeBinary(p, thresh):
    red = int(p[0] * 0.21)
    green = int(p[1] * 0.72)
    blue = int(p[2] * 0.07)
    new_pix = red + green + blue
    if new_pix > thresh:
        new_pix = 255
    elif new_pix < thresh:
        new_pix = 0
    return [new_pix, new_pix, new_pix]


def binarize(thresh):
    """binarize maakt zwart wit met drempelwaarde

    Args:
        thresh (int): threshold tussen 0 en 255
    """
    im_pix = get_rgb('spam.png')

    new_pix = [[makeBinary(p, thresh) for p in row] for row in im_pix]

    save_rgb(new_pix, 'out.png')


def vert_flipper(pix):
    """vert_flipper extra functie omdat het moet

    pix: list: lijst met pixels
    """
    new_pix = pix[::-1]
    return new_pix


def flip_vert():
    """flip_vert neemt image en draait deze om zodat het op de kop staat
    """
    im_pix = get_rgb('in.png')

    new_pix = vert_flipper(im_pix)

    save_rgb(new_pix, 'out.png')


def horiz_flipper(pix):
    """horiz_flipper neemt pixel rij en flipt deze

    Args:
        pix (list): lijst voor de rij pixels
    """
    new_pix = pix[::-1]
    return new_pix


def flip_horiz():
    """flip_horiz draait een image horizontaal
    """
    im_pix = get_rgb('spam.png')

    new_pix = [horiz_flipper(row) for row in im_pix]

    save_rgb(new_pix, 'out.png')

def mirror_vert():
    """mirror_vert neemt foto en spiegelt deze op horizontale as
    """
    im_pix = get_rgb('in.png')

    pixwh = get_wh(im_pix)
    firstHalf = im_pix[0: pixwh[1]//2]
    secondHalf = firstHalf[::-1]
    new_pix = firstHalf + secondHalf

    save_rgb(new_pix, 'out.png')


def horiz_help(pix):
    """horiz_help flipt elke rij een voor een

    pix: list: rij pixels
    """
    pixw = len(pix)
    firstHalf = pix[0 : pixw//2]
    new_pix = firstHalf + firstHalf[::-1]
    return new_pix


def mirror_horiz():
    """mirror_horiz neemt foto en spiegelt deze op de verticale as
    """
    im_pix = get_rgb('spam.png')
    
    new_pix = [horiz_help(row) for row in im_pix]

    save_rgb(new_pix, 'out.png')


def scale():
    """scale neemt een foto en verkleint deze naar de helft van de oorspronkelijke afmetingen.
    """
    im_pix = get_rgb('spam.png')

    new_pix = [row[::2] for row in im_pix[::2]]

    save_rgb(new_pix, 'out.png')


