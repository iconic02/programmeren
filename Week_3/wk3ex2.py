#wk3ex2

import random  
import sys
import time


def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """rwpos Geeft locatie weer na aantal stappen

    Args:
        start (int): startlocatie
        nsteps (int): aantal stappen

    """
    time.sleep(0.2)
    print('positie is ', start)   
    if nsteps == 0:
        return 
    else:
        return rwpos(start + rs(), nsteps - 1)


def rwpos_plain(start, nsteps):
    """rwpos_plain de functie geeft de loper positie terug

    start, int, beginpositie
    nsteps, int, niet negatieve aantal willekeurige stappen.
    """
    
    if nsteps <= 0:
        return start
    else:
        return rwpos_plain(start + rs(), nsteps -1)


def afw_calc(start, nsteps):
    """afw_calc een functie die afwijking berekend door eind - start
    

    Args:
        start (int): start getal
        nsteps (int): aantal stappen

    Returns:
        int: afwijking van startpositie
    """
    return rwpos_plain(start, nsteps) - start

def rwsteps(start, low, hi):
    """rwsteps Een spel waarbij je een startpunt, low en high geeft.
    De slaapwandelaar loopt random en geeft het aantal stappen terug wanneer het een muur raakt

    Args:
        start (int): start pos
        low (int): linker muur
        hi (int): rechtermuur
    """
    sys.stdout.flush()
    time.sleep(0.1)
    
    if start < low or start > hi:
        return 0
    else:
        print('|', (start-low)*'_', '\U0001F634' , (hi-start)*'_', '|')
        return 1 + rwsteps(start + rs(), low, hi)

def ave_signed_displacement(numtrials):
    """ave_signed_displacement neemt numtrials en maakt een lijst van numtrials keer de uitkomst fan rwpos_plain(0, 100)

    Args:
        numtrials (int): het aantal keer dat rwpos uitgevoerd moet worden en in de lijst moet worden gezet
    """
    lc = [rwpos_plain(0, 100) for x in range(numtrials)]
    avg_lc = sum(lc) / (len(lc)-1)
    print(lc)
    print('average: ', avg_lc)

def ave_squared_displacement(numtrials):
    lc = [rwpos_plain(0,100)**2 for x in range(numtrials)]
    avg_lc = sum(lc) / (len(lc)-1)
    print(lc)
    print('average: ', avg_lc)


""" 
    ave_signed_displacement geeft de totale afwijking van rwpos met 100 stappen, dit geeft de functie numtrials keer.
    als we de lijst nemen en hier een gemiddelde van berekenen, krijgen we bij kleine numtrials een veel varierend getal. 
    Zodra we numtrials groter maken, zien we dat het gemiddelde verder richting de 0 blijft hangen. en bij numtrials = 1000
    krijgen we soms zelfs gemiddelden met 1 nul achter de punt!
    ave_signed_displacement(1000)
    [-10, 10, 6, 12, -12, -4, -4, 24, 20, 18, 6, 8, -20, -6, 28, -12, -2, -4, 8, 20, 2, 0, 0, -34, ....
    average: 0.062062062062062065

    Bij de totale afwijking van ave_squared is het een ander verhaal. Bij het uitvoeren van veel tests
    zie je dat de uitkomsten van het gemiddelde allemaal rond het aantal stappen van rwpos_plain blijven hangen.
    Als je het aantal stappen verandert van 100 naar bijv. 140, dan zal de uitkomst van de test ook vaak hoger uitvallen: rond de 140.
    Dit is te verklaren omdat bij de uitkomst van rwpos_plain de lage getallen in het kwadraat niet relatief heel hoog zijn, maar zodra je bij grotere getallen komt, zal 
    het kwadraat ook relatief hoger worden. Dus weeg je eigenlijk de hogere getallen zwaarder dan de lage getallen, zodat de som ook erg groot wordt. 
    Net zoals bij ave_signed_displacement, zal een grotere numtrials ook zorgen voor een kleinere afwijking van nsteps van rwpos_plain
    voorbeeld:
    ave_squared_displacement(30)
    [64, 100, 324, 36, 0, 196, 324, 324, 400, 0, 196, 484, 484, 196, 64, 100, 144, 100, 0, 36, 4, 144, 256, 64, 4, 144, 36, 36, 4, 
    36]
    148.27586206896552
 """

#
#Bonusopgave
#

def rs_2d():
    """rs_2d Geeft een random waarde mee.
    We gebruiken ook 0, omdat we dit aanroepen voor zowel een horizontale als een verticale stap, en als je voor beide van deze alleen -1 of 1 hebt, zal het spel snel eindigen.

    return: een stap -1, 0 of 1 
    """
    #steps_pos = [-1, 0, 1]
    return random.choice([-1, 0, 1])




def rwsteps_2d(start, length, height):
    """rwsteps_2d Een spel waarbij je een x en y coordinaat geeft en een ruimte met lengte en breedte.
    zodra de ruimte is gemaakt zal via random choice een stap gemaakt worden in hor, vert richting, ook kan het geen van beide of beide tegelijk zijn.
    Zodra de slaapwandelaar een muur raakt is het spel voorbij

    Args:
        start (list): start pos in de vorm [x,y]
        length (int): lengte
        height (int): breedte 
    """
    
    sys.stdout.flush()
    time.sleep(0.3)

    if start[0] == 0 or start[0] == length+1:
        print('kopstoot! Spel gestopt')
        return
    elif start[1] == 0 or start[1] == height+1:
         print('kopstoot! Spel gestopt')
         return
    else:


        #print een lege lengte tot start[1]
        #print dan een ruimte met poppetje op start[0]
        #print dan rest lege ruimtes

        print(' ' + '~' * length)
        for x in range(start[1]-1):
            print('|' + '_'*length + '|')
        print('|' + '_'*(start[0]-1) + '\U0001F634' + '_' * (length-start[0])  + '|')
        for x in range(height-start[1]):
            print('|' + '_'*length + '|')
        print(' ' + '~' * length)

        start[0] = start[0] + rs_2d()
        start[1] = start[1] + rs_2d()
        
        return rwsteps_2d(start,length,height)