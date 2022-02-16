def leng(s):
    """leng returns the length of  arg s
       Argument: s
       Arg Type: String or List
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    else:
        return 1 + leng(s[1:])

def mult(n,m):
    """Deze functie zorgt ervoor dat m vermenigvuldigd wordt met n door 
    behulp van recursie

    Args:
        n (int): eerste getal
        m (int): tweede getal
    """
    if m == 0 or n == 0:
        return 0
    elif m > 0:
        return n + mult(n, m-1)
    else:
        return -n + mult(n, m+1)

assert mult(-2,-2) == 4
assert mult(2,2) == 4
assert mult(2,-2) == -4
assert mult(-2,2) == -4

def dot(L, k):
    """dot Deze functie geeft het inproduct van 2 even lange lijsten terug

    Args:
        L (list): De eerste lijst die alleen ints heeft
        k (list): De tweede lijst die ook alleen ints heeft
    """
    if len(L) != len(k):
        return 0
    elif len(L) == 0 or len(k) == 0:
        return 0
    else:
        return L[0] * k[0] + dot(L[1:],k[1:])

assert dot([5,4,3],[1,2,3]) == 22
assert dot([1,2,3],[1,2]) == 0
assert dot([],[6]) == 0
assert dot([6],[]) == 0
assert dot([],[]) == 0

def ind(e, L):
    """ind: Een functie die checkt of e voorkomt in L en de index returnt.
    Als e niet in L zit, return len(L)

    Args:
        e (int, string): De interger waarnaar gekeken wordt
        L (list, string): De lijst die bekeken wordt
    """
    if e == L[0]:
        return 0
    elif len(L) != 1:
        return 1 + ind(e, L[1:])
    else: 
        return len(L)

assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100))) == 42
assert ind("hoi", ["hallo", 42, True]) == 3
assert ind("hoi", ["oh", "hoi", "daar"]) == 1
assert ind("i", "team") == 4
assert ind(" ", "nader onderzoek") == 5

def letter_score(let):
    """letter_score Een betere versie van letter, waarbij de string alfabet wordt gecheckt met let.
    De waarde die teruggegeven wordt de de plek van de letter, waarna je via de list punten de juiste punt kan vinden.
    Assert laat zien dat bij v de waarde 4 hoord. Door de lijst te indexeren kan je de index vinden met de for loop.
    Hierdoor kun je diezelfde index bij de waardes gebruiken.

    Args:
        let (string): 1 letter die gecheckt moet worden.
    """
    alfabet = ['a', 'b', 'c', 'd' ,'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    waardes = [1,3,3,1,1,5,2,2,1,4,4,2,3,1,1,3,10,1,1,1,4,4,4,8,8,6]
    if let in "abcdefghijklmnopqrstuvwxyz" and len(let) == 1:
       for idx, val in enumerate(alfabet):
           if val == let:
               return waardes[idx]
    else:
        return 0

def scrabble_score(s):
    """scrabble_score is een functie die een string aanpakt en voor elke letter de waarde checkt en deze optelt tot een totaal.
    Hiervoor maakt de functie gebruik van de vorige: letter_score().


    Args:
        s (string): het scrabble woord waarvan men de waarde wilt weten.
    """
    if s == '':
        return 0
    else: 
        return letter_score(s[0]) + scrabble_score(s[1:])

assert scrabble_score("quotums") == 24
assert scrabble_score("jacquet") == 24
assert scrabble_score("pyjama") == 20
assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 84
assert scrabble_score("?!@#$%^&*()") == 0
assert scrabble_score("") == 0


def transcribe(s):
    """transcribe pakt een string aan dna data en maakt hiervan een boodschapper rna string
    A wordt U
    C wordt G
    G wordt C
    T wordt A
    andere letters worden verwijdert.
    Args:
        s (string): de dna string
    """
    if s != '':
        return odtr(s[0]) + transcribe(s[1:])
    else: 
        return ''

    

def odtr(s):
    """odtr one_dna_to_rna maakt van 1 dna letter de juiste rna letter

    Args:
        s (string): 1 letter
    """
    if s == 'A':
        return 'U'
    elif s == 'C':
        return 'G'
    elif s == 'G':
        return 'C'
    elif s == 'T':
        return 'A'
    else:  
        return ''

assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'  # De spatie verdwijnt
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('hanze')    == ''         # Andere tekens verdwijnen
assert transcribe('')         == ''

#
# Ik heb alle STRING-opgaven van CodingBat gemaakt.
#
# Beide opgaven zijn toegevoegd als bijlage als extra verificatie
#
# Ik heb alle LIJST-opgaven van CodingBat gemaakt.
#


klinker = 'aeiuo'
def piglet_latin(s):
    """piglet_latin een functie die van string s piglet latin maakt:
    medeklinkers voor aan in een woord worden achteraan gezet: straat wordt aatstr. Banaan wordt anaanb.
    Als een woord met medeklinker begint wordt ook 'ee' achter het woord gezet.
    Bij woorden met een klinker wordt alleen 'hee' achter het woord gezet

    Args:
        s (sting): wordt getransformeerd
    """
    top = ''
    if s[0] == '' or s[0] in klinker or s[0] == 'y' and s[1] not in klinker:
        return s + 'ee'
    else:
        return refert(s,top)
        
def refert(s,top):
    """refert Functie die de medeklinkers in een string zet tot er geen medeklinkers meer zijn
    Args:
        s (string): het woord
        top (string): de lege string voor medeklinkers
    Returns:
        string: helaas krijg ik het niet voor mekaar om goed te returnen. Ik krijg de juiste string wel, maar via recursie wordt de return value weer 0.
    """
    if s[0] not in klinker:
        top = top + s[0]
        refert(s[1:], top)
    else:
        return s + top + 'ee'
