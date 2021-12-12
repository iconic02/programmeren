#
# wk9ex1.py - Practicum Game of Life
#
# Naam:
#

import random


def create_one_row(width):
    """ returns one row of zeros of width "width"...  
         You might use this in your create_board(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row


def create_board(width, height):
    """create_board maakt een tweedimensionale lijst van w bij h.

    Args:
        width (int): aantal kolommen in de lijst
        height (int): aantal rijen in de lijst
    """
    listt = [create_one_row(width) for i in range(height)]
    return listt
    

def print_board(a):
    """print_board print een lijst van 2d arrays

    Args:
        a (list): de list
    """
    for row in a:
        for col in row:
            print(col, end='')
        print()    


def diagonalize(width, height):
    """diagonalize neemt w en h en maakt een array, waarbij een diagonale lijn ontstaat met 1'en ipv 0'en

    Args:
        width (int): lengte
        height (int): hoogte van de array
    """
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                a[row][col] = 1
            else:
                a[row][col] = 0

    return a
    

def inner_cells(w, h):
    """inner_cells geeft 2d array terug met alleen maar levende cellen, behalve een rand met nullen

    Args:
        w (int): lengte
        h (int): hoogte van de array
    """
    a = create_board(w, h)
    

    for row in range(1, h -1):
        for col in range(1, w -1):
            a[row][col] = 1

    return a


def random_cells(w, h):
    """random_cells geeft een willekeurige gevulde array terug

    Args:
        w (int): lengte
        h (int): hoogte van de array
    """
    a = create_board(w, h)
    

    for row in range(1, h -1):
        for col in range(1, w -1):
            a[row][col] = random.choice([0, 1])

    return a


def copy(a):
    """copy geeft een diepe copy van een gegeven array

    Args:
        a (list): array
    """
    h = len(a)
    w = len(a[0])
    new_a = create_board(w,h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            new_a[row][col] = a[row][col]

    return new_a


def inner_reverse(a):
    """inner_reverse flipt alle bits in een board, 1 wordt 0 en omgekeerd.

    Args:
        a (list): ons bord
    """
    h = len(a)
    w = len(a[0])


    for row in range(1, h -1):
        for col in range(1, w -1):
            if a[row][col] == 1:
                a[row][col] = 0
            else:
                a[row][col] = 1


    return a


def count_neighbours(row, col, a):
    """count_neighbours kijkt van een cel in een array hoeveel buren er zijn

    Args:
        row (int): rij getal
        col (int): kolom getal
        a (list): de array
    """
    count = 0
    if a[row-1][col-1] == 1:
        count += 1 
    if a[row-1][col] == 1:
        count += 1
    if a[row-1][col+1] == 1:
        count += 1
    if a[row][col-1] == 1:
        count += 1
    if a[row][col+1] == 1:
        count += 1
    if a[row+1][col-1] == 1:
        count += 1
    if a[row+1][col] == 1:
        count += 1
    if a[row+1][col+1] == 1:
        count += 1
    
    return count


def next_life_generation(a):
    """nex_life_generation Makes a copy of a and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.


    Args:
        a (list): de array die we gaan bewerken
    """
    h = len(a)
    w = len(a[0])


    new_a = copy(a)
    for row in range(1, h-1):
        for col in range(1, w-1):
            if count_neighbours(row,col,a) < 2 or count_neighbours(row,col,a) > 3:
                new_a[row][col] = 0
            elif count_neighbours(row,col,a) == 3:
                new_a[row][col] = 1

    return new_a



#ik kon helaas geen visualisatie aan de praat krijgen, omdat tkinter niet als een bestaande module werd gezien.