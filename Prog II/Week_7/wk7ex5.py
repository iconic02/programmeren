#
# wk7ex5.py listige lussen
#
# Naam: Timo
#

import random

def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # beginwaarde; lijkt op een basisgeval
    for x in range(1, n + 1):  # herhaal van 1 tot en met n
        result = result * x    # pas het resultaat aan door keer x te doen
    return result              # merk op dat dit NA de lus is!

#
# Tests voor de lus-versie van de faculteit
#
assert fac(0) == 1
assert fac(5) == 120


def power(b, p):
    """power geeft b tot de macht van p

    Args:
        b (int): grondtal
        p (int): machtsgetal
    """
    result = 1
    for x in range(1, p + 1):
        result = b * result
    return result

assert power(0,10) == 0
assert power(10,0) == 1
assert power(3,3) == 27
assert power(2,3) == 8
assert power(0,0) == 1


def summed(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)
       Argument: L, a list of integers.
       Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # of result += e
    return result

# tests!
assert summed([4, 5, 6]) == 15
assert summed(range(3, 10)) == 42


def summed_odds(L):
    """summed_odds telt alle oneven nummers van een lijst L bij elkaar op

    Args:
        L (list): lijst met getallen
    """
    result = 0
    for e in L:
        if e % 2 != 0:
            result = result + e
    return result

assert summed_odds([4, 5, 6]) == 5
assert summed_odds(range(3, 10)) == 24
assert summed_odds([2,3,4,5,6,7]) == 15


def count_guesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 tot en met 99
    num_guesses = 1                          # we hebben nu 1 keer geraden
    while guess != hidden:
        guess = random.choice(range(0, 100)) # opnieuw raden!
        num_guesses += 1                     # 1 toevoegen aan het aantal pogingen
    return num_guesses


def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])


def until_a_repeat(high):
    """until_a_repeat blijft raden, tot er 2 getallen hetzelfde zijn

    Args:
        high (int): max gok range
    """
    L = []
    guess = random.choice(range(0, high)) 
    num_guesses = 1                    
    while unique(L) == True:
        guess = random.choice(range(0, high))
        L = L + [guess]
        num_guesses += 1                  
    return num_guesses

