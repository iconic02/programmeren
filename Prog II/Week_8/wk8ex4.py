#wk8ex4
#conway probleem

def next(n):
    """next neemt een int n. En converteerd deze naar het 'volgende' getal d.m.v. de conway methode.
    zo wordt bijv 11242 --> 21121412.

    Args:
        n (int): een willekeurig getal.
    """
    n = str(n)
    count = 0
    storage = '' #hier houden we de tot nu toe geconverteerde nummers
    while n != '':
        for i in n:
            if i == n[0]:
                count += 1
            else:
                break
        storage += extra(n, count)
        n = n.replace(n[0:count], '', 1)
        count = 0
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
assert next(312211) == 13112221



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

    


    

