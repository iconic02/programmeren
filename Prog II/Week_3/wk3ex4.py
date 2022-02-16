#wk3ex4.py

# sources: 
# http://www.devx.com/supportitems/showSupportItem.php?co=41509&supportitem=figure1
# https://realpython.com/beginners-guide-python-turtle/#changing-the-pen-speed
from turtle import *
from random import *


colormode(255)



def spiral(initial_length):
    """Spiral-drawing function.  Arguments:
       initial_length = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    for x in range(37):
        red = choice(range(255)) 
        green = choice(range(255)) 
        blue = choice(range(255)) 
        pencolor(red,green,blue)
        speed(50)
        circle(100)
        left(10)
