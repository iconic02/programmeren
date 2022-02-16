#wk4ex1

import time
import random
import math
from audio import *


# een functie zodat we kunnen beginnen met een opfrisser
# over list comprehensions...
def three_ize(L):
    """three_ize is a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # dit is een voorbeeld van een list comprehension
    lc = [3 * x for x in L]
    return lc


# Te schrijven functie #1: scale
def scale(L, s):
    """scale neemt lijst L en vermenigvuldigt elk element in de lijst met s

    Args:
        L (list): de lijst
        s (float): de factor voor vermenigvuldigen

    Returns:
        list: de vermenigvuldigde lijst
    """
    lc = [i*s for i in L]
    return lc


assert scale([70,80,420], 0.1) == [7.0, 8.0, 42.0]


# hier is een voorbeeld van hoe je op een andere
# manier de functie three_ize kan schrijven:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # nog een voorbeeld van een list comprehension
    n = len(L)
    lc = [3 * L[i] for i in range(n)]
    return lc

# Te schrijven functie #2: add_2
def add_2(L,m):
    """add_2 neemt 2 lijsten en geeft een lijst terug met alle getallen per index bij elkaar opgeteld

    Args:
        L (list): lijst 1
        m (list): lijst 2

    Returns:
        list: de gemodificeerde lijst
    """
    n = min(len(L), len(m))
    lc = [L[i]+m[i] for i in range(n)]
    return lc

assert add_2([10, 11, 12], [20, 25, 30]) == [30, 36, 42]
assert add_2([10, 11], [20, 25, 30]) == [30, 36]

# Te schrijven functie #3: add_3
def add_3(L, m, p):
    """add_3 neemt 3 lijsten en telt elke index de 3 elementen bij elkaar op en geeft het resultaat in een lijst.

    Args:
        L (list): lijst 1
        m (list): lijst 2
        p (list): lijst 3

    Returns:
        list: 1 lijst met de antwoorden
    """
    n = min(len(L), len(m), len(p))
    lc = [L[i] + m[i] + p[i] for i in range(n)]
    return lc

# Te schrijven functie #4: add_scale_2
def add_scale_2(L, m, L_scale, m_scale):
    """add_scale_2 stuurt 2 lijsten naar scale() en geeft de return waarden door aan add_2()

    Args:
        L (list): lijst 1
        m (list): lijst 2
        L_scale (float): de scale waarde van lijst L
        m_scale (float): de scale waarde van lijst m

    Returns:
        list: een gemodificeerde lijst met het resultaat
    """
    L = scale(L,L_scale)
    m = scale(m,m_scale)

    return add_2(L,m)

# Hulpfunctie: randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x


# Te schrijven functie #5: replace_some
def replace_some(L, chance_of_replacing):
    """replace_some neemt een lijst L en vervangt random waarden hierin met een waarde gekozen door randomize()

    Args:
        L (list): de lijst met waarden
        chance_of_replacing (float): de kans die mee word gegeven aan randomize()

    Returns:
        list: de gemodificeerde lijst
    """
    lc = [randomize(i, chance_of_replacing) for i in L]
    return lc

#
# de functies hieronder betreffen geluidsbewerking...
#


# een functie om te zorgen dat alles werkt
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# De voorbeeldfunctie change_speed
def change_speed(filename, newsr):
    """change_speed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Het originele geluid afspelen...")
    play(filename)

    sound_data = [0, 0]             # een "lege" lijst
    read_wav(filename, sound_data)  # laad gegevens IN sound_data

    samps = sound_data[0]           # de samples van de ruwe geluidsgolven

    print("De eerste 10 geluidsdruksamples zijn\n", samps[:10])
    sr = sound_data[1]              # de sampling rate, sr

    print("Het aantal samples per seconde is", sr)

    # deze regel is niet echt nodig, maar staat hier voor de consistentie...
    newsamps = samps                      # dezelfde samples als eerder
    new_sound_data = [newsamps, newsr]    # nieuwe geluidsgegevens
    write_wav(new_sound_data, "out.wav")  # sla de gegevens op naar out.wav
    print("\nNieuw geluid afspelen...")
    play('out.wav')   # speel het nieuwe bestand 'out.wav' af


def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Het originele geluid afspelen...")
    play(filename)

    print("Geluidsgegevens inlezen...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Nieuw geluid berekenen...")
    # dit bepaalt het middelpunt en noemt dat x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')


def reverse(filename):
    """reverse neemt een file en speelt hem omgekeerd af

    Args:
        filename (string): de file die gebruikt moet worden

    """
    print("Het originele geluid afspelen...")
    play(filename)

    print("Geluidsgegevens inlezen...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Nieuw geluid berekenen...")
    # dit bepaalt het middelpunt en noemt dat x
    newsamps = samps[::-1]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play("out.wav")


