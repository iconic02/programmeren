import math

def dbl(x):
    """
    Will return 2 times the value of an argument
    argument: x
    """
    return 2* x
    
def tpl(x):
    """
    Will return 3 times the value of an argument
    argument: x
    argument type: int, float, string
    """
    return 3 * x

def sq(x):
    """
    Will return the square root of the argument
    param: value to square
    argument: x
    argument type: int, float, string
    """
    return sqrt(x)

def interp(low, hi, fraction):
    """
    takes arguments low, hi and fraction
    Will return the fraction of hi - low
    Arguments: low, hi ,fraction
    Type: int, float
    """
    return (hi-low)* fraction + low

def checkends(s):
    """
    Will return a bool, and checks if the last letter of 's' is the same as the first letter of 's'
    Argument: S
    Argument type: string
    """
    firstLetter = s[0]
    lastLetter = s[len(s)-1]

    return firstLetter == lastLetter

def flipside(s):
    """
    Functie wisseld de 1e en 2e helft van een woord om
    Args: s
    Arg type: string
    """
    halve = len(s) // 2
    firstH = s[0:halve]
    secH = s[halve::]

    return secH + firstH

def convert_from_seconds(t):
    """Een functie die een int seconden accepteerd en deze output in:
    d, Days
    h, Hours
    m, Minutes
    s, Seconds

    Args:
        t (int): time in seconds
    """

    d = t // 86400
    t = t - (d * 86400)
    h = t // 3600
    t = t - (h * 3600)
    m = t // 60 
    t = t - (m * 60)
    s = t 
    tijd = [d, h, m, s]
    return tijd