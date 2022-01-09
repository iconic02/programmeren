#wk8ex4
#
#conway probleem
#
# naam: Timo Kosse



def next(n):
    """next neemt een int n. En converteerd deze naar het 'volgende' getal d.m.v. de conway methode.
    zo wordt bijv 11242 --> 21121412.

    Args:
        n (int): een willekeurig getal.
    """
    n = str(n)
    count = 1
    storage = '' #hier houden we de tot nu toe geconverteerde nummers
    while n != '':
        while True:
            if len(n) > 1:
                if n[1] == n[0]:
                    count += 1
                    n = n[1:]
                else:
                    storage += extra(n[0],count)
                    n = n[1:]
                    count = 1
                    break
        else:
            storage += extra(n[0],count)
            n = n[1:]
            break
    return int(storage)
        
    
def extra(n, count):
    """extra neemt n0 van next en count, en maakt hier een conway getal van

    Args:
        n (string): het cijfer als een string
        count (int): het aantal keer dat ie voorkomt
    """
    result = str(count) + n
    return result
        

assert next(21) == 1211
assert next(2222) == 42
assert next(42) == 1412
assert next(312211) == 13112221
assert next(2229428) == 3219141218



def read_it(n):
    """read_it drukt de eerste n getallen van conway's methode af

    Args:
        n (int): hoevaak moeten we afdrukken
    """
    start = 1
    while n > 0:
        print(start)
        start = next(start)
        n -= 1

    


    

