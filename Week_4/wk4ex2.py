def encode(s, n):
    """encode een functie die string s voorwaards roteert met n stappen. volgens ceasar schrift 

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
        return e_letter(s[0],n) + encode(s[1:], n)

alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def e_letter(s, n):
    """e_letter neemt 1 letter van encode en roteert

    Args:
        s (string): de letter
        n (int): aantal stappen vooruit
    """
    if s.isUpper() == True:
        for x in range(len(alfabet)):
            if alfabet[x] == s[0]:
                if x+n <= 25:
                    return alfabet[x+n]
                else:
                    return alfabet[x+n-26]       
    elif s.isUpper() == False:
        for x in range(len(alfabet)):
            if alfabet[x] == s[0]:
                if x+n <= 25:
                    return alfabet[x+n]
                else:
                    return alfabet[x+n-26]
    else:
        return s
    
