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
transform charlefta:
       xalign 0.4
       yalign 0.65
transform charleftb:
       xalign 0.15
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
    show tohi tissue at charlefta with moveinright
    show nico nosebleed at charleftb with moveinright
    "Tohiro quickly grabs a box of tissues and wipes away the blood."
    t "Where are the baths!"
    n "W-Wh-What!"
    t "Where are the baths!"
    n "D-D-Down the hall, second d-door on the right!"
    t "Alright!"
    "Tohrio takes the boy in his arm and carries him to the bathroom."
    scene bg bathroom
    with wipeslide
    show tohi hold at charleft with moveinright
    n "Ugghhh..."
    show nico nosebleed at charleft
    show tohi wet at charmid with moveinleft
    t "There!"
    n "Ugghhhhhh..."
    t "Jeez... You're gonna stain your shirt at this rate."
    "Tohiro buttons off both of their shirts"
    show nico topless
    show tohi topless
    n "H-Hey!"
    scene cg bathroom1
    t "There we go!"
    t "Hey are you sure you are alright?\nYou are loosing alot of blood."
    n "I-I-I'm good, must h-have been the dryness o-of the air."
    t "Would you like me to wash your back?"
    n "MmmHmm"
    scene cg bathroom2
    n "nnngggnnnhh"
    t "Hey, do you mind turning on the water nozzle."
    n "U-U-Uhh Sure!"
    #more naration
    #Nico Fall Asleep
    scene cg bathroom3
    t "Uwahhh! The water is so nice!"
    #More Nico Narration
    t "Hey Nico~."
    n "..."
    t "Nico?"
    n "......"
    t "Nico?"
    n "........."
    #Narration
    t "Dang... Must have been pretty worn out."
    scene bg bathroom
    with wipedissolve
    show tohi sad at charmid
    t "Welp! I can't just leave him here."
    "Tohiro picks up the frail boy and looks down at him."
    show tohi hold
    t "H-He's! Woah! He's a stiff as a board!"
    t "W-Well, he is sleeping after all..."
    t "God... This is so embarassing."






    # prototype end

    return
