#Turtle

import time
from turtle import *
from random import *


def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
       Note that n doesn't have to be 3 (!)
    """
    color('darkgreen')
    width(10)
    if n == 0:
        return      # Geen zijden om te tekenen, dus stop met tekenen
    else:
        
        forward(100)
        left(120)
        tri(n-1)    # Gebruik recursie om de overige zijden te tekenen!
    
def spiral(initial_length, angle, multiplier):
    """Spiral-drawing function.  Arguments:
       initial_length = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    if initial_length <= 1 or initial_length > 1000:
        return
    else:
        forward(initial_length)
        left(angle)
        spiral(initial_length*multiplier)

def chai(size):
    """chai vertakkende recursie

    Args:
        size ([type]): [description]
    """
    if size < 5: 
        return
    else:
        forward(size)
        left(90)
        forward(size/2)
        right(90)

        chai(size/2)

        right(90)
        forward(size)
        left(90)

        chai(size/2)

        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

def svtree(trunklength, levels):
    """svtree: Deze functie laat het programma een boom tekenen via recursie.

    trunklength: int, bepaald hoe lang een tak zal worden.
    levels: int, geeft aan hoe lang de boom wordt.
    """
    if levels == 0:       
        return
    else:
        forward(trunklength)
        left(30)
        svtree(trunklength*0.7,levels-1)
        right(60)
        svtree(trunklength*0.7,levels-1)
        left(30)
        backward(trunklength)
        



def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)

def flakeside(sidelength, levels):
    """flakeside Deze functie maakt een kant van de sneeuwvlok.

    Args:
        sidelength (int): het aantal pixels dat de totale kant moet zijn
        levels (int): de diepte van de kant.
    """
    if levels == 0:
        forward(sidelength)
    else:
        flakeside(sidelength/3, levels-1)
        right(60)
        flakeside(sidelength/3, levels-1)
        left(120)
        flakeside(sidelength/3, levels-1)
        right(60)
        flakeside(sidelength/3, levels-1)