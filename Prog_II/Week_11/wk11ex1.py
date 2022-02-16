GlowScript 2.8 VPython
#
# game_starter.py
#
# Een interactie met 3D graphics bouwen met Python
#
#Naam: Timo Kosse
#


scene.bind('keydown', keydown_fun)        # Functie voor toetsaanslagen
scene.background = 0.8 * vector(1, 1, 1)  # Lichtgrijs (0.8 van 1.0)
scene.width = 640                         # Maak het 3D-scherm groter
scene.height = 480
scene.camera.pos = vector(0,-5,15)




def make_alien(starting_position, starting_vel=vector(0, 0, 0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vector(0, 0, 0).

       Compounds can have any number of components.  Here are the
       alien's components:
    """
    alien_body = sphere(size=1.0 * vector(1, 1, 1), pos=vector(0, 0, 0), color=color.green)
    alien_eye1 = sphere(size=0.3 * vector(1, 1, 1), pos=.42 * vector(.7, .5, .2), color=color.white)
    alien_eye2 = sphere(size=0.3 * vector(1, 1, 1), pos=.42 * vector(.2, .5, .7), color=color.white)
    alien_hat = cylinder(pos=0.42 * vector(0, .9, -.2), axis=vector(.02, .2, -.02), size=vector(0.2, 0.7, 0.7), color=color.magenta)
    alien_objects = [alien_body, alien_eye1, alien_eye2, alien_hat]  # maak een lijst die we "aan elkaar plakken" met een compound
    # we gaan nu een compound maken -- we noemen hem com_alien:
    com_alien = compound(alien_objects, pos=starting_position)
    com_alien.vel = starting_vel   # stel de beginsnelheid in
    return com_alien


ground = box(size=vector(20, 1, 20), pos=vector(0, -1, 0), color=.4*vector(1, 1, 1))

# We maken twee muren, ook met een box
wall_a = box(pos=vector(0, 0, -10), axis=vector(1, 0, 0), size=vector(20, 1, .2), color=vector(1.0, 0.7, 0.3))  # geel
wall_b = box(pos=vector(-10, 0, 0), axis=vector(0, 0, 1), size=vector(20, 1, .2), color=color.blue)   # blauw
wall_c = box(pos=vector(10, 0, 0), axis=vector(0,0,1), size=vector(20,1,.2), color=color.red) #rood
wall_d = box(pos=vector(0,0,10), axis=vector(1,0,0), size=vector(20,1,.2), color=color.green) #groen

# Een bal die we kunnen besturen
ball = sphere(size=1.0*vector(1, 1, 1), color=vector(0.8, 0.5, 0.0))   # ball is een object van de klasse sphere
ball.vel = vector(0, 0, 0)     # dit is de beginsnelheid

dabox = box(pos=vector(3,0,3), size=vector(2,2,2), color=vector(1,1,1))



rando1 = (random() * 20 -10) #een random x pos tussen de muren
rando2 = (random() * 20 -10) #een random z pos tussen de muren
rando3 = (random() * 3 + 4) #een random x snelheid
rando4 = (random() * 3 + 4) #een random z snelheid
spaceship = cone(pos=vector(rando1,6,rando2), axis=vector(0,radians(90),0), radius=1.5, color=color.red)
spaceship_light = cone(pos=vector(rando1, 0, rando2), axis=vector(0,radians(90),0), size=vector(6,3,3), radius=2, opacity=0.5)
spaceship.vel = vector(rando3, 0 ,rando4)

def alien_create():
    """
    Een functie om een alien te maken
    """
    # We maken twee aliens met twee aanroepen naar de functie make_alien (hierboven)
    rando1 = (random() * 20 -10) #een random x pos tussen de muren
    rando2 = (random() * 20 -10) #een random z pos tussen de muren
    rando3 = (random() * 3 + 4) #een random x snelheid
    rando4 = (random() * 3 + 4) #een random z snelheid
    alien = make_alien(starting_position=vector(rando1, 0, rando2), starting_vel=vector(rando3, 0, rando4))
    return alien

alien = alien_create()#maak de eerste alien voor het spel



# Andere constanten
RATE = 30                # Het aantal keer dat de while-lus per seconde wordt uitgevoerd
dt = 1.0/RATE            # De tijdstap per keer dat de while-lus wordt uitgevoerd
scene.autoscale = False  # Voorkomen dat het beeld automatisch wordt aangepast
scene.forward = vector(0, -3, -2)  # De scene vanuit de lucht wordt bekeken...

#event loop
while True:

    rate(RATE)   # Maximaal aantal keer per seconden dat de while-lus uitgevoerd wordt


    alien.pos = alien.pos + alien.vel*dt   # Werk de positie van de alien bij
    ball.pos = ball.pos + ball.vel*dt      # Werk de positie van de bal bij
    ball.vel = ball.vel * 0.95
    spaceship.pos = spaceship.vel*dt + spaceship.pos
    spaceship_light.pos = spaceship_light.pos + spaceship.vel*dt


    #checken voor botsingen
    arena_collide(ball)
    arena_collide(alien)
    arena_collide(spaceship)
    

    # Geef de alien verticale snelheid als de bal de alien raakt
    if mag(ball.pos - alien.pos) < 1.0:
        print("Je hebt me!")
    
    if mag(ball.pos - spaceship_light.pos) <2.0:
        print("Biep boep, ik ben een ruimteschip")
        
    if mag(ball.pos - dabox.pos) <2.0:
        ball.vel *= -1.0


def keydown_fun(event):
    """This function is called each time a key is pressed."""
    key = event.key
    ri = randint(0, 10)
    print("toets:", key, ri)  # Drukt de ingedrukte toets af
    
    amt = 0.90              # Hoeveel de snelheid per toetsaanslag wordt aangepast
    if key in 'wWiI':
        ball.vel = ball.vel + vector(0, 0, -amt)
    elif key in 'aAjJ':
        ball.vel = ball.vel + vector(-amt, 0, 0)
    elif key in 'sSkK':
        ball.vel = ball.vel + vector(0, 0, amt)
    elif key in "dDlL":
        ball.vel = ball.vel + vector(amt, 0, 0)
    

    elif key in ' rR':
        ball.vel = vector(0, 0, 0)  # Opnieuw beginne! via de spatiebalk, " "
        ball.pos = vector(0, 0, 0)
    







def arena_collide(ball):
    """
    Checkt of object ball een collide triggerd en verandert hierop de vel"""
    # Als de bal wall_a raakt
    if ball.pos.z < wall_a.pos.z:  # Geraakt -- vergelijk de z-positie
        ball.pos.z = wall_a.pos.z  # Zorg dat de bal binnen de grenzen blijft
        ball.vel.z *= -1.0        # Draai de z-snelheid om

    # Als de ball wall_b raakt
    if ball.pos.x < wall_b.pos.x:  # Geraakt -- vergelijk de x-positie
        ball.pos.x = wall_b.pos.x  # Zorg dat de bal binnen de grenzen blijft
        ball.vel.x *= -1.0        # Draai de x-snelheid om
        
    if ball.pos.x > wall_c.pos.x:  # Geraakt -- vergelijk de z-positie
        ball.pos.x = wall_c.pos.x  # Zorg dat de bal binnen de grenzen blijft
        ball.vel.x *= -1.0        # Draai de z-snelheid om

    # Als de ball wall_b raakt
    if ball.pos.z > wall_d.pos.z:  # Geraakt -- vergelijk de x-positie
        ball.pos.z = wall_d.pos.z  # Zorg dat de bal binnen de grenzen blijft
        ball.vel.z *= -1.0        # Draai de x-snelheid om



def choice(L):
    """Implements Python's choice using the random() function."""
    length = len(L)              # Haal de lengte op
    random_index = int(length * random())  # Kies een willekeurige index
    return L[random_index]       # Geef dat element terug


def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low                   # Draai ze om als ze verkeerd om staan!
    length = int(hi) - int(low) + 1.        # Bereken het verschil en voeg 1 toe
    rand_value = length * random() + int(low)  # Kies een willekeurige waarde
    return int(rand_value)                  # Geef het integergedeelte terug


def randcolor():
    """Returns a vector of (r, g, b) random from 0.0 to 1.0."""
    r = random(0.0, 1.0)
    g = random(0.0, 1.0)
    b = random(0.0, 1.0)
    return vector(r, g, b)  # Een kleur is een tuple met drie elementen