# wk8ex3.py
#


import random
import math


def throw_dart():
    """throw_dart generates two values x and y and checks if coörds are in circle with surface pi
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if math.sqrt(x**2 + y**2) <= 1:
        return True
    else:
        return False


def for_pi(n):
    """for_pi will print number of dart thrown and number of darts within circle and calculated pi

    Args:
        n (int): number of throws
    """
    hit = 0
    for i in range(n):
        if throw_dart() == True:
            hit += 1
        print(hit, ' raak van ', i +1, ' worpen dus pi is ', (hit/(i+1) * 4)) 
    
    
def while_pi(error):
    """while_pi takes float error and calculates the amount of times needed to come withing pi +- error

    Args:
        error (float): the amount of error allowed
    """
    hit = 0
    throw = 0
    while True:
        throw += 1
        if throw_dart() == True:
            hit += 1
        pi_calc = (hit / (throw + 1)) * 4
        print(hit, ' raak van ', throw, ' worpen dus pi is ', pi_calc)
        if pi_calc < (error + math.pi) and pi_calc > (math.pi - error):
            return throw