# wk10ex3.py
#
# Naam: Timo Kosse
#


import random

# functie #1
#
def create_dictionary(filename):
    """create_dictionary neemt een string wat een textbestandsnaam is en geeft een dictionary terug met als sleutels alle woorden en als waardes alle mogelijke opvolgers.

    Args:
        filename (string): naam van een tekstbestand
    """
    f = open(filename)
    text = f.read()
    f.close()

    #woorden tellen

    words = text.split()
    print('Er zijn ', len(words), 'woorden')

    #het aantal keer dat elk woord voorkomt tellen
    d = {}
    pw = '$'
    for nw in words:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]


        if nw[-1] in '.!?':
            pw = '$'
        else: 
            pw = nw
    return generate_text(d,500)



# functie #2
#
def generate_text(d, n):
    """generate_text krijgt een dictionary van create_dictionary en een integer n. Maakt hiervan een string met n woorden en deze string teruggeven.

    Args:
        d (dictionary): een dictionary 
        n (int): aantal woorden in string
    """
    key = '$'
    zin = ''
    for i in range(n):
        word = random.choice(d[key])
        zin += word + ' '
        if word[-1] in '.!?':
            key = '$'
        else:
            key = word
    print(zin)
    return


#
# Essay gemaakt door Romeo & Juliet. Act 2 Scene 2. Auteur: Shakespeare
#
"""

The orchard walls are high and pale with the rite; And not impute this yielding to hide me here: My ears have spoke: but love, by night, good nurse! 
By a winged messenger of thy father and Juliet is a Montague? I have not Romeo and be Romeo. Anon, good night! If my 'havior light: But love be substantial. 
I gave thee mine before thou as deep; the white-upturned wondering eyes To twinkle in a glove upon my soul that I lent me but thy name, dear love, and give to be true. 
what light wings did I lent me but for such merchandise. I wish but farewell compliment! This bud of my name: How silver-sweet sound lovers' perjuries Then say, Jove laughs. 
Stay but a falconer's voice, To twinkle in heaven Would through the lazy-pacing clouds And follow thee mine before thou mayst prove a hundred words Of mortals that calls upon my love! 
Hist! What man art thou hither, tell me, gentleman, I'll believe thee. Romeo, and good night So stumblest on him eyes. How silver-sweet sound lovers' perjuries Then say, Jove laughs. 
Stay but love, And the worse, to climb, And I'll prove false; at thy light. She speaks: Two of my love! 
'Tis but thy love's passion: therefore thou think'st I was ware, My true love's passion: therefore thou art thou overheard'st, ere I would adventure for both are high and a name? 
By a Capulet. Hist! for a name? My love me? Romeo, hist! Her eye discourses; I am too quickly won, I'll no longer be substantial. 
I am too quickly won, I'll lay And the mask of their books, But to attending ears! My life were a hundred words Of mortals that which thou art As daylight doth cease to give to a Montague? 
If thou as deep; the world. Three words, dear Romeo, Romeo! What's Montague? 
By a winged messenger of thee nay, So Romeo and green And I'll be a lamp; her maid art far more peril in night, being o'er my breast! 
for mine. what love can say thee I have spoke: but for both are high and think it is already sick and what of this yielding to hide me here: My name, And yet I o'er-perch these walls; 
For that vast shore wash'd with the inconstant moon, Who is too bold, 'tis not for both are no part of this place? I will answer it. 
I know not her eyes To lure this contract to-night: It is envious; Her vestal livery is an say thee nay, So Romeo would, were not a dream, Too like the sound: Art thou wilt not, be substantial. 
is the heaven, Having some business, do beseech thee. By a lamp; her eyes in her eyes To twinkle in heaven Would through the worse, to want thy bent of thy foot I'll no longer be new baptized; 
Henceforth I speak at thy kinsmen are infinite. O blessed, blessed moon I was ware, My name.

"""
#
#
