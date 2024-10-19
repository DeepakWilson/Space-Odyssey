# Define characters
define s = Character("Neil", color="#42aaff")
define n = Character("Narrator", color="#ffffff")

# Music
play music"ringtone.mp3"

# Images
image bg milkyway = im.Scale("bg milkyway.webp", 1920, 1080)
image bg solar_system = im.Scale("solar_system_overview.webp", 1920, 1080)
image bg mars = im.Scale("mars.jpg", 1920, 1080)
image bg jupiter = im.Scale("jupiter.webp", 1920, 1080)
image bg saturn = im.Scale("saturn.webp", 1920, 1080)
image bg earth = im.Scale("earth.jpg", 1920, 1080)
image bg venus = im.Scale("venus.jpg", 1920, 1080)
image bg neptune = im.Scale("neptune.jpg", 1920, 1080)
image bg uranus = im.Scale("uranus.jpg", 1920, 1080)
image bg mercury = im.Scale("mercury.jpg", 1920, 1080)
image bg quiz = im.Scale("quiz_background.jpg", 1920, 1080)
image bg background2 = im.Scale("onmars.jpg",1920,1080)
image bg aster = im.Scale("asteroid field.jpg",1920,1080)

image Neil = im.Scale("Neil.png", 500, 500)
image Neil1 = im.Scale("neil1.png", 500, 500)
image Neil2 = im.Scale("neil2.png", 500, 500)
image Neil3 = im.Scale("neil3.png", 500, 500)
image circle = im.Scale("stone1.png",200,200)
image triangle = im.Scale("stone2.png",200,200) 
image square = im.Scale("stone3.png",200,200)
image drop_box = im.Scale("dropbox.png",300,300)

init python:
    store.draggable = None
    store.droppable = None

    store.dropped_items = {
        "circle": False,
        "triangle": False,
        "square": False
    }

    def drag_placed(drags, drop):
        if not drop:
            return

        # Record which item was dragged and which drop area it was placed in
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        # Check if the item is successfully placed into the drop box
        if drop.drag_name == "drop_box":
            # Mark the draggable item as dropped
            if store.draggable in store.dropped_items:
                store.dropped_items[store.draggable] = True

        return True

    def all_items_dropped():
        return all(store.dropped_items.values())



# Start of the game
label splashscreen:
    scene black
    with Pause(1)

    show text "{b}TeamX presents{/b}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "{b}{i}Space Odyssey{/i}{/b}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return
label start:
    play music "ringtone.mp3" loop
    scene bg milkyway
    show neil3 at left
    with fade
    
    s "Welcome, young rocket explorer! I'm Neil, your guide through the cosmos."
    s "Are you ready for an adventure?"
    
    menu:
        "Yes, let's go!":
            s "Fantastic! Strap in and let's blast off!"
        "Tell me more first":
            s "We'll explore planets, dodge asteroids, and test your knowledge. It'll be out of this world!"
    
    jump solar_system

label solar_system:
    scene bg solar_system
    show neil1 at left
    with dissolve
    
    s "Behold, our magnificent solar system! Where should we go first?"
    
    menu:
        "Zoom to Mercury":
            jump mercury
        "Visit Venus":
            jump venus
        "Check out Earth":
            jump earth
        "Visit Mars":
            jump mars
        "Explore Jupiter":
            jump jupiter
        "See Saturn's rings":
            jump saturn
        "Unravel Uranus":
            jump uranus
        "Discover Neptune":
            jump neptune
      

label mars:
    scene bg mars
    show neil1 at left
    with dissolve
    
    s "Welcome to Mars, the Red Planet! It's like a giant desert with the largest volcano in the solar system—Olympus Mons!"
    s "If you thought your home was hot, try a summer on Mars. Temperatures can reach up to 20 degrees Celsius, but don't get too comfy; it can drop to -125 degrees at night!"
    s "But that's not all! Mars has vital materials that we need for our journey. Are you ready to collect some Martian resources?"
    menu:
        "Yes, let's collect resources!":
            jump waste_game
        "Not right now, let's go back to the solar system.":
            jump return_to_solar_system

label waste_game:
    play music "Game.mp3"
    scene bg background2  # Show the background image

    # Show the initial drag-and-drop screen
    show screen drag_and_drop

    show neil3 at left with moveinleft
    s "Collect the vitals and drop them into the crate"
    hide neil3 with moveinleft

    window hide
    pause
    
    # Wait until all items are dropped
    while not all_items_dropped():
        pause 0.1
        
    # Continue the game after all items are dragged and dropped
    show neil1 at left with moveinleft
    s "Great job! You've dropped all the vitals to the crate"
    hide neil1 with moveinleft

    jump waste_over

screen drag_and_drop:
    # Define draggable items
    draggroup:
        # Circle
        drag:
            drag_name "circle"
            xpos 130
            ypos 700
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            if not store.dropped_items["circle"]:
                child "circle"

        # Triangle
        drag:
            drag_name "triangle"
            xpos 480
            ypos 750
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            if not store.dropped_items["triangle"]:
                child "triangle"

        # Square
        drag:
            drag_name "square"
            xpos 680
            ypos 720
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            if not store.dropped_items["square"]:
                child "square"

        # Define droppable area (trash can)
        drag:
            drag_name "drop_box"
            xpos 1550
            ypos 650
            draggable False
            droppable True
            drag_raise True
            if not all_items_dropped():
                child "drop_box"

label waste_over:
    scene mars with dissolve
    show neil2 at left with moveinleft
    s "You have done well in collecting all the vitals"
    play music "ringtone.mp3"
   
    jump return_to_solar_system


label jupiter:
    scene bg jupiter
    show neil3 at left
    with dissolve
    
    s "This is Jupiter, the king of the planets! It's so big, you could fit all the other planets inside it!"
    s "That Great Red Spot? It's a storm bigger than Earth! Talk about a wild ride!"
    
    jump return_to_solar_system

label saturn:
    scene bg saturn
    show neil2 at left
    with dissolve
    
    s "Look at those rings! Saturn's rings are made mostly of ice and rock. They sparkle like a cosmic disco ball!"
    s "If Saturn were a giant bathtub toy, it would float like a cork. Now that’s some buoyancy!"
    
    jump return_to_solar_system

label earth:
    scene bg earth
    show neil3 at left
    with dissolve
    
    s "Welcome to Earth, our home sweet home! It's the only planet known to support life—how cool is that?"
    s "With diverse climates, amazing oceans, and plenty of creatures, Earth is like a cosmic treasure chest!"
    
    jump return_to_solar_system

label venus:
    scene bg venus
    show neil1 at left
    with dissolve
    
    s "Say hello to Venus, the hottest planet in our solar system! It’s like a giant oven out here, with temperatures reaching 460 degrees Celsius!"
    s "Covered in thick clouds of sulfuric acid, you wouldn’t want to stop for a picnic here!"
    
    jump return_to_solar_system

label neptune:
    scene bg neptune
    show neil2 at left
    with dissolve
    
    s "This is Neptune, the windy giant! Its winds can reach up to 2,100 kilometers per hour—talk about a bad hair day!"
    s "With its deep blue color and mysterious storms, Neptune is the most distant planet in our solar system!"
    jump return_to_solar_system
    

label uranus:
    scene bg uranus
    show neil1 at left
    with dissolve
    
    s "Welcome to Uranus, the planet that spins on its side! It’s like the cosmic equivalent of a tilted ice cream cone."
    s "With its beautiful blue hue, Uranus is a chilly place with an average temperature of -224 degrees Celsius!"
    s "Uh-oh! We need to be cautious as we approach Neptune. Reports say there's an asteroid field in the way!"
    
    menu:
        "Navigate through the asteroid field":
            jump asteroids
        "Continue to Neptune":
            jump Neptune
    
    jump return_to_solar_system

label mercury:
    scene bg mercury
    show neil3 at left
    with dissolve
    
    s "Here we have Mercury, the speedy planet! It zips around the sun in just 88 Earth days!"
    s "With extreme temperatures ranging from -173 to 427 degrees Celsius, it’s a rollercoaster ride of climate!"
    jump return_to_solar_system

label return_to_solar_system:
    s "Where to next, rocket cadet?"
    
    menu:
        "Back to the solar system":
            jump solar_system
        "Let's face the quiz challenge!":
            jump quiz

label asteroids:
    scene bg aster
    show neil1 at left
    with dissolve
    
    s "Oh no! Look out, space explorers! We’re flying into an asteroid field!"
    s "Asteroids are like big, rocky space balls floating around. Some are small, and some are really big!"
    
    s "They zoom around the solar system, and we need to be careful not to bump into them!"
    jump return_to_solar_system 

label quiz:
    play music "lessgoo.mp3"
    scene bg milkyway
    show neil1 at left
    with dissolve
    
    s "Time to test your cosmic knowledge! Ready for a quick quiz?"
    
    $ score = 0
    
    s "Question 1: Which planet is known as the Red Planet?"
    menu:
        "Mars":
            $ score += 1
            s "Correct! Mars is indeed the Red Planet."
        "Jupiter":
            s "Not quite. Mars is the Red Planet, but good try!"
    
    s "Question 2: What are Saturn's rings primarily made of?"
    menu:
        "Gas":
            s "Sorry, that's not right. Saturn's rings aren't made of gas."
        "Ice and rock":
            $ score += 1
            s "Excellent! Saturn's rings are indeed mostly ice and rock."
    
    s "Question 3: Which planet is known for its beautiful rings?"
    menu:
        "Mars":
            s "Oops! Mars is beautiful, but it doesn't have rings."
        "Saturn":
            $ score += 1
            s "You got it! Saturn's rings are a sight to behold!"
    
    s "Question 4: What is the hottest planet in our solar system?"
    menu:
        "Venus":
            $ score += 1
            s "Correct! Venus is a sizzling oven!"
        "Mercury":
            s "Close, but Venus takes the crown for heat!"
    
    s "Question 5: Which planet is famous for its Great Red Spot?"
    menu:
        "Jupiter":
            $ score += 1
            s "Right! That storm has been raging for centuries!"
        "Neptune":
            s "Not quite! Neptune has storms, but Jupiter's is legendary!"
    
    s "Question 6: What is the farthest planet from the sun?"
    menu:
        "Neptune":
            $ score += 1
            s "Correct! Neptune is the furthest from our sun!"
        "Uranus":
            s "Almost! But Neptune is the last stop in our solar system!"
    
    s "You got [score] out of 6 questions correct!"
    
    if score >= 3:
        s "Well done! You're a real rocket genius!"
    else:
        s "Don't worry! Space is complex. Keep exploring and learning!"
    
    s "Thanks for joining me on this cosmic adventure. Until next time, rocket cadet!"
                
return





