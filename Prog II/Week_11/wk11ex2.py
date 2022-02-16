#
# week 11 ex 2
# AI voor 4-op-een-rij
#
# Naam: Timo Kosse

import sys, time, random

#in een rij checks
def in_a_row_n_east(ch, r_start, c_start, a, n):
    rows = len(a)
    cols = len(a[0])

    if c_start > cols -n or c_start < 0:
        return False
    if r_start < 0 or r_start >= rows:
        return False

    for i in range(n):
        if a[r_start][c_start + i] != ch:
            return False
    return True


def in_a_row_n_south(ch, r_start, c_start, a, n):
    rows = len(a)
    cols = len(a[0])


    if r_start < 0 or r_start > rows -n:
        return False
    if c_start < 0 or c_start >= cols:
        return False

    for i in range(n):
        if a[r_start + i][c_start] != ch:
            return False
    return True


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    rows = len(a)
    cols = len(a[0])


    if c_start < 0 or c_start > cols -n:
        return False
    if r_start < 0 or r_start > rows -n:
        return False

    for i in range(n):
        if a[r_start + i][c_start + i] != ch:
            return False
    return True


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    rows = len(a)
    cols = len(a[0])


    if r_start < n-1 or r_start >= rows:
        return False
    if c_start < 0 or c_start > cols -n:
        return False

    for i in range(n):
        if a[r_start - i][c_start + i] != ch:
            return False
    return True


#class Board

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # de string om terug te geven
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # onderkant van het bord
        s += '\n'

        for w in range(self.width):
            s += ' '
            s += str(w%10)

        # hier moeten de nummers nog onder gezet worden

        return s       # het bord is compleet, geef het terug

    
    def add_move(self, col, ox):
        """add_move neemt een colom en een character dat wordt toegevoegd   
        

        Args:
            col (int):  kolom nummer
            ox (str): character X of O
        """
        if ox != 'X' and ox != 'O':
            return
        for i in range(1, self.height +1):
            if self.data[self.height-i][col] == ' ':
                self.data[self.height-i][col] = ox
                break
        

    def clear(self):
        """clear when called, will clear the board
        """
        for col in range(self.width):
            for row in range(self.height):
                self.data[row][col] = ' '
    

    def set_board(self, move_string):
        """set_board neemt een set met moves en implementeerd dit in het spel.

        Args:
            move_string (string): een string met alle sets
        """
        ox = 'X'
        self.clear()
        for i in move_string:
            if 0<= int(i) <= self.width:
                self.add_move(int(i),ox)
            if ox == 'X':
                ox = 'O'
            elif ox == 'O':
                ox = 'X'


    def allows_move(self,col):
        """allows_move neemt col en kijkt of er daar een set kan worden gemaakt.

        Args:
            col (int): kolom nummer
        """
        if col < 0 or col > self.width -1:
            return False
        elif self.data[0][col] != ' ':
            return False
        else:
            return True


    def is_full(self):
        """is_full geeft terug of het hele bord gevuld is met stenen
        """
        for i in range(self.width-1):
            if self.allows_move(i) == True:
                return False
        return True
        

    def del_move(self, col):
        """del_move deletes the upper stone on the given column

        Args:
            col (int): column number
        """
        for i in range(self.height):
            if self.data[i][col] != ' ':
                self.data[i][col] = ' '
                break


    def wins_for(self,ox):
        """wins_for checks if someone has won the game

        Args:
            ox (string): character that needs to be checked
        """
        for col in range(self.width):
            for row in range(self.height):
                if in_a_row_n_east(ox, row, col, self.data, 4) == True:
                    return True
                if in_a_row_n_south(ox, row, col, self.data, 4) == True:
                    return True
                if in_a_row_n_southeast(ox, row, col, self.data, 4) == True:
                    return True
                if in_a_row_n_northeast(ox, row, col, self.data, 4) == True:
                    return True
        return False
        

    def cols_to_win(self, ox):
        """cols_to_win geeft alle kolommen terug waarmee ox kan winnen

        Args:
            ox (string): het character voor de check
        """
        b = False
        win_list = []
        for i in range(self.width):
            if self.allows_move(i):
                b = True
                self.add_move(i, ox)
            if self.wins_for(ox):
                win_list.append(i)
            if b == True:
                self.del_move(i)
            b = False
        return win_list


    def ai_move(self, ox):
        """ai_move takex ox and gives back an integer that resembles the colom it will go for

        Args:
            ox (string): the character
        """
        my_list = self.cols_to_win(ox)
        if ox == 'X':
            enem_ox = 'O'
        else:
            enem_ox = 'X'
        enem_list = self.cols_to_win(enem_ox)
        
        if my_list != []:
            return my_list[0]
        elif enem_list != []:
            return enem_list[0]
        else:
            ai_choice = random.randint(0, self.width-1)
            return ai_choice


    def host_game(self):
        sys.stdout.flush()
        """host_game Zorgt dat alles samenkomt tot een geheel spel
        """
        dubble_ai = False
        self.clear()
        print('Welkom bij 4 op een rij, wil je X, of O zijn?') # keuze geven
        print('Of wil je dat de AI allebei speelt? typ daarvoor: allebei')
        choice = input()
        choice = choice.upper()
        if choice ==  'X':
            enem = 'O'
        elif choice == 'O':
            enem = 'X'
        elif choice == 'ALLEBEI':
            dubble_ai = True
        else: 
            print('Geen geldige keuze')
            self.host_game()

        #begin spel
        print('\n')
        print(self)

        if dubble_ai == True:  #dubbele AI
            while self.is_full() == False:
                ai1 = 'X'
                ai2 = 'O'
                b = self.ai_move(ai1)
                print('\n' + 'Keuze van AI nummer 1 (' + ai1 + ') : ', b)
                time.sleep(1)
                if self.allows_move(b):
                    self.add_move(b, ai1)
                print(self)
                time.sleep(1)
                if self.wins_for(ai1) == True:
                    print('AI nummer 1 (' + ai1 + ') heeft het spel gewonnen!')
                    return

                c = self.ai_move(ai2)
                print('\n' + 'Keuze van AI nummer 2 (' + ai2 + ') : ', c)
                time.sleep(1)
                if self.allows_move(c):
                    self.add_move(c, ai2)
                print(self)
                time.sleep(1)
                if self.wins_for(ai2) == True:
                    print('AI nummer 2 (' + ai2 + ') heeft het spel gewonnen!')
                    return
            print('Niemand won, het bord is vol...')
            return

        # Speler tegen AI
        else:
            while self.is_full() == False:
                b = input('\n' + 'Keuze van jou (' + choice + ') : ')
                b = int(b)
                if self.allows_move(b) == True:
                    self.add_move(b, choice)
                    print(self)
                else:
                    print('ongeldige keuze')
                if self.wins_for(choice) == True:
                    print('Player (' + choice + ') heeft het spel gewonnen!')
                    return

                b = self.ai_move(enem)
                print('\n' + 'Keuze van AI (' + enem + ') : ', b)
                if self.allows_move(b):
                    self.add_move(b, enem)
                print(self)
                if self.wins_for(enem) == True:
                    print('AI (' + enem + ') heeft het spel gewonnen!')
                    return
            print('Niemand won, het bord is vol...')
            return

    
