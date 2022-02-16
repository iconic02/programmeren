#
#wk9ex3.py
#
#Naam: Timo Kosse
#


def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Voer een nieuwe lijst in")
    print("(1) Druk de huidige lijst af")
    print("(2) Geef de gemiddelde prijs")
    print("(3) Geef de standaardafwijking")
    print("(4) Geef het minimum met de bijbehorende dag")
    print("(5) Geef het maximum met de bijbehorende dag")
    print("(6) Het beste investeringsplan")
    print("(9) Stoppen! (einde)")
    print()


def predict(L):
    """Predict ignores its argument and returns
       what the next element should have been.
    """
    return 42


def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:
            result = x
    return result


def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    min_val = L[0]
    min_loc = 0

    for i in list(range(len(L))):
        if L[i] < min_val:  # een kleinere gevonden!
            min_val = L[i]
            min_loc = i

    return min_val, min_loc

def find_avg(L):
    """find_avg geeft het gemiddelde van een lijst terug

    Args:
        L (list): de lijst met prijzen
    """
    count = 0
    num_items = 0
    for i in L:
        count += i
        num_items += 1
    return (count / num_items)


def find_standard_deviation(L):
    """find_standard_deviation kijkt voor lijst L wat de standaardafwijkingis

    Args:
        L (list): lijst met prijzen
    """
    sum_L = 0
    for i in L:
        b = (i - find_avg(L)) ** 2
        sum_L += b
    breuk = sum_L / len(L)
    total_sum = breuk ** 0.5
    return total_sum

assert find_standard_deviation([30, 20, 50]) == 12.47219128924647
assert find_standard_deviation([6.4, 70.3, 2.9, 50]) == 28.689806552153676
assert find_standard_deviation([4, 6.3, 8.1, 7, 3.4]) == 1.7872884490199112
assert find_standard_deviation([100, 300, 405, 209.67, 43]) == 131.22678318087355


def find_min_day(L):
    index = 0
    right_index = 0
    minimal = L[0]
    for i in L:
        if i < minimal:
            minimal = i
            right_index = index
        index += 1
    return minimal, right_index


def find_max_day(L):
    index = 0
    right_index = 0
    maximal = L[0]
    for i in L:
        if i > maximal:
            maximal = i
            right_index = index
        index += 1
    return maximal, right_index

def best_buy(L):
    max_profit = 0
    days = [0,0,0,0]
    for i in range(len(L)):
        for b in range(i + 1,len(L)):
            if L[b] - L[i] > max_profit:
                max_profit = L[b] - L[i]
                days = [i, L[i], b, L[b]]
    return max_profit, days





def main():
    """De kern van het programma, waaruit alle keuzes gemaakt kunnen worden
    """
    secret_value = 4.2

    L = [20, 10, 30]

    while True:     # de lus voor gebruikersinteractie. Door het een while loop te maken, kan na elke menu-keuze doorgewerkt worden
        print("\n\nDe lijst is", L)
        menu()
        choice = input("Maak een keuze: ")

        #
        # De invoer van de gebruiker "opschonen en controleren"
        # 
        try:
            choice = int(choice)   # omzetten naar een int!
        except:
            print("Ik begreep de invoer niet! Verder gaan...")
            continue

        # de gekozen menu-optie uitvoeren
        #
        if choice == 9:    # We willen stoppen
            break          # De hele while-lus afbreken

        elif choice == 0:  # Het invoeren van een lijst
            new_L = input("Voer een nieuwe lijst in: ")    # _iets_ invoeren

            #
            # De invoer van de gebruiker "opschonen en controleren"
            #
            try: 
                new_L = eval(new_L)   # eval voert de Python-interpreter uit! Let op: Gevaarlijk!
                if not isinstance(new_L, list): 
                    print("Dat lijkt geen lijst. L wordt niet aangepast.")
                else: 
                    L = new_L  # Hier is het wel OK, dus we passen onze lijst L aan
            except:
                print("Ik begreep de invoer niet. L wordt niet aangepast.")

        elif choice == 1:  #lijst uitprinten
            print(L)

        elif choice == 2:   # Gemiddelde geven
            print('het gemiddelde is ', find_avg(L))
            

        elif choice == 3:  # Standaard afwijking
            m = find_standard_deviation(L)
            print('standaardafwijking is ', m)


        elif choice == 4:  # Minimale bedrag en dag
            a,b = find_min_day(L)
            print("Het minimum is ", a, " op dag ", b + 1)

        elif choice == 5:  # Maximale bedrag en dag
            a,b = find_min_day(L)
            print("Het maximum is ", a, " op dag ", b + 1)

        elif choice == 6:   # Beste investeringsplan
            print("Het beste investeringsplan:")
            print()
            a,b = best_buy(L)
            print("Kopen op dag: ", b[0]+1, " voor ", b[1], " euro")
            print("Verkopen op dag ", b[2]+1, " voor ", b[3], " euro")
            print("Hiermee maak je ", a, " euro winst")


        else:
            print(choice, " ?      Dat staat niet op het menu!")
        
    print()
    print("Tot gisteren!")