"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time


def adventure():
    """Runs one session of interactive fiction

    Well, it's "fiction," depending on the pill color chosen...

    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
    """
    # zet deze waarde op 0.0 om te testen of snel te spelen,
    # ..of hoger voor meer dramatisch effect!
    delay = 10.0

    print('Welkom avonturier. Wat is uw naam?')
    naam = input()

    #intro
    print('Tijdens dit avontuur bent u op zoek naar de rode draak, een bekende lokale legende.')
    time.sleep(5)
    print('Na een lang avontuur denk je dat je het nest van de draak hebt gevonden, waar hij al 500 jaar zou verschuilen. \nVeel krijgers zijn jullie voorgegaan, maar velen van hun zijn niet teruggekeerd. \nDegenen die wel terugkwamen, waren amper te herkennen door de blaren op hun huid.')
    time.sleep(5)
    print('Na jaren aan training denken jullie dat jullie het wél aan kunnen.')
    time.sleep(5)
    print('Het nest van de draak is in een krater in het midden van een grote berg. \nSamen met 4 krijgers werd jij op pad gestuurd om deze draak te verslaan, maar veel van de krijgers zijn tijdens de lange reis overleden. \nAlleen jij en je trouwe krijger Tibaltus zijn over. Jullie staan aan de voet van de berg. ')
    time.sleep(5)
    print('Jij: Dus, het lijkt dat we via de smalle paden naar boven moeten gaan, naar de top van de berg. \nMisschien dat bovenaan wel een plek is waar we in de krater naar beneden kunnen. ')
    time.sleep(5)
    print('Tibaltus: Tibaltus: Naar boven? Dat is wel een flink eind, misschien kunnen we beter een weg zoeken om \ndwars door de berg door een tunnel te gaan. De verhalen van onze voorouders spraken \nvan een tunnel dwars naar de draak.  ')
    time.sleep(5)
    print('Jij: Dat kan, maar de berg is groot, wat als het aan de andere kant van de berg is? \nDat zou ons zeker een dag langer duren om heen te komen, en wie weet is de tunnel wel ingestort?')
    time.sleep(5)
    print('Tibaltus: Dat is waar, beide opties hebben hun risico\'s, maar jij bent de leider, dus kies maar. ') 
    time.sleep(5)
    print('Wat ga je doen? Kies je het pad naar boven, of ga je op zoek naar de tunnel? ')
    time.sleep(5)
    keuze1 = input('[pad, tunnel]')

    #keuze pad of tunnel. Het pad zal meteen tot dood leiden. Tunnel geeft meer keuzes
    if keuze1 == 'pad':
        print('Jij: laten we via het pad gaan, er is maar weinig zekerheid van een tunnel,\n dus we kunnen het best via boven gaan. ')
        time.sleep(5)
        print('Jullie reizen uren omhoog, de paden worden steeds smaller en de berg steeds steiler. \nPlanten die uit de berg groeien, zijn jullie houvast om niet van de berg te vallen in de diepte.')
        time.sleep(5)
        print('Terwijl je achteromkijkt om te zien of Tibaltus nog bij kan blijven. Grijp je mis naar een plant. \nJe raakt je balans kwijt en probeert nog een wortel van een boom vast te pakken. ')
        time.sleep(5)
        print('Terwijl Tibaltus je probeert te redden, breek te tak af en vallen jij en Tibaltus in de diepte. ')
        time.sleep(2)
        death()


    elif keuze1 == 'tunnel':
        print('Jullie zoeken uren naar de tunnel, maar gelukkig is hij ook snel gevonden. \nTibaltus zien hem achter wat dichtgegroeide planten en met jullie zwaarden maken jullie de ingang zichtbaar. ')
        time.sleep(5)
        print('Jullie lopen de tunnel in. Na een half uur komen jullie een kruising tegen. \nJe kunt naar voren, links, rechts of terug ')
        time.sleep(5)
        print('Waar ga je heen? ')
        time.sleep(5)
        keuze2 = input('[voor, links, rechts, terug]')
        time.sleep(5)
    # user krijgt keuze waarheen. Links geeft winnende antwoord.
        if keuze2 == 'voor':
            print('nadat jullie de gang in zijn gelopen, hoor je iets onder je voet bewegen. \nOpeens zakt je voet een stuk weg, omdat de steen onder je ingedrukt wordt.')
            time.sleep(5)
            print('Hierna begint de hele tunnel te schudden. Achter je valt een steen in de gang, \ndie de terugweg blokkeerd. Jullie rennen naar voren, terwijl achter je de stenen blijven vallen.')
            time.sleep(5)
            print('Het schudden blijft doorgaan en jullie blijven maar rennen. \nVoor jullie valt ook een steen en jullie zijn helemaal ingesloten.')
            time.sleep(5)
            print('Als laatste zie je de fakkel van Tibaltus uit zijn handen vallen en dofen, \nvoor het allemaal zwart wordt voor je ogen.')
            time.sleep(5)
        elif keuze2 == 'links':
            print('Je gaat links. Na een lange toch van zeker 15 minuten zie je een deur aan het einde van de gang. \nOp de deur staat: Een ieder die zich hier betreed, zal het niet lang overleven.  ')
            time.sleep(5)
            print('Tibaltus: Zou dit de deur naar de Draak zijn?  ')
            time.sleep(5)
            print('Jij: Ik weet het niet, moeten we naar binnen gaan?  ')
            time.sleep(5)
            print('Ga je de deur door? Y/N ')
            time.sleep(5)
            keuze3 = input('[Y,N]')
            if keuze3 == 'y':
                print('Je gaat de deur door en stapt in een grote ruimte met licht wat door het gat van boven komt. \nHet licht valt in stralen naar beneden, op de draak die daar licht te slapen. \nDe draak ligt helemaal stil, en je ziet stoom uit de neus van de draak komen met elke uitademing.')
                time.sleep(5)
                print('Je kijkt naar Tibaltus die met een wit gezicht terugkijkt. \nGeen enkel verhaal had jullie kunnen voorbereiden op hoe groot en angstaanjagend de draak is. \nTerwijl je naar de draak toe loopt, pak je jouw schild van je rug en wil je jouw zwaard uit de schede trekken.')
                time.sleep(5)
                print('Dit maakt echter een geluid en je stopt met bewegen. Je kijkt of de draak iets heeft gehoord. \nDe draak opent zijn ogen en je ziet dat hij boos wordt en op wil staan. \nJe seint naar Tibaltus dat het nu de tijd is om aan te vallen.  ')
                time.sleep(5)
                print('Schreeuwend rennen jullie naar de draak, die nog niet overeind is.  ')
                time.sleep(5)
                print('Waar ren je naar toe? ')
                time.sleep(5)
                keuze4 = input('[hoofd,vleugel]')
                if keuze4 == hoofd:
                    print('Je rent naar het hoofd van de draak, die nog aan de grond is. \nJe pakt hem bij een van de oren vast terwijl de draak zijn hoofd hoog in de lucht houdt. \nAls je van deze hoogte zou vallen, zou je het zeker niet overleven.')
                    time.sleep(5)
                    print('Je herpakt je balans en kijkt naar je zwaard die prachtig schijnt in de zonnestralen. \nJe steekt je zwaard precies in het oog van de draak.')
                    time.sleep(5)
                    print('Die uit pijn hard schreeuwt en net slotte dood neervalt. \nJe hebt het gedaan, de draak is dood en jij en Tibaltus keren terug naar de stad waar jullie worden onthaald als helden.')
                    time.sleep(5)
                    print('In de stad eten jullie veel taart en drinken jullie ontzettend veel bier.')
                elif keuze4 == vleugel:
                    print('Terwijl je naar de vleugel rent, ziet de draak je rennen, hij heft zijn vleugel wat zo veel wind creeerd dat je omver wordt geblazen. \nJe zien Tibaltus nog naar je toe rennen terwijl de Draak zijn mond opend om vuur te spuwen. \nJe harnas smelt om je heen terwijl je levend verbrand. ')
                else:
                    print('Je gaat door de deur terug, fuck this shit im out. \nTibaltus gaat dood door de draak en je wordt onthoofd omdat je te laf was om je taak te voltooien. ')
            else:
                print('Je gaat terug naar de splitsing ')
        elif keuze2 == 'rechts':
            print('Je gaat naar rechts. Na een lange toch van zeker 15 minuten zie je een deur aan het einde van de gang. \nOp de deur staat: Een ieder die zich hier betreedt, zal het niet lang overleven. ')
            time.sleep(5)
            print('Tibaltus: Zou dit de deur naar de Draak zijn?  ')
            time.sleep(5)
            print('Jij: Ik weet het niet, moeten we naar binnen gaan?')
            time.sleep(5)
            print('Ga je door de deur?')
            time.sleep(5)
            keuze5 = input('[Y,N]')
            if keuze5 == 'y':
                print('Als je de deur door bent, valt deze achter jullie op slot.  ')
                time.sleep(5)
                print('Er zitten gaten in de muren waardoor plotseling allemaal slangen komen. \nOok uit de gaten in het plafond vallen. Ondanks de beten proberen jullie door te rennen.')
                time.sleep(5)
                print('Tevergeefs... Het gif spreid snel en al snel worden jullie beiden verlamd. \nJe licht verlamd op de grond en kijkt naar boven, zo lig je nog wel even, tot alles zwart wordt. ')
            else:
                print('Je gaat terug naar de splitsing ')
        else:
            print('Je gaat terug naar de uitgang. wil je naar je stad, typ Y')
            keuze6 = input()
            if keuze6 == 'y':
                print('Je gaat terug naar de stad. Je wordt onthoofd omdat je te laf was om je taak te voltooien.')
            
#als de user dood gaat. Wordt deze functie geroepen.
def death(): 
    print('Je bent dood. Opnieuw proberen? ')
    retry = input('Y/N ')
    if retry == 'Y':
        adventure()
    else:
        return

#als de user wint. Wordt deze functie geroepen.
def victory(): 
    print('Je hebt gewonnen! Nog een keer? ')
    retry = input('Y/N ')
    if retry == 'Y':
        adventure()
    else:
        return
