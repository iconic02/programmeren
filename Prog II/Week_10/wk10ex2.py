#
# Wk10ex2.py
#
# Naam: Timo Kosse
#



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
        for i in range(1,self.height+1):
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
        print(self.data[0][col])
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


    def host_game(self):
        """host_game Zorgt dat alles samenkomt tot een geheel spel
        """
        self.clear()
        print('Welkom bij 4 op een rij, jij begint')
        print('\n')
        ox = 'X'
        print(self)
        while self.is_full() == False:
            b = input('Keuze van ' + ox + ' : ')
            b = int(b)
            if self.allows_move(b) == True:
                self.add_move(b, ox)
                print(self)
            else:
                print('ongeldige keuze')
                continue
            if self.wins_for(ox) == True:

                print(ox, ' heeft het spel gewonnen!')
                return
            if ox == 'X':
                ox = 'O'
            else: 
                ox = 'X'
        print('Niemand won, het bord is vol...')
        return
        