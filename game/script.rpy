# Characters
define k = Character("Kiyoshi", image="kiyo",
                     who_color="#9be394")
define n = Character("Nico", image="nico",
                     who_color="#f09b5b")
define t = Character("Tohiro", image="tohi",
                     who_color="#5badf0")
define ko = Character("Kosomos", image="kos",
                     who_color="#f59153")

# Posistions/Transistions
transform charright:
       xalign 0.76
       yalign 0.65
transform charleft:
       xalign 0.24
       yalign 0.65
transform charmid:
       xalign 0.5
       yalign 0.65
define sceneswitch = Dissolve(.5)
define wipeinward = ImageDissolve("gradient reverse.png", 1.0, ramplen=128)
define wipedissolve = ImageDissolve("gradient.png", 1.0, ramplen=128)
define wipeweird = ImageDissolve("weird.png", 2.5, ramplen=250)
define wipeslide = ImageDissolve("swipe.png", 1.0, ramplen=128)


# The game starts here.

label start:

    scene bg foyer
    with wipedissolve

    show nico wet at charleft with moveinright

    # idk the game starts here now...

    "Nico quickly hustled into his house as he was doused by the entourage of rain coming from the outside. He sighed as he look downed at his completely soaked school outfit and started to get some of the clothes off."
    n "The news said nothing about the rain, just my luck..."
    show tohi wet at charright with moveinright
    "A male much taller than Nico sprinted in after, making sure to take his shoes off and put his bag down in front of the doorway" 
    t "Thanks again- for having me over" 
    "Tohiro Shigata, the man behind Nico, had a big grin on his face and took off his drenched school coat, now being able to see through the white button up shirt he had been wearing under"
    "A male much taller than Nico sprinted in after, making sure to take his shoes off and put his bag down in front of the doorway"
    t "Thanks again- for having me over"
    n "I-It's no problem, didn't w-want you to get even more wet than you already a-are."
    t "I’m glad your house is closer than mine, I haven’t had time to tidy my room"
    n "Y-Yeah... I-I'm gonna t-take a s-shower{p=0.7}or would you like to?"
    t "Oh, I don't mind being last.\nUnless you wanna take one together?"
    n "T-T-Togther!"
    t "Yeah! It'll be like a bath house! I'll even wash your back if you want~."
    n "b-b-b-b-"
    scene bg yaoi
    with wipedissolve
    #Wipe to hot yaoi doujin looking scene
    "Not Too Hard, Tohi~"
    scene bg foyer
    show nico nosebleed at charleft
    show tohi wet at charright
    t "Ah! Are you ok? Here!"
    "Tohiro quickly grabs a box of tissues and wipes away the blood."
    t "Where are the baths!"
    n "D-D-Down the hall, second d-door on the right!"


    # prototype end

    return
