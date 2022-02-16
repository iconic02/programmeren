#
# wk9ex2.py
#
# Naam: Timo Kosse
#


def print_2d(a):
    """print_2d prints a 2D array, a
       as rows and columns
       Argument: a, a 2D list of lists
       Result: None (no return value)
    """
    rows = len(a)
    cols = len(a[0])

    for r in range(rows):      # rows == aantal rijen
        for c in range(cols):  # cols == aantal kolommen
            print(a[r][c], end=' ')
        print()

    return None  # dit is impliciet aanwezig
    # als er geen return-statement aanwezig is





def create_a(rows, cols, s):
    """Returns a 2D array with
       rows rows and
       cols cols
       using the data from s: across the
       first row, then the second, etc.
       We'll only test it with enough data!
    """
    a = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row += [s[0]]  # voeg dat karakter toe
            s = s[1:]          # verwijder het eerste karakter
        a += [new_row]
    return a



def in_a_row_3_east(ch,r_start,c_start,a):
    """in_a_row_3_east kijkt voor fopr for karakter met rij en kolom start en krijgt een array mee

    Args:
        ch (string): het karakter waar we voor kijken
        r_start (int): een cijfer voor rij
        c_start (int): een cijfer voor kolom
        a (list): de array

    Returns:
        boolean: waar of niet waar
    """
    rows = len(a)
    cols = len(a[0])

    if c_start > cols -3 or c_start < 0:
        return False
    if r_start < 0 or r_start >= rows:
        return False

    for i in range(3):
        if a[r_start][c_start + i] != ch:
            return False
    return True


def in_a_row_3_south(ch, r_start, c_start, a):
    """in_a_row_3_south kijkt voor fopr for karakter met rij en kolom start en krijgt een array mee

    Args:
        ch (string): het karakter waar we voor kijken
        r_start (int): een cijfer voor rij
        c_start (int): een cijfer voor kolom
        a (list): de array

    Returns:
        boolean: waar of niet waar
    """
    rows = len(a)
    cols = len(a[0])


    if r_start < 0 or r_start > rows -3:
        return False
    if c_start < 0 or c_start >= cols:
        return False

    for i in range(3):
        if a[r_start + i][c_start] != ch:
            return False
    return True


def in_a_row_3_southeast(ch,r_start,c_start,a):
    """in_a_row_3_southeast kijkt voor fopr for karakter met rij en kolom start en krijgt een array mee

    Args:
        ch (string): het karakter waar we voor kijken
        r_start (int): een cijfer voor rij
        c_start (int): een cijfer voor kolom
        a (list): de array

    Returns:
        boolean: waar of niet waar
    """
    rows = len(a)
    cols = len(a[0])


    if c_start < 0 or c_start > cols -3:
        return False
    if r_start < 0 or r_start > rows -3:
        return False

    for i in range(3):
        if a[r_start + i][c_start + i] != ch:
            return False
            
    return True


def in_a_row_3_northeast(ch, r_start, c_start, a):
    """in_a_row_3_northeast kijkt voor fopr for karakter met rij en kolom start en krijgt een array mee

    Args:
        ch (string): het karakter waar we voor kijken
        r_start (int): een cijfer voor rij
        c_start (int): een cijfer voor kolom
        a (list): de array

    Returns:
        boolean: waar of niet waar
    """
    rows = len(a)
    cols = len(a[0])


    if r_start < 2 or r_start >= rows:
        return False
    if c_start < 0 or c_start > cols -3:
        return False

    for i in range(3):
        if a[r_start - i][c_start + i] != ch:
            return False
    return True


# tests voor in_a_row_3_east
a = create_a(3, 4, 'XXOXXXOOOOOO')
assert not in_a_row_3_east('X', 0, 0, a)
assert in_a_row_3_east('O', 2, 1, a)
assert not in_a_row_3_east('X', 2, 1, a)
assert not in_a_row_3_east('O', 2, 2, a)

# tests voor in_a_row_3_south
a = create_a(4, 4, 'XXOXXXOXXOO OOOX')
assert in_a_row_3_south('X', 0, 0, a)
assert not in_a_row_3_south('O', 2, 2, a)
assert not in_a_row_3_south('X', 1, 3, a)
assert not in_a_row_3_south('O', 42, 42, a)

# tests voor in_a_row_3_southeast
a = create_a(4, 4, 'XOOXXXOXX XOOOOX')
assert in_a_row_3_southeast('X', 1, 1, a)
assert not in_a_row_3_southeast('X', 1, 0, a)
assert in_a_row_3_southeast('O', 0, 1, a)
assert not in_a_row_3_southeast('X', 2, 2, a)

# tests voor in_a_row_3_northeast
a = create_a(4, 4, 'XOXXXXOXXOXOOOOX')
assert in_a_row_3_northeast('X', 2, 0, a)
assert in_a_row_3_northeast('O', 3, 0, a)
assert not in_a_row_3_northeast('O', 3, 1, a)
assert not in_a_row_3_northeast('X', 3, 3, a)

# XOOX
# XXOX
# X XO
# OOOX


def in_a_row_n_east(ch, r_start, c_start, a, n):
    rows = len(a)
    cols = len(a[0])

    if c_start > cols -n or c_start < 0:
        return False
    if r_start < 0 or r_start >= rows:
        return False

    for i in range(n):
        if a[r_start][c_start + i] != ch:
            return False
    return True


def in_a_row_n_south(ch, r_start, c_start, a, n):
    rows = len(a)
    cols = len(a[0])


    if r_start < 0 or r_start > rows -n:
        return False
    if c_start < 0 or c_start >= cols:
        return False

    for i in range(n):
        if a[r_start + i][c_start] != ch:
            return False
    return True


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    rows = len(a)
    cols = len(a[0])


    if c_start < 0 or c_start > cols -n:
        return False
    if r_start < 0 or r_start > rows -n:
        return False

    for i in range(n):
        if a[r_start + i][c_start + i] != ch:
            return False
    return True


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    rows = len(a)
    cols = len(a[0])


    if r_start < n-1 or r_start >= rows:
        return False
    if c_start < 0 or c_start > cols -n:
        return False

    for i in range(n):
        if a[r_start - i][c_start + i] != ch:
            return False
    return True



# tests voor in_a_row_n_east
a = create_a(5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
assert in_a_row_n_east('O', 1, 1, a, 4)
assert in_a_row_n_east('O', 1, 3, a, 2)
assert not in_a_row_n_east('X', 3, 2, a, 4)
assert in_a_row_n_east('O', 4, 0, a, 5)


# tests voor in_a_row_n_south
a = create_a(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
assert not in_a_row_n_south('X', 0, 0, a, 5)
assert in_a_row_n_south('O', 1, 1, a, 4)
assert not in_a_row_n_south('O', 0, 1, a, 6)
assert in_a_row_n_south('X', 4, 3, a, 1)


# tests voor in_a_row_n_southeast
a = create_a(5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX')
assert in_a_row_n_southeast('X', 1, 1, a, 4)
assert not in_a_row_n_southeast('O', 0, 1, a, 3)
assert in_a_row_n_southeast('O', 0, 1, a, 2)
assert not in_a_row_n_southeast('X', 3, 0, a, 2)


# tests voor in_a_row_n_northeast
a = create_a(5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX')
assert in_a_row_n_northeast('X', 4, 0, a, 5)
assert in_a_row_n_northeast('O', 4, 1, a, 4)
assert not in_a_row_n_northeast('O', 2, 0, a, 2)
assert not in_a_row_n_northeast('X', 0, 3, a, 1)