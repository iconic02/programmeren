#wk5ex1

def is_odd(n):
    """is_odd neemt n en geeft T/F terug

    Args:
        n (int): het nummer in kwestie
    """
    if n % 2 == 0:
        return False
    else:
        return True

assert is_odd(1) == True
assert is_odd(21) == True
assert is_odd(10) == False
assert is_odd(52) == False
assert is_odd(42) == False
assert is_odd(43) == True

def num_to_binary(n):
    """num_to_binary neemt een int en geeft binaire reeks terug

    Args:
        n (int): een getal om te conferteren
    """
    if n == 0:
        return ''
    elif n % 2 == 1:
        n -= 1
        return num_to_binary(n/2) + '1'
    else:
        return num_to_binary(n/2) + '0'


assert num_to_binary(0) == ''
assert num_to_binary(1) == '1'
assert num_to_binary(4) == '100'
assert num_to_binary(10) == '1010'
assert num_to_binary(42) == '101010'
assert num_to_binary(100) == '1100100'


def binary_to_num(s):
    """binary_to_num neemt s en geeft num terug


    Args:
        s (string): lijst met bits
    """
    if s == '':
        return 0
    elif s[-1] == '1':
        return binary_to_num(s[:-1]) + binary_to_num(s[:-1]) + 1
    else:
        return binary_to_num(s[:-1]) + binary_to_num(s[:-1]) + 0

assert binary_to_num('100') == 4
assert binary_to_num('1011') == 11
assert binary_to_num('00001011') == 11
assert binary_to_num('') == 0
assert binary_to_num('0') == 0
assert binary_to_num('1100100') == 100
assert binary_to_num('101010') == 42


def increment(s):
    """increment neemt string met binaire getallen. hij geeft het volgende getal in binair terug.
    Dus als je 010 geeft (getal 2) geeft de functie 011 terug (3)

    Args:
        s (string): de binaire string
    """
    if '0' not in s:
        return '0' * len(s)
    newNum =  num_to_binary(binary_to_num(s)+1)
    return '0' * (len(s)-len(newNum)) + newNum

assert increment('00000000') == '00000001'
assert increment('00000001') == '00000010'
assert increment('00000111') == '00001000'
assert increment('11111111') == '00000000'


def count(s, n):
    """count neemt string van 8 binaire tekens die de string n keer doortelt   

    Args:
        s (string): binaire lijst
        n (int): doortel nummer
    """
    print(s)
    if len(s) != 8:
        return
    elif n == 0:
        print(s)
    else:
        return count(increment(s), n-1)


"""
het ternaire getal voor 59 is 1012
omdat 27 * 2 = 54 + 3 * 1 = 57 + 1 * 2 = 59
"""

def num_to_ternary(n):
    """num_to_ternary geeft de ternaire string van een getal terug
    

    Args:
        n (int): het te conferteren getal.
    """
    if n == 0:
        return ''
    elif n % 3 == 1:
        n -= 1
        return num_to_ternary(n/3) + '1'
    elif n % 3 == 2:
        n -= 2
        return num_to_ternary(n/3) + '2'
    else:
        return num_to_ternary(n/3) + '0'

assert num_to_ternary(42) == '1120'
assert num_to_ternary(4242) == '12211010'


def ternary_to_num(s):
    """ternary_to_num neemt string aan ternaire getallen en geeft het nummer terug

    Args:
        s (string): string met ternaire getallen
    """
    if s == '':
        return 0
    elif s[-1] == '2':
        return ternary_to_num(s[:-1]) + ternary_to_num(s[:-1]) + ternary_to_num(s[:-1]) + 2
    elif s[-1] == '1':
        return ternary_to_num(s[:-1]) + ternary_to_num(s[:-1]) + ternary_to_num(s[:-1]) + 1
    else:
        return ternary_to_num(s[:-1]) + ternary_to_num(s[:-1]) + ternary_to_num(s[:-1]) + 0

assert ternary_to_num("1120") == 42
assert ternary_to_num("12211010") == 4242


def balanced_ternary_to_num(s):
    """balanced_ternary_to_nums neemt een string balanced ternary symbolen en geeft het getal terug


    Args:
        s (string): string met balanced ternary symbolen
    """
    if s == '':
        return 0
    elif s[-1] == '+':
        return balanced_ternary_to_num(s[:-1]) + balanced_ternary_to_num(s[:-1]) + balanced_ternary_to_num(s[:-1]) + 1
    elif s[-1] == '0':
        return balanced_ternary_to_num(s[:-1]) + balanced_ternary_to_num(s[:-1]) + balanced_ternary_to_num(s[:-1]) + 0
    elif s[-1] == '-':
        return balanced_ternary_to_num(s[:-1]) + balanced_ternary_to_num(s[:-1]) + balanced_ternary_to_num(s[:-1]) - 1

assert balanced_ternary_to_num("+---0") == 42
assert balanced_ternary_to_num("++-0+") == 100

def num_to_balanced_ternary(n):
    """num_to_balanced_ternary neemt int N en geeft een string met balanced ternary getallen terug.

    Args:
        n (int): het nummer
    """
    if n == 0:
        return ''
    elif n % 3 == 1:
        n -= 1
        return num_to_balanced_ternary(n/3) + '+'
    elif n % 3 == 2:
        n += 1
        return num_to_balanced_ternary(n/3) + '-'
    else:
        return num_to_balanced_ternary(n/3) + '0'

assert num_to_balanced_ternary(42) == '+---0'
assert num_to_balanced_ternary(100) == '++-0+'