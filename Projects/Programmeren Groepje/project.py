# Milestone.py
# Namen: Timo Kosse, Mark Kuipers, Karel Lucidore
# Klas: ITV-1D
#
#



import random

# De klasse Board
class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]
        self.moves = 0
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

        # hier moeten de nummers nog onder gezet worden
        s += '\n'
        for i in range(self.width):
            s += ' ' + str(i%10)

        return s       # het bord is compleet, geef het terug

    def add_move(self, col, ox):
        """Adds a stone for player ox to column col"""
        i = 0
        while i < self.height and self.data[i][col] == ' ':
            i += 1
        self.data[i-1][col] = ox

    def clear(self):
        """Clears the board"""
        self.data = [[' ']*self.width for _ in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.set_board('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.set_board('000000') to
           see them alternate in the left column.

           move_string must be a string of one-digit integers.
        """
        next_checker = 'X'  # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allows_move(self, col):
        """Checks whether column col can be played"""
        return 0 <= col < self.width and self.data[0][col] == ' '

    def is_full(self):
        """Checks whether the board is full"""
        for col in range(self.width):
            if self.allows_move(col):
                return False
        return True

    def del_move(self, col):
        """Removes a stone from column col"""
        i = 0
        while i < self.height and self.data[i][col] == ' ':
            i += 1
        if i < self.height:
            self.data[i][col] = ' '

    def del_lowest(self,col):
        """Deletes the lowest ox of a row
        """
        
        

    def wins_for(self, ox):
        """Checks whether player ox wins the game"""
        for y in range(self.height):
            for x in range(self.width):
                if in_a_row_n_east(ox, y, x, self.data, 4) or in_a_row_n_south(ox, y, x, self.data, 4) or \
                    in_a_row_n_southeast(ox, y, x, self.data, 4) or in_a_row_n_northeast(ox, y, x, self.data, 4):
                    return True
        return False

    def row_full(self):
        """Checks if a row is full
        """
        for col in range(self.width):
            print(col)
            if self.data[self.height-1][col] == ' ':
                print('returning')
                return
        for i in range(self.width):
            print('deleting')
            self.data[self.height-1][i] = ' '
        for col in range(self.width):
            for row in range(self.height-2, 0, -1):
                car = self.data[row][col]
                self.data[row+1][col] = car


    def host_game(self):
        """Plays a game of Connect Four"""
        ox = 'O'
        while True:
            # druk het bord af
            print(self)

            # controleer of het spel afgelopen is
            if self.wins_for(ox):
                print(ox, 'heeft gewonnen!')
                break
            elif self.is_full():
                print('Gelijkspel!')
                break

            # verander de huidige speler
            if ox == 'O':
                ox = 'X'
            else:
                ox = 'O'

            # laat de speler een kolom kiezen
            col = -1
            while not self.allows_move(col):
                col = int(input('Kolom voor '+ox+': '))

            # voer de zet uit
            self.add_move(col, ox)

    def switch(self, percentage):
        """
        """
        change = random.choice(range(percentage))
        if self.moves == 21:
            return True
        if change == 0:
            return True
        else:
            return False

    def play_game(self, px, po, show_scores=False):
        """
        Plays a game of Connect Four between players px and po.
        If show_scores is True, the player's board evaluations are printed each turn.
        """
        print("Je kunt kiezen of je zelf wil spelen,")
        print("of het allemaal van de AI laten afhangen.")
        ai_or_human = input("[zelf/ai]: ")
        while ai_or_human != "zelf" and ai_or_human != "ai":
                print("Kies alsjeblieft een geldig antwoord: ")
                ai_or_human = input("[zelf/ai]: ")

        if ai_or_human == 'zelf':
            px = "human"

        print("\nHoe groot moet je kans zijn op een karakter switch?")
        print("Hoe hoger de integer, hoe kleiner de kans")
        percentage = int(input("integer tussen 1 en 10: "))
        

        # px en po zien er zo uit: Player('X', 'LEFT', 0)
        
        ox = 'O'
        while True:
            # druk het bord af
            print(self)
            print()

            # controleer of het spel afgelopen is
            if self.wins_for(ox):
                print(f'{ox} heeft gewonnen!')
                break
            elif self.is_full():
                print('Gelijkspel!')
                break

            # verander de huidige speler, maar niet als de switch aan staat
            if self.switch(percentage) == True:
                """"""

            if ox == 'O':
                ox = 'X'
                player = px
            else:
                ox = 'O'
                player = po      


            if player == 'human':
                # laat de menselijke speler een kolom kiezen
                col = -1
                while not self.allows_move(col):
                    col = int(input('Kolom voor ' + ox + ': '))
            else:
                # de computerspeler berekent een zet
                if show_scores:
                    scores = player.scores_for(self)
                    print('Scores voor ', ox, ':', [int(sc) for sc in scores])
                    col = player.tiebreak_move(scores)
                else:
                    col = player.next_move(self)

            # voer de zet uit
            self.add_move(col, ox)
            self.row_full()


def in_a_row_n_east(ch, r_start, c_start, a, n):
    """Checks whether ch has n in a row starting at r_start, c_start going east"""
    if r_start < 0 or r_start >= len(a) or c_start < 0 or c_start >= len(a[0]) - n+1:
        return False
    for i in range(0, n):
        if a[r_start][c_start+i] != ch:
            return False
    return True

def in_a_row_n_south(ch, r_start, c_start, a, n):
    """Checks whether ch has n in a row starting at r_start, c_start going south"""
    if r_start < 0 or r_start >= len(a) - n+1 or c_start < 0 or c_start >= len(a[0]):
        return False
    for i in range(0, n):
        if a[r_start+i][c_start] != ch:
            return False
    return True

def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """Checks whether ch has n in a row starting at r_start, c_start going southeast"""
    if r_start < 0 or r_start >= len(a) - n+1 or c_start < 0 or c_start >= len(a[0]) - n+1:
        return False
    for i in range(0, n):
        if a[r_start+i][c_start+i] != ch:
            return False
    return True

def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """Checks whether ch has n in a row starting at r_start, c_start going northeast"""
    if r_start < n-1 or r_start >= len(a) or c_start < 0 or c_start >= len(a[0]) - n+1:
        return False
    for i in range(0, n):
        if a[r_start-i][c_start+i] != ch:
            return False
    return True


# De Klasse Player

class Player:
    """An AI player for Connect Four."""

    # de constructor van Player
    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply


    # de representatie van Player
    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player: ox = " + self.ox + ", "
        s += "tbt = " + self.tbt + ", "
        s += "ply = " + str(self.ply)
        return s


# begin methodes
    # Functie opp_ch
    def opp_ch(self):
        """Returns the opposite character from Player
        """
        s = "O"             # Ga ervan dat O tegenovergestelde is van self

        if s == self.ox:    # Als dat niet zo is, maak er dan X van
            s = "X"
    
        return s


    # Functie score_board
    def score_board(self,b):
        """Geeft de score van de set van Player terug
        """
        winS = b.wins_for(self.ox)          
        winOpp = b.wins_for(self.opp_ch())
        
        if winS == True:        # Wint Self? dan 100.0 punten
            return 100.0
        elif winOpp == True:    # Wint Opposite? dan 0.0 punten
            return 0.0
        else:                   # Anders gebeurt er nog niks en dan 50.0 punten
            return 50.0


    # Functie tiebreak_move
    def tiebreak_move(self, scores):
        """ Krijgt lijst scores mee, die floating point getallen bevat.
        De functie geeft de hoogste score terug.
        """
        # vind de max
        highest = max(scores)       # voor alle 3
        lijst_met_hoogste = []      # voor random
        index = 0                   # voor alle 3
        
        # RANDOM als strategie
        if self.tbt == "RANDOM":
            for i in scores:
                if i == highest:
                    lijst_met_hoogste.append(index)
                index += 1
            kolomnummer = random.choice(lijst_met_hoogste)
        
        # links als strategie
        elif self.tbt == "LEFT":
            for i in scores:
                if i == highest:
                    kolomnummer = index
                    break
                else:
                    index += 1

        # rechts als strategie
        elif self.tbt == "RIGHT":
            lijst_omg = scores[::-1]  #lijst omdraaien voor RIGHT (Hebreeuws lezen)
            index = 0
            for i in lijst_omg:
                if i == highest:
                    kolomnummer = (len(scores) -1) - index 
                    break
                else:
                    index += 1 
        
        return kolomnummer
        

    def scores_for(self, b):
        """ Deze functie moet een lijst met scores teruggeven.
        Op index c word aangegeven hoe 'goed' het bord is na de zet.
        """
        # Als er niks verandert, is elke kolom een "onbekende" mogelijkheid
        scores = [50.0] * b.width

        # for loop om elke mogelijkheid in elke kolom een waarde te geven
        for col in range(b.width):
            # Als kolom vol is, geef waarde -1.0
            if b.allows_move(col) == False:
                scores[col] = -1.0
            
            # Met een eigen win in het bord, kolomwaarde 100.0
            elif b.wins_for(self.ox) == True:
                scores[col] = 100.0

            # Met een tegenstander win, kolomwaarde 0.0 
            elif b.wins_for(self.opp_ch()) == True:
                scores[col] = 0.0
            
            # Niet verder kijken? Elke mogelijkheid is "onbekend" dus 50.0
            elif self.ply == 0:
                scores[col] = 50.0
            
            # Verder kijken met self.ply
            elif self.ply > 0:
                b.add_move(col, self.ox)
                # Eigen win na zet? Kolomwaarde 100.0
                if b.wins_for(self.ox) == True:
                    scores[col] = 100.0
                
                # Win van tegenstander? Kolomwaarde 0.0
                elif b.wins_for(self.opp_ch()) == True:
                    scores[col] = 0.0
                
                # Recursief ontdenken wat de tegenstanders waardes zouden zijn als
                # zhij na onze beurt zou spelen.
                else:
                    enemy = Player(self.opp_ch(), self.tbt, self.ply - 1)
                    enemy_scores = enemy.scores_for(b)
                    enemy_scores_max = enemy_scores[enemy.tiebreak_move(enemy_scores)]
                    scores[col] = 100.0 - enemy_scores_max
                
                b.del_move(col)

        return scores


    def next_move(self, b):
        """ De functie next_move krijgt een argument b mee
        en geeft een integer terug van het kolomnummer van het aanroepende object
        """

        score_lijst = self.scores_for(b)            # creeert lijst met score per kolom
        best_col = self.tiebreak_move(score_lijst)  # evalueert lijst

        return best_col




# Tests for function opp_ch
p = Player('X', 'LEFT', 3)
assert p.opp_ch() == 'O'
assert Player('O', 'LEFT', 0).opp_ch() == 'X'


#Tests for function score_board
b = Board(7, 6)
b.set_board('01020305')
#print(b)
p = Player('X', 'LEFT', 0)
assert p.score_board(b) == 100.0
assert Player('O', 'LEFT', 0).score_board(b) == 0.0
assert Player('O', 'LEFT', 0).score_board(Board(7, 6)) == 50.0


# Tests for function tiebreak_move
scores = [0, 0, 50, 0, 50, 50, 0]
p = Player('X', 'LEFT', 1)
p2 = Player('X', 'RIGHT', 1)
p3 = Player("X", "RANDOM", 1)
assert p.tiebreak_move(scores) == 2
assert p2.tiebreak_move(scores) == 5
assert p3.tiebreak_move(scores) in [2, 4, 5]


"""# Tests for function scores_for
b = Board(7, 6)
b.set_board('1211244445')
#print(b)
# 0-ply lookahead ziet geen bedreigingen
assert Player('X', 'LEFT', 0).scores_for(b) == [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]
# 1-play lookahead ziet een manier om te winnen
# (als het de beurt van 'O' was!)
assert Player('O', 'LEFT', 1).scores_for(b) == [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0]
# 2-ply lookahead ziet manieren om te verliezen
# ('X' kan maar beter in kolom 3 spelen...)
assert Player('X', 'LEFT', 2).scores_for(b) == [0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 0.0]
# 3-ply lookahead ziet indirecte overwinningen
# ('X' ziet dat kolom 3 een overwinning oplevert!)
assert Player('X', 'LEFT', 3).scores_for(b) == [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0]
# Bij 3-ply ziet 'O' nog geen gevaar
# als hij in een andere kolom speelt
assert Player('O', 'LEFT', 3).scores_for(b) == [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0]
# Maar bij 4-ply ziet 'O' wel het gevaar!
# weer jammer dat het niet de beurt van 'O' is...
assert Player('O', 'LEFT', 4).scores_for(b) == [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0]"""


# Tests for function next_move
b = Board(7, 6)
b.set_board('1211244445')
#print(b)

assert Player('X', 'LEFT', 1).next_move(b) == 0
assert Player('X', 'RIGHT', 1).next_move(b) == 6
assert Player('X', 'LEFT', 2).next_move(b) == 3

# de keuzestrategie maakt niet uit
# als er maar één beste zet is...
assert Player('X', 'RIGHT', 2).next_move(b) == 3

# nogmaals, de keuzestrategie maakt niet uit
# als er maar één beste zet is...
assert Player('X', 'RANDOM', 2).next_move(b) == 3