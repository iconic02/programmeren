#
#wk9ex3.py
#Naam: Timo Kosse
#


def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Doorgaan!")
    print("(1) Nieuwe lijst invoeren")
    print("(2) Volgende element voorspellen")
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


def main():
    """The main user-interaction loop"""
    secret_value = 4.2

    L = [30, 10, 20]  # een beginlijst

    while True:     # de lus voor gebruikersinteractie
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

        elif choice == 0:  # We willen doorgaan...
            continue       # Terug naar het begin van de while-lus

        elif choice == 1:  # We willen een nieuwe lijst invoeren
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

        elif choice == 2:   # Het volgende element voorspellen en toevoegen
            n = predict(L)  # Het volgende element uit de functie predict halen
            print("Het volgende element is", n)
            print("Het wordt toegevoegd aan je lijst...")
            L = L + [n]     # ...en toevoegen aan de lijst

        elif choice == 3:  # Geheime menu-optoe!
            pass       # Dit is het "nop"- (niets-doen) statement in Python

        elif choice == 4:  # Geheime menu-optie (iets interessanter...)
            m = find_min(L)
            print("De kleinste waarde van L is", m)

        elif choice == 5:  # Nog een geheime menu-optie (nog interessanter...)
            min_val, min_loc = find_min_loc(l)
            print("De kleinste waarde van L is", min_val, "op dag #", min_loc)

        else:
            print(choice, " ?      Dat staat niet op het menu!")

    print()
    print("Tot gisteren!")