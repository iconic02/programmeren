#
# wk10ex1.py
#
# naam:
#

# Eerst de klassedefinitie
# Hieronder definiëren we een aantal handige objecten van het type Date
#  +++ bewaar die en/of voeg je eigen toe! +++


class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # de constructor heet altijd __init__ !
    def __init__(self, day, month, year):
        """Construct a Date with the given day, month, and year."""
        self.day = day
        self.month = month
        self.year = year

    # de "afdruk"-functie heet altijd __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}-{:02d}-{:04d}".format(self.day, self.month, self.year)
        return s


    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way, we don't need to use the awkward
            d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False


    def __lt__(self, d2):
        """__lt__ past het less than controle aan

        Args:
            d2 (Datum): vergelijkende datum

        Returns:
            boolean: True of False
        """
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
        return False
    

    def __gt__(self, d2):
        """__gt__ greater than, geeft terug of self groter is dan d2

        Args:
            d2 (date): de tweede datum

        Returns:
            boolean: True of False
        """
        if self.year > d2.year:
            return True
        elif self.year == d2.year:
            if self.month > d2.month:
                return True
            elif self.month == d2.month:
                if self.day > d2.day:
                    return True
        return False

    
    def __iadd__(self, n):
        """__iadd__ += operator redivined to equal add_n_days()

        Args:
            n (int): number added

        Returns:
            Date: a new date
        """
        



    # Hier is een voorbeeld van een "methode" van de klasse Date:
    def is_leap_year(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False


    def copy(self):
        """copy kopiëerd een datum naar een tweede var 
        """
        dnew = Date(self.day, self.month, self.year)
        return dnew

    
    def equals(self, d2):
        """equals neemt 2 data en kijkt of ze gelijk zijn

        Args:
            d2 (
                data 2
            ): de andere data
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False





    def is_before(self, d2):
        """is_before Geeft True terug als self eerder voorkomt dan d2, anders False

        Args:
            d2 (Date): de te vergelijken data

        """
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
        return False


    def is_after(self, d2):
        """is_after geeft terug of self voor d2 is.

        Args:
            d2 (Date): een datum
        """
        if self.year > d2.year:
            return True
        elif self.year == d2.year:
            if self.month > d2.month:
                return True
            elif self.month == d2.month:
                if self.day > d2.day:
                    return True
        return False


    def tomorrow(self):
        """tomorrow verandert self naar 1 dag later
        """
        if self.month in [1,3,5,7,8,10]:
            if self.day == 31:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        elif self.month in [4,6,9,11]:
            if self.day == 30:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        elif self.month == 2:
            if self.day == 28 and self.is_leap_year() == False:
                self.day = 1
                self.month += 1
            elif self.day == 29 and self.is_leap_year() == True:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        elif self.month == 12:
            if self.day == 31:
                self.year += 1
                self.month = 1
                self.day = 1
            else:
                self.day += 1
        

    def yesterday(self):
        """yesterday takes a date and sets it back one day
        """
        if self.month in [2,4,6,8,9,11]:
            if self.day == 1:
                self.day = 31
                self.month -= 1
            else:
                self.day -= 1
        elif self.month in [5,7,10,12]:
            if self.day == 1:
                self.day = 30
                self.month -= 1
            else:
                self.day -= 1
        elif self.month == 3:
            if self.day == 1 and self.is_leap_year() == False:
                self.day = 28
                self.month -= 1
            elif self.day == 1 and self.is_leap_year() == True:
                self.day = 29
                self.month -= 1
            else:
                self.day -= 1
        elif self.month == 1:
            if self.day == 1:
                self.year -= 1
                self.month = 12
                self.day = 31
            else:
                self.day -= 1


    def add_n_days(self, n):
        """add_n_days takes self and n and adds n days to self.

        Args:
            n (int): days added    
        """
        for i in range(n):
            self.tomorrow()
            print(self)

            
    def sub_n_day(self, n):
        """sub_n_day takes self and n and subtracts n days from self

        Args:
            n (int): days removed
        """
        for i in range(n):
            self.yesterday()
            print(self)



d = Date(1,1,2001)
d2 = Date.copy(d)
assert Date.__eq__(d, d2)

ny = Date(1, 1, 2021)
d = Date(2, 12, 2020)
assert ny.is_before(d) == False
assert d.is_before(ny)
assert not d.is_before(d)
assert d < ny 

assert ny.is_after(d)
assert not d.is_after(ny)
assert not d.is_after(d)
assert ny > d

d = Date(31,12,2020)
d.tomorrow()
assert str(d) == '01-01-2021'
d = Date(28, 2, 2020)
d.tomorrow()
assert str(d) == '29-02-2020'

d = Date(1,1,2021)
d.yesterday()
assert str(d) == '31-12-2020'
d = Date(1,3,2021)
d.yesterday()
assert str(d) == '28-02-2021'



#
# vergeet niet je code voor de klasse Date HIERBOVEN toe te voegen; in de klassedefinitie
#


#
# een aantal datums om mee te werken...
#
# Het handige van ze hier plaatsen is dat ze elke keer dat de software uitgevoerd
#   wordt ze opnieuw gedefinieerd worden (en dat is nodig om te testen!)
#

d = Date(2, 12, 2020)    # Vandaag?
d2 = Date(21, 12, 2020)   # Kerstvakantie
ny = Date(1, 1, 2021)   # Nieuwjaar
nd = Date(1, 1, 2030)   # Nieuw decennium
nc = Date(1, 1, 2100)   # Nieuwe eeuw
graduation = Date(12, 7, 2024)   # Pas dit zelf aan!
vacation = Date(19, 7, 2021)     # Dit ook ~ zomervakantie!
sm1 = Date(28, 10, 1929)    # Krach aandelenbeurs
sm2 = Date(19, 10, 1987)    # Nog een beurskrach: Maandagen in okt. zijn gevaarlijk...
