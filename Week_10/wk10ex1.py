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
        for i in range(n):
            self.tomorrow
        return self

    
    def __isub__(self, n):
        """__isub__ -= operator redivined to equal sub_n_days()


        Args:
            n (int): number of days

        Returns:
            Date: the new date
        """
        for i in range(n):
            self.yesterday
        return self


    def __sub__(self, d2):
        """__sub__ gives the difference between self and d2.

        Args:
            d2 (Date): the other date

        Returns:
            int: the number of days difference
        """
        if self.is_after(d2):
            diff = self.diff(d2)
            return diff
        elif self.is_before(d2):
            diff = self.diff(d2)
            return diff
        else:
            return 0




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
            print(self)
            self.tomorrow()
            

            
    def sub_n_days(self, n):
        """sub_n_days takes self and n and subtracts n days from self

        Args:
            n (int): days removed
        """
        for i in range(n):            
            print(self)
            self.yesterday()


    def diff(self, d2):
        """diff gives the amount of days 2 dates differ. 

        Args:
            d2 (Date): the other date
        """
        new_self = self.copy()
        new_d2 = d2.copy()
        count = 0
        if new_self.is_before(new_d2):
            while True:
                count += 1
                new_self.tomorrow()
                if new_self.equals(new_d2):
                    break
        elif new_self.is_after(new_d2):
            while True:
                count -= 1
                new_self.yesterday()
                if new_self.equals(new_d2):
                    break
        return count


    def dow(self):
        """dow geeft de day of the week terug
        """
        date = Date(10,10,2010)
        difference = abs(self - date) % 7
        lijstje = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        dag = lijstje[difference]
        return dag


    def dow2(self, ref_date):
        """dow2 a new function for dow, which will help speed up day13_counter

        Args:
            ref_date (Date): a reference date
        """
        difference = abs(self - ref_date) % 7
        lijstje = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        dag = lijstje[difference]
        return dag


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

d = Date(1,1,2021)
d2 = Date(9,1,2021)
assert d.diff(d2) == 8

d = Date(19,12,2021)
d2 = Date(20,12,2021)
assert d.dow() == 'Sunday'
assert d2.dow() == 'Monday'



# bonusopdrachten



def ny_counter():
    """Kijkt voor de volgende 100 jaar, op welke dagen de nieuwjaars dagen vallen.
    De functie geeft de totalen na het tellen terug
    """

    dowd = {}              # dowd is een dictionary van weekdagen
    dowd["Sunday"] = 0     # een waarde van 0 voor Sunday
    dowd["Monday"] = 0     # en zo verder...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # 100 jaar vooruit kijken...
    for year in range(2021, 2121):
        d = Date(1, 1, year)   # nieuwjaar opvragen
        print('Huidige datum is', d)
        s = d.dow()        # dag van de week zoeken
        dowd[s] += 1       # tellen

    print('Totalen zijn', dowd)

    # we zouden dowd hier kunnen teruggeven
    # maar dat is nu niet nodig
    # return dowd


def bday_counter():
    """Kijkt voor de volgende 100 jaar, op welke dagen mijn verjaardagen vallen.
    De functie geeft de totalen na het tellen terug
    """

    dowd = {}              # dowd is een dictionary van weekdagen
    dowd["Sunday"] = 0     # een waarde van 0 voor Sunday
    dowd["Monday"] = 0     # en zo verder...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # 100 jaar vooruit kijken...
    for year in range(2021, 2121):
        d = Date(22, 6, year)   # nieuwjaar opvragen
        print('Huidige datum is', d)
        s = d.dow()        # dag van de week zoeken
        dowd[s] += 1       # tellen

    print('Totalen zijn', dowd)

# Totalen zijn {'Sunday': 14, 'Monday': 14, 'Tuesday': 15, 'Wednesday': 15, 'Thursday': 14, 'Friday': 14, 'Saturday': 14}



def day13_counter():
    """f13_counter geeft terug op welke dagen de 13e valt. Bekijkt voor de volgende 400 jaar
    """
    dowd = {}              
    dowd["Sunday"] = 0     
    dowd["Monday"] = 0     
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    ref_date = Date(10,10,2010)
    for year in range(2021, 2421):
        print('The year is: ', year)
        for month in range(1,13):
            d = Date(13, month, year)   
            if d.dow2(ref_date) == 'Sunday':
                ref_date = d.copy()
            s = d.dow2(ref_date)       
            dowd[s] += 1       

    print('Totalen zijn', dowd)


    # Totalen zijn {'Sunday': 687, 'Monday': 685, 'Tuesday': 685, 'Wednesday': 687, 'Thursday': 684, 'Friday': 688, 'Saturday': 684}