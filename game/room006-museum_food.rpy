# todo: food exihibit conversation bg #190

# todo: food main exhibit painting #226

image bg museum_food_top:
    "map-bgs/museum_food_top.png"
    zoom 1.15
    yalign 0.2

image badpainting:
    "items/badpainting.jpg"
    zoom 0.1
    yalign 0.5

image painting_food_floor:
    "items/Brussel_Sprouts.png"
    xalign 0.5
    yalign 1.0
    zoom 0.75

image painting_food:
    "items/Brussel_Sprouts.png"
    truecenter
    zoom 0.75

image eating:
    "items/personeatingfoodpainting.png"
    truecenter
    zoom 1.75

label museum_food:
    scene bg museum_food_top
    show posty neutral

    p "_" # todo: food exhibit imagemap #224

    menu:
        "Ripped Mitten & Unappetizing painting" if (quest.painting_food == False):
            jump .painting
        "Ripped Mitten" if quest.painting_food:
            jump .rm
        "Notepad":
            jump .notepad
        "Marble Bust":
            jump .marble
        "Corndog painting" if (food_switch == False):
            jump .corndog
        "Hidden passageway" if food_switch:
            jump janitors
        "Eating painting":
            jump .eating
        "Go back to the entrance.":
            jump museum_entrance

label .marble:
    scene bg museum_food
    show marble
    if quest.money_food:
        jump .marble3
    elif saw.marble:
        jump .marble2
    else:
        jump .marble1

    show posty neutral
    $ saw.marble = True
    
    label .marble1: #248
    show posty neutral
    $ saw.marble = True
    marble "As an art critic and collector, I am severely disappointed with these so-called \"artworks\"! Everything here is so bland."
    p suspicious "..Okaay?"
    if item.napkin:
        jump .marble_napkin
    else:
        marble "You clearly don't understand true art! Leave at once while I search for {b}the ultimate work of art{/b}!"
        jump museum_food

label .marble2: #248
    show posty neutral
    if item.napkin:
        jump .marble_napkin
    else:
        marble "Did you not hear me? Get out! I am trying to find {b}the ultimate work of art{/b}!"
    jump museum_food

label .marble_napkin: 
    marble "Hold on. What is that you're holding?"
    p "This?"
    show badpainting
    marble "Why... This is the greatest artwork I have ever seen! I simply must have it for my collection!! I will pay handsomely!"
    p suspicious "{i}really??{/i}"
    p happy "hmm.. oh I'm not sure! I don't want to give away this wonderful piece of art, but alright!"
    "You handed over the {b}priceless, one-of-a-kind highbrow painting{/b}!"
    $ item.napkin = False
    hide badpainting
    $ money += 2
    $ quest.money_food = True
    show cash_bundle_2 at truecenter
    $ renpy.transition(irisout, layer="master") #prevents interruption of the text window
    "{b}{color=#bdbb9a}Marble Bust{/color}{/b} gave you {b}some money{/b}!"
    hide cash_bundle_2
    call money_get
    p "Farewell!"
    jump museum_food

label .marble3: #251
    show posty neutral
    marble "Thank you for this masterpiece!"
    jump museum_food

label .notepad:
    scene bg museum_food
    show notepad
    if gave_chips:
        jump .notepad3
    elif saw.notepad:
        jump .notepad2
    else:
        jump .notepad1

label .notepad1: #244
    show posty concerned
    $ saw.notepad = True
    p "Oh my, are you alright?"
    notepad "Can't you tell?! I am rock bottom here."
    notepad "I have turned my whole damn life upside down for the chance of exhibitions and I can't even find a bite to eat!!"
    notepad "Many times I pleaded and begged the curators to buy my life's work, many times they rejected me..."
    p sad "Damn that sucks."
    notepad "Not even half of it: I even reduced my prices all the way down to $2 for everything I ever made."
    notepad "You know what they said? No!"
    notepad "I am at my wits end: starving in the middle of the food exhibit."
    notepad "I should've stayed back home, then I wouldn't have ended up here."
    notepad "Time after time I put so much heart into this, only to be thrown out like a stray cup."
    notepad "I don't know why I bother."
    if item.chips:
        jump .notepad_chips
    else:
        p "_" # posty apologizes, not having any food for them.
        notepad "_" # notepad tells her to let them know if they find any for them
        jump museum_food

