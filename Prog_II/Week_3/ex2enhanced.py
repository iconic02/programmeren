import random  
import sys
import time


def rs():
    """rs_2d Geeft 2 waarden mee: een nummer horizontaal en een verticaal

    :
    hor = horizontale keuze
    vert = verticale keuze
    """
    steps_pos = [-1, 0, 1]
    return random.choice(steps_pos)




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

        start[0] = start[0] + rs()
        start[1] = start[1] + rs()
        
        return rwsteps_2d(start,length,height)





#temp storage code
"""
    field_length = '|' + '_'*length + '|'
    field_height = (field_length + '\n') * height
    
    print(field_height)

    field_length[start[0]+1] = '\U0001F634'
"""
    


    