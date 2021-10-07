#
# wk1ex2a.py
#

import time          # importeer de module met de naam time
import random        # importeer de module met de naam random
from sys import exit

def rps():
    """ this plays a game of rock-paper-scissors in Dutch ("steen"-"papier"-"schaar")
        The variety is that there are also the "hagedis" and the "spock"
        link to game: https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    #computer kiest
    comp = random.choice(['steen', 'papier', 'schaar', 'hagedis', 'spock'])

    #user kiest
    print('Kies je wapen [steen, papier, schaar, hagedis, spock ]:')
    user = input('Kies een optie: ')
    user = user.lower()

    print('Jij kiest: ', user)
    print('Ik koos:', comp)
    print()
    time.sleep(2)

    #check of input 1 van de keuzes is
    if user == 'steen' or user == 'papier' or user == 'schaar' or user == 'hagedis' or user == 'spock':
        print('Geldige input')
    
    
        #check voor gelijkspel
        if user == comp:
            print('Gelijkspel!')

        if user == 'steen':
            if comp == 'papier':
                print('Papier bedekt Steen ')
                print('Ik win ')
            if comp == 'schaar':
                print('Steen vernietigd Schaar ')
                print('Jij wint ')
            if comp == 'hagedis':
                print('Steen vermorzeld Hagedis ')
                print('Jij wint ')
            if comp == 'spock':
                print('Spock verdampt Steen ')
                print('Ik win ')

        if user == 'papier':
            if comp == 'steen':
                print('Papier bedekt Steen ')
                print('Jij wint ')
            if comp == 'schaar':
                print('Schaar knipt Papier ')
                print('Ik win ')
            if comp == 'hagedis':
                print('Hagedis eet Papier ')
                print('Ik win ')
            if comp == 'spock':
                print('Papier weerlegt Spock ')
                print('Jij wint ')

        if user == 'schaar':
            if comp == 'steen':
                print('Steen vernietigd Schaar ')
                print('Ik win ')
            if comp == 'papier':
                print('Schaar knipt Papier ')
                print('Jij wint ')
            if comp == 'hagedis':
                print('Schaar onthoofd Hagedis ')
                print('Jij wint ')
            if comp == 'spock':
                print('Spock vernietigd Schaar ')
                print('Ik win ')
        
        if user == 'hagedis':
            if comp == 'steen':
                print('Steen vermorzeld Hagedis ')
                print('Ik win ')
            if comp == 'papier':
                print('Hagedis eet Papier ')
                print('Jij wint ')
            if comp == 'schaar':
                print('Schaar onthoofd Hagedis ')
                print('Ik win ')
            if comp == 'spock':
                print('Hagedis vergiftigd Spock ')
                print('Jij wint ')
        
        if user == 'spock':
            if comp == 'steen':
                print('Spock verdampt Steen ')
                print('Jij wint ')
            if comp == 'papier':
                print('Papier weerlegt Spock ')
                print('Ik win ')
            if comp == 'schaar':
                print('Spock vernietigd Schaar ')
                print('Jij wint ')
            if comp == 'hagedis':
                print('Hagedis vergiftigd Spock ')
                print('Ik win ')  
    else:
        print('Hmm, geen geldige input')

        
    #vraag voor retry, bij N of een andere input exit.
    retry = input('Wil je nog een keer? [Y/N]')
    if retry == 'Y':
        rps()
    