# Te schrijven geluidsfunctie #2: volume
def volume(filename, scale_factor):
    """volume neemt een file een scaled deze omhoog of naar beneden met scale()


    Args:
        filename (string): de file die gebruikt moet worden
        scale_factor (float): de factor waarmee je moet scalen

    """
    print('orgineel volume: ')
    play(filename)

    sound_data = [0,0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    new_samps = scale(samps, scale_factor)
    new_sound_data = [new_samps, sr]
    
    print('Nieuw volume: ')
    write_wav(new_sound_data, 'out.wav')

    play('out.wav')

# Te schrijven geluidsfunctie #3: static
def static(filename, prob_of_static):
    """static neemt file en vervangt sommige delen met een andere sample via replace_some

    Args:
        filename (string): het audio bestand
        prob_of_static (float): wordt gegeven aan replace_some

    """
    print('orgineel geluid:')
    play(filename)

    sound_data = [0,0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    new_samps = replace_some(samps, prob_of_static)
    new_sound_data = [new_samps, sr]

    print('nieuw geluid')
    write_wav(new_sound_data, 'out.wav')
    play('out.wav')
# Te schrijven geluidsfunctie #4: overlay
def overlay(filename, filename2): 
    """overlay takes 2 samples and plays them together using add_scale_2


    Returns:
        sound: new sound
    """
    print('orgineel geluid:')
    play(filename)
    print('orgineel geluid 2:')
    play(filename2)

    sound_data = [0,0]
    sound_data2 = [0,0]

    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    read_wav(filename2, sound_data2)
    samps2 = sound_data2[0]
    sr2 = sound_data2[1]
    

    new_samps = add_scale_2(samps,samps2,0.5,0.5)
    new_sound_data = [new_samps, sr]
    write_wav(new_sound_data, 'out.wav')

    play('out.wav')

# Te schrijven geluidsfunctie #5: echo
def echo(filename, timedelay):
    """echo neemt een file en laat een 2e keer het geluid iets later afspelen

    Takes:
    Filename string: de file
    timedelay float: het aantal seconden delay

    Returns:
        : 
    """
    print('Het orginele geluid:')
    play(filename)
    
    sound_data = [0,0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    samplesilence = int(timedelay * sr)
    echosamps = [0 for i in range(samplesilence)]
    echosamps = echosamps + samps
    new_samps = add_scale_2(echosamps, samps, 0.5, 0.5)
    new_sound_data = [new_samps, sr]
    write_wav(new_sound_data, 'out.wav')

    play('out.wav')


# Hulpfunctie om pure tonen te genereren
def gen_pure_tone(freq, seconds, sound_data):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    if sound_data != [0, 0]:
        print("De waarde van sound_data moet [0, 0] zijn.")
        return
    sampling_rate = 22050
    # hoeveel samples we moeten genereren
    nsamples = int(seconds*sampling_rate)  # naar beneden afgerond
    # de factor f om de frequentie te schalen
    f = 2*math.pi/sampling_rate   # omrekenen van samples naar Hz
    # de factor a om de amplitude te schalen
    a = 32767.0
    sound_data[0] = [a * math.sin(f*n*freq) for n in range(nsamples)]
    sound_data[1] = sampling_rate
    return sound_data


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Toon genereren...")
    sound_data = [0, 0]
    gen_pure_tone(freq, time_in_seconds, sound_data)

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #6: chord
def chord(f1, f2, f3, timeSeconds):
    """chord neemt 3 frequenties en een tijd en geeft een akkoord terug

    Args:
        f1 (float): frequentie 1
        f2 (float): frequentie 2
        f3 (fload): frequentie 3
        timeSeconds (float): tijd in seconden
    """

    samps1, sr1 = gen_pure_tone(f1, timeSeconds, [0,0])
    samps2, sr2 = gen_pure_tone(f2, timeSeconds, [0,0])
    samps3, sr3 = gen_pure_tone(f3, timeSeconds, [0,0])

    new_samps = add_scale_3(samps1, samps2, samps3, 0.33, 0.33, 0.33)
    new_sound_data = [new_samps, sr1]
    write_wav(new_sound_data, 'out.wav')

    play('out.wav')

    #chord(440.0, 554, 659, 1.0) A-majoor ! 


def add_scale_3(L,m,n,L_scale,m_scale,n_scale):
    """add_scale_3 neemt 3 lijsten en geeft 1 gescalde lijst  terug

    Args:
        L (list): lijst 1
        m (list): lijst 2
        n (list): lijst 3
        L_scale (float): 1e scale
        m_scale (float): 2e scale
        n_scale (float): 3e scale
    """
    L = scale(L,L_scale)
    m = scale(m,m_scale)
    n = scale(n,n_scale)

    return add_3(L,m,n)
    