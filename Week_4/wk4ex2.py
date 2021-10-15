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

alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperAlfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def rot(s, n):
    """rot neemt 1 letter van encipher en roteert

    Args:
        s (string): de letter
        n (int): aantal stappen vooruit
    """
    if s.isupper() == True:
        for x in range(len(upperAlfabet)+1):
            if upperAlfabet[x] == s[0]:
                if x+n <= 25:
                    return upperAlfabet[x+n]
                else:
                    return upperAlfabet[x+n-26]       
    elif s.isupper() == False and s.islower() == True:
        for x in range(len(alfabet)+1):
            if alfabet[x] == s[0]:
                if x+n <= 25:
                    return alfabet[x+n]
                else:
                    return alfabet[x+n-26]
    else:
        return s
    
assert encipher("xyza", 1) == "yzab"
assert encipher("Z A", 1) == "A B"
assert encipher('Caesarcijfer? Ik heb liever Caesarsalade.', 25) == 'Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.'

def decipher(s):
    """decipher functie die een gegeven string ontcijfert met een omgekeerd caesarschrift

    Args:
        s (string): de gegeven versleutelde string
    """
    L = [encipher(s,n) for n in range(26)]
    sumList = []
    for x in L:
        listProb = [letter_prob(x[b]) for b in range(len(x))]
        sumList.append(sum(listProb))
    max_index = sumList.index(max(sumList))
    return L[max_index]



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
    sortList = []
    numOne = 0
    for x in L:
        if x == 0:
            sortList.append(0)
        if x == 1:
            numOne += 1
    for x in range(numOne):
        sortList.append(1)
    return sortList

def gensort(L):
    """gensort neemt lijst L en sorteerd.

    Args:
        L (list): lijst met integers
    """
    newL = []
    for x in range(len(L)):
        newL.append(min(L))
        L.remove(min(L))
    return newL

assert gensort([42, 1, 3.14]) == [1, 3.14, 42]
assert gensort([7, 9, 4, 3, 0, 5, 2, 6, 1, 8]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def lingo(s, t):
    """lingo neemt 2 strings en geeft terug hoeveel letters de beide woorden gemeen hebben.
    Dit hoeven niet letters zijn op dezelfde plek.

    s: string: het eerste woord
    t: string: het tweede woord

    """
    sameCounter = 0
    for x in range(len(s)):
        for b in range(len(t)):
            if s[x] == t[b]:
                t = t.replace(t[b], ' ', 1)
                sameCounter += 1
                print(s, t)
                #visualisatie over hoe het programma werkt
                break
    if '' in s:
        #compensatie voor spaties in s
        #deze worden namelijk wel meegerekend in sameCounter
        sameCounter -= 1    
    return sameCounter

def exact_change(target, L):
    if target < 0:
       return False
    elif target == 0:
       return True
    else: 
        oou = sum(L)-target
        if oou in L:
            L.remove(oou)
            print(L)
            return True
        elif oou not in L:
            print('Geen direct resultaat')
            return False



        
   



#total = sum(L)
#    oou = total-target
#    if oou in L:
#        L.remove(oou)
#        return True
#    elif oou not in L:
#        print('Cant find exact oou in list L')
#        return