label .notepad2: #244
    show posty neutral
    notepad "_" # notepad asks posty if she has any food for them now.
    if item.chips:
        jump .notepad_chips
    else:
        p "_" # posty apologizes, as she still doesn't.
        notepad "_" # notepad reminds her to let them know if they find any for them
        jump museum_food

label .notepad_chips: #246
        p concerned "You want a snack?"
        notepad "What?"
        p "I got a bunch of chips if you wan-"
        notepad "OOOHH PLEASE GIVE IT TO ME THANK YOU SO MUCH!!!"
        p "You need it more than I do, you gone crazy."
        show generichips at truecenter
        "You handed over the {b}Generi-Chips{/b}!"
        $ item.chips = False
        $ gave_chips = True
        hide generichips
        notepad "My god this tastes soooo amazing."
        notepad "First meal in a week, you are my shining saviour."
        p happy "Glad to be of help!"
        notepad "For assisting me in my direst hour, you shall have my greatest work."
        notepad "It distills my essence into a small package you can carry around as a reminder."
        p astonished "Aw shucks, that is too much!"
        show badpainting
        "You got the {b}napkin \"painting\"{/b}! : if this was in the eye of the beholder, then they would be blind." #245 describe napkin painting
        $ item.napkin = True
        hide badpainting
        p confused "Oohhheheh it looks... avant garde."
        notepad "This is for feeding me, only the best!"
        p happy "Hehe no biggie!"
        p suspicious "(Did they pick up some trash to fool me? Why would anyone even consider this?)"
        p neutral "(Eh whatever, I guess I'll find a rubbish bin to properly dispose it in later)"
        p concerned "Ahahaha ohh I am soo sorry, I have a meeting in 30 minutes!"
        p concerned "I can't hang around any longer sadly..."
        notepad "It is a shame I can't see your enjoyment for any longer."
        p happy "See you around I guess!"
        jump museum_food
label .notepad3: #247
    show posty neutral
    notepad "_" # revisiting notepad
    jump museum_food

label .painting: #228
    scene bg museum_food
    show painting_food_floor
    show posty neutral
    show rm
    p "_" # posty arrives, having felt drawn to this painting inexplicably
    rm "_" # Ripped Mitten says a veiled complaint about the painting, like it doesn't belong here, and how nobody would miss it. then they leave.
    hide rm with moveoutright
    p "_" # posty beholds the main painting in the food exhibit and feels a compulsion to collect it.
    hide painting_food_floor
    show painting_food
    "You got an {b}art piece{/b}!" #227 describe food painting
    $ item.painting_food = True
    $ quest.painting_food = True
    $ paintings += 1
    hide painting_food
    if paintings == 1:
        p "this was the first painting (replace this text)" # posty says something and decides to look around the rest of the exhibit
    else:
        p "that was easy (replace this text)" # posty remarks that it was easy to take this painting, if this isn't her first painting.
    jump museum_food

label .rm:
    scene bg museum_food
    show posty neutral
    show rm
    rm "_" #230 speaking to ripped mitten a second time, briefly
    jump museum_food

label .corndog:
    scene bg museum_food
    show corndog
    show posty neutral
    p "_" #231 posty observes the corndog painting. it doesnt really call out to her, but it sure is huge. it doesn't seem to be supported by anything, just leaning on the wall. posty decides to look at the other paintings.
    jump museum_food

label .eating: #233
    scene bg museum_food
    show eating
    show posty neutral
    if food_switch == False:
        p "_" # posty observes that the painting doesn't really belong here. these are paintings of food, not paintings of eating. she takes a look at the painting's placard, curious why it was included.
        "The title of the painting is \"{i}Crisis of the Poplar Trees{/i}\". The rest of the text is too small to read at this distance." 
        p "_" # posty remarks that that's hardly a fitting name for this painting either, and it sure as hell isnt fitting for a painting in the food exhibit.
        label .eating_decide:
        menu:
            "Read more of the placard?"

            "Yes.":
                "You try to read more of the placard, but bonk your face on it by mistake!"
                # play a sound here! like a click!!!
                # and then a scene of the corndog painting disappearing, revealing the secret passageway.
                $ food_switch = True
                p "_" # something like "well that was weird. better back off"
                jump museum_food
            "No.":
                p "_" # posty decides she is uninterested in reading more of the placard. she starts to walk away, but returns to the placard, still curious.
                jump .eating_decide
    else:
        p "_" # posty returns to actually read the placard this time.
        "The placard reads: \"{i}(something){/i}\". Weird!" # placard full text.
        p "_" # some kind of remark
        jump museum_food

