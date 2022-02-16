#wk4ex2


def encipher(s, n):
    """encipher een functie die string s voorwaards roteert met n stappen. volgens ceasar schrift 

    Args:
        s (string): een string, kan een zin zijn.
        n (int): een geheel getal tussen 0 en 25
    """
    if n > 25 or n < 0 or type(n) is not int:
        print('geen geldige input voor n')
        return
    elif s == '':
        return ''
    else:
        return rot(s[0],n) + encipher(s[1:], n)



def rot(s, n):
    """rot neemt 1 letter van encipher en roteert

    Args:
        s (string): de letter
        n (int): aantal stappen vooruit
    """
    if n == 0:
        return s
    elif 'a' <= s < 'z' or 'A' <= s < 'Z':
        return rot(chr(ord(s[0])+1),n-1)
    elif s == 'z' or s == 'Z':
        return rot(chr(ord(s[0]) - 25), n-1)
    else:
        return s
    


def decipher(s):
    """decipher functie die een gegeven string ontcijfert met een omgekeerd caesarschrift

    Args:
        s (string): de gegeven versleutelde string
    """
    L = [[encipher(b,n) for b in s] for n in range(26)]
    
    prob = [[letter_prob(b) for b in x] for x in L]
    lol = [sum(x) for x in prob]

    return encipher(s, lol.index(max(lol)))




def letter_prob(c):
    """If c is an alphabetic character,
       we return its monogram probability (for Dutch),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       https://www.sttmedia.com/characterfrequency-nederlands
    """
    if c == 'e' or c == 'E':
        return 0.1909
    if c == 'n' or c == 'N':
        return 0.0991
    if c == 'a' or c == 'A':
        return 0.0769
    if c == 't' or c == 'T':
        return 0.0642
    if c == 'i' or c == 'I':
        return 0.0630
    if c == 'o' or c == 'O':
        return 0.0581
    if c == 'r' or c == 'R':
        return 0.0562
    if c == 'd' or c == 'D':
        return 0.0541
    if c == 's' or c == 'S':
        return 0.0384
    if c == 'l' or c == 'L':
        return 0.0380
    if c == 'h' or c == 'H':
        return 0.0312
    if c == 'g' or c == 'G':
        return 0.0312
    if c == 'k' or c == 'K':
        return 0.0279
    if c == 'm' or c == 'M':
        return 0.0256
    if c == 'v' or c == 'V':
        return 0.0224
    if c == 'u' or c == 'U':
        return 0.0212
    if c == 'j' or c == 'J':
        return 0.0182
    if c == 'w' or c == 'W':
        return 0.0172
    if c == 'z' or c == 'Z':
        return 0.0160
    if c == 'p' or c == 'P':
        return 0.0149
    if c == 'b' or c == 'B':
        return 0.0136
    if c == 'c' or c == 'C':
        return 0.0130
    if c == 'f' or c == 'F':
        return 0.0073
    if c == 'y' or c == 'Y':
        return 0.0006
    if c == 'x' or c == 'X':
        return 0.0005
    if c == 'q' or c == 'Q':
        return 0.0001
    return 1.0


assert decipher('Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.') == 'Caesarcijfer? Ik heb liever Caesarsalade.'
assert decipher('Aadxas ue exqotfe pq haadflqffuzs hmz baxufuqw yqf mzpqdq yuppqxqz.') == 'Oorlog is slechts de voortzetting van politiek met andere middelen.'


def blsort(L):
    """blsort neemt een lijst met binaire getallen, en set deze op volgorde

    Args:
        L (list): de lijst met binaire getallen
    """
    lc = [0 for x in L if x == 0] + [1 for x in L if x == 1]
    return lc


def rem_one(e, L):
    """Returns sequence L with one e rmoved
    """
    if len(L) == 0:
        return L
    elif L[0] != e:
        return L[0:1] + rem_one(e, L[1:])
    else:
        return L[1:]


def gensort(L):
    """gensort neemt lijst L en sorteerd.

    Args:
        L (list): lijst met integers
    """
    if L == []:
        return []
    else:
        lc = [min(L)]
        L = rem_one(min(L), L)
        return lc + gensort(L)


assert gensort([42, 1, 3.14]) == [1, 3.14, 42]
assert gensort([7, 9, 4, 3, 0, 5, 2, 6, 1, 8]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def lingo(s, t):
    """lingo neemt 2 strings en geeft terug hoeveel letters de beide woorden gemeen hebben.
    Dit hoeven niet letters zijn op dezelfde plek.

    s: string: het eerste woord
    t: string: het tweede woord

    """
    sameCounter = 0
    if s == '' or t == '':
        return 0
    if s[0] in t:
        rem_one(s[0], t)
        sameCounter += 1
    return sameCounter + lingo(s[1:], t)   
        

def changeCalc(target, L):
    print(L)
    if target == 0:
        return True
    if target < 0:
        return False
    if L == []:
        return 0
    if L[0] > target:
        return changeCalc(target, L[1:])
    elif L[0] == target:
        return L[0]
    elif L[0] < target:
        use = L[0] + changeCalc(target - L[0], L[1:])
        lose = changeCalc(target, L[1:])
        return max(use, lose)

def exact_change(target, L):
    """exact_change neemt een target amount en een lijst en kijkt of target gehaald kan worden met de inhoud van de lijst

    Args:
        target (int): het te behalen nummer.
        L (list): de lijst met waarden

    Returns:
        boolean: T/F op basis van te behalen of niet
    """
    if changeCalc(target, L) == target or changeCalc(target, L) == True:
        return True
    else: 
        return False

assert exact_change(42, [25, 1, 25, 10, 5, 1]) == True
assert exact_change(42, [25, 1, 25, 10, 5]) == False
assert exact_change(42, [23, 1, 23, 100]) == False
assert exact_change(42, [23, 17, 2, 100]) == True
assert exact_change(42, [25, 16, 2, 15]) == True  # de 16 moet "overgeslagen" kunnen worden...
assert exact_change(0, [4, 5, 6]) == True
assert exact_change(-47, [4, 5, 6]) == False
assert exact_change(0, []) == True
assert exact_change(42, []) == False


def lcs(s,t):
    """lcs neemt s en t en geeft een string terug met gemeenschappelijke letters

    Args:
        s (string): de eerste string
        t (string): de tweede string
    """
    newString = ''
    if len(s) == 0 or len(t) == 0:
        return ''
    elif s[0] == t[0]:
        newString += s[0]
        return s[0] + lcs(s[1:],t[1:])
    else:
        return max(lcs(s, t[1:]), lcs(s[1:], t), key=len)
                
assert lcs('mens', 'chimpansee') == 'mns'
assert lcs('gattaca', 'tacgaacta') == 'gaaca'
assert lcs('wow', 'wauw') == 'ww'
assert lcs('abcdefgh', 'efghabcd') == 'abcd'



