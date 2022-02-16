#wk3ex3.py
#numerieke integratie

from math import *

def dbl(x):
    """dbl dubbelt een waarde

    Args:
        x (int): de waarde die verdubbelt moet worden

    Returns:
        int: het dubbele getal
    """

    return 2 * x 

def sq(x):
    """sq geeft x ** 2

    Args:
        x (int): dit is x

    Returns:
        int: dit is x ** 2
    """
    return x**2

def lc_mult(n):
    """lc_mult geeft een lijst met verdubblede waardes

    Args:
        n (int): de max van de range 

    Returns:
        list: een lijst met alle waardes van n verdubbelt
    """
    return  [2 * x for x in range(n)]   

def lc_idiv(n):
    """lc_idiv geeft aan hoevaak range n in 2 past

    Args:
        n (int): range waarde

    Returns:
        list: een lijst met 0,0,1,1 etc
    """
    return [float(x // 2) for x in range(n)]

def lc_fdiv(n):
    """lc_fdiv geeft een lijst met alle getallen / 2

    Returns:
        list: deze lijst bevat alle gedeelde getallen.
    """
    return [x / 2 for x in range(n)]
assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

def unitfracs(n):
    """unitfracs Gives a list from 0 to 1 in equal steps 

    Args:
        n (int): amount of steps

    Returns:
        list: list of all equal x positions
    """
    return [x * 1/n for x in range(n)]

assert unitfracs(1) == [0.0]
assert unitfracs(2) == [0.0,0.5]
assert unitfracs(4) == [0.0,0.25,0.5,0.75]

def scaledfracs(low, hi, n):
    """scaledfracs geeft een lijst van low naar high met gelijke stappen ertussen

    Args:
        low (int): lowest point
        hi (int): highest point
        n (int): steps between
    """
    return [x * (hi-low)/n + low for x in range(n)]

assert scaledfracs(0,10,5)
assert scaledfracs(10,20,5)
assert scaledfracs(0,50,3)
assert scaledfracs(0,100,10)


def sqfracs(low, hi, n):
    """sqfracs geeft een lijst van low naar high met n stappen, maar squared alle uitkomsten

    Args:
        low (int): lowest num
        hi (int): highest num
        n (int): steps between
    """
    return [x ** 2 for x in scaledfracs(low, hi, n)]

assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert sqfracs(0, 10, 5) == [0.0, 4.0, 16.0, 36.0, 64.0]
assert sqfracs(10, 20, 2) == [100.0, 225.0]

def f_of_fracs(f, low, hi, n):
    """f_of_fracs neemt een functie en maakt van low, hi, n een lijst via scaledfracs.
    De uitkomsten van scaledfracs worden door de gegeven functie gehaald.

    Args:
        f (functie): neemt een functie om te gebruiken.
        low (int): lowest num
        hi (int): highest num   
        n (int): steps
    """
    return [f(x) for x in scaledfracs(low, hi, n)]

def integrate(f, low, hi, n):
    """integrate geeft integraal terug via f_of_fracs, hij neemt de som van de uitkomsten en 
    vermenigvuldigt dit met de x per stap: (hi-low)/n

    Args:
        f (functie): de gewenste functie
        low (int): laagste getal
        hi (int): hoogste getal
        n (int): stappen
    """
    return sum(f_of_fracs(f, low, hi, n)) * (hi-low)/n

assert integrate(dbl, 0, 10, 4) == 75
assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])

def c(x):
    """
    C volgt de bovenste helft van een cirkel met straal 2.
    """
    return (4-x**2) **0.5  


""" 
Vraag 1.
Dit komt omdat je zoals uitgelegd de rechthoeken wel dunner kunt maken, maar om een perfecte
driehoek te maken zul je oneindig veel van dit soort rechthoeken moeten hebben.
Het blijft dus 100 naderen maar zal het nooit aanraken omdat je niet oneindig veel rechthoeken kunt maken.

Deelvraag: Dit zou kunnen door bijvoorbeeld de functie lijn omhoog te schuiven. 
Ipv y=2x zou je y=2x+0.01 kunnen doen.

Vraag 2.
C gaat richting het getal van pi
integrate(c,0,2,200)
geeft 3.15117...
integrate(c,0,2,2000)
geeft 3.14257...

hoe groter n wordt, hoe dichter C bij het getal van pi komt. 
Dit komt omdat je de halve cirkel vult met de rechthoeken uit het figuur. 
Zo kom je langzaam uit bij het getal pi


""" 
