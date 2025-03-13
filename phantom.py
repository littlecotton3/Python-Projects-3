# PHANTOM: Prologue
# Para and choices 1
print("You awaken abruptly, your eyes opening to a familiar yet unsettling sight—the walls of your bedroom, shrouded in darkness. A thick, irregular silence blankets the room, making the air feel unmoving. The only sound is your own breath, slow and deliberate, as if your body itself is hesitant to move.")
print("Your gaze shifts to the window.")
print("There is no light.")
print("No soft glow of the sun creeping through the curtains—just an abyss of endless black stretching beyond the glass.")
print("                                            ")
print("   1) Move towards the window")
print("   2) Check alarm clock")
print("   3) Stay still in bed")
print("                                            ")
# Input of numbers
num1 = int(input("Choose a number (1-3) "))
while num1 < 1 or num1 > 3:
  print("Invalid")
  num1 = int(input("Choose a number (1-3) "))
print("                                            ")
# IF 3
if num1 == 3:
  print("The world you know outside the window doesn’t exist. But you don’t get up. You don’t move. You don’t want to see. You just listen.")
  print("Listen...")
  print("Can you hear it?")
  print("                                          ")
  print("   1) Close your eyes")
  print("   2) Look in the doorway")
  print("                                          ")
  # Input of numbers
  num2 = int(input("Choose a number (1-2) "))
  print("                                          ")
  while num2 < 1 or num2 > 2:
    print("Invalid")
    num2 = int(input("Choose a number (1-2) "))
  # IF 3 and then 1
  if num2 == 1:
    print("Maybe if you don’t look, it won’t be real. You squeeze your eyes shut.")
    print("You just need to wake up.")
    print("The air shifts. A step. It’s inside the room.")
    print("Wake up.")
    print("You don’t see it, but it sees you.")
    print("Wake up.")
    print("Only…")
    print("you’re already awake.")
    print("                                        ")
    print("                      GAME OVER          ")
    print("   ENDING 1/3 - The darkness claimed you, and the phantom consumed you.")
  # IF 3 and then 2
  if num2 == 2:
    print("A figure, tall and wrong, hides behind the open door peering at you.")
    print("No features. No face.")
    print("Just a dark entity feeding off your soul.")
    print("“Hello…friend.”")
    print("Its voice scrapes against your mind, a sound that doesn’t belong here.")
    print("The door creaks open. You blink and the entity’s blank face hovers above you, staring.")
    print("It was waiting for you.")
    print("                                        ")
    print("                      GAME OVER          ")
    print("   ENDING 1/3 - The darkness claimed you, and the phantom consumed you.")
# IF 1
if num1 == 1:
  print("Something feels… off.") 
  print("Pushing back the covers, you climb out of the bed, the floor beneath you cold and uncomforting. You step cautiously toward the window, drawn by the unnatural void on the other side of it. Your hands part the delicate curtains.")
  print("Blackness.")
  print("A darkness so absolute, swallowing everything. No streetlights. No movement. No people.")
# IF 2
if num1 == 2:
  print("A gnawing unease curls in your gut, turning toward the alarm clock on your bedside table. The red digits glare back at you: ~11:00 AM~. You glance back at the window, then back at the clock.")
  print("11am?")
  print("Where is the sun?")
  print("Something feels… off.")
  print("Pushing back the covers, you climb out of the bed, the floor beneath you cold and uncomforting. You step cautiously toward the window, drawn by the unnatural void on the other side of it. Your hands part the delicate curtains.") 
  print("Blackness.") 
  print("A darkness so absolute, swallowing everything. No streetlights. No movement. No people.")
# continuing from "No people..."
if num1 == 1 or num1 == 2:
  print("No people...")
  print("                                          ")
  print("   1) Look closely")
  print("   2) Close curtains")
  print("                                          ")
  num1 = int(input("Choose a number (1-2) "))
  while num1 < 1 or num1 > 2:
    print("Invalid")
    num1 = int(input("Choose a number (1-2) "))
  print("                                          ")
  # IF 2
  if num1 == 2:
    print("You release the curtains, letting them shut. This has to be some sort of lucid dream, a hallucination.")
    print("Exhaustion plays tricks on the mind… right?")
    print("So you make your way back into bed, into the comfort and warmth of your covers. Safety.")
    print("                                        ")
    print("   1) Close your eyes")
    print("   2) Lay awake in bed")
    print("                                        ")
    # Input of numbers
    num = int(input("Choose a number (1-2) "))
    while num < 1 or num > 2:
      print("Invalid")
      num = int(input("Choose a number (1-2) "))
    print("                                        ")
    # IF 2 and then 1
    if num == 1:
      print("Just wake up from this nightmare and you’ll be okay. You squeeze your eyes shut.")
      print("The air shifts. A step. It’s inside the room.")
      print("Wake up.")
      print("You don’t see it, but it sees you.")
      print("Wake up.")
      print("Only…")
      print("you’re already awake.")
      print("“I see you…”")
      print("                      GAME OVER          ")
      print("   ENDING 1/3 - The darkness claimed you, and the phantom consumed you.")
    # IF 2 and then 2
    if num == 2:
      print("Don’t close your eyes. It doesn’t feel safe. ")
      print("Your gaze drifts to the window hiding behind the curtains. After a while, the exhaustion is gone.")
      print("Your mind is clear and sharp. Steadily sitting yourself up, you take in your surroundings after a noticeable change in the atmosphere.")
      print("What happened?")
      print("                      GAME OVER          ")
      print("   ENDING 3/3 - You survived. You live in this world now. You are alone and safe.")
  # IF 1
  if num1 == 1:
    print("One.")
    print("A lone figure stands in the distance.")
    print("A singular streetlight placed next to it begins to flicker, its weak glow casting long, distorted shadows across the pavement. The only source of light on the street.")
    print("It lifts an arm. So slow its motion is unnatural, as if trying to be human.")
    print("The hand extends and begins to wave at you.")
    print("                                        ")
    print("   1) Wave back")
    print("   2) Ignore it and close the curtains")
    print("                                        ")
    # Input of numbers
    num = int(input("Choose a number (1-2) "))
    while num < 1 or num > 2:
      print("Invalid")
      num = int(input("Choose a number (1-2) "))
    # IF 1 and then 2
    print("                                        ")
    if num == 2:
      print("You release the curtains, letting them shut. This has to be some sort of lucid dream, a hallucination.")
      print("Exhaustion plays tricks on the mind… right?")
      print("So you make your way back into bed, into the comfort and warmth of your covers. Safety.")
      print("                                        ")
      print("   1) Close your eyes")
      print("   2) Lay in bed awake")
      print("                                        ")
      num8 = int(input("Choose a number (1-2) "))
      while num8 < 1 or num8 > 2:
        print("Invalid")
        num8 = int(input("Choose a number (1-2) "))
        # IF 1 and then 2 and then 1
        print("                                        ")
        if num8 == 1:
          print("Just wake up from this nightmare and you’ll be okay. You squeeze your eyes shut.")
          print("The air shifts. A step. It’s inside the room.")
          print("Wake up.")
          print("You don’t see it, but it sees you.")
          print("Wake up.")
          print("Only…")
          print("you’re already awake.")
          print("“I see you…”")
          print("                      GAME OVER          ")
          print("   ENDING 1/3 - The darkness claimed you, and the phantom consumed you.")
        # IF 1 and then 2 and then 2
        if num8 == 2:
          print("Don’t close your eyes. It doesn’t feel safe.")
          print("Your gaze drifts to the window hiding behind the curtains. After a while, the exhaustion is gone.")
          print("Your mind is clear and sharp. Steadily sitting yourself up, you take in your surroundings after a noticeable change in the atmosphere.")
          print("What happened?")
          print("                      GAME OVER          ")
          print("   ENDING 3/3 - You survived. You live in this world now. You are alone and safe.")
    # IF 1 and then 1
    if num == 1:
      print("Eventually, you raise your arm and wave back at it. Maybe they can explain what is happening, why the world has gone dark, why the atmosphere is dense with something unseen and suffocating. The figure pauses mid-wave and mechanically places its arm back down to its side.")
      print("You blink– ")
      print("It moved.")
      print("It stands in front of the window, towering over you, its faceless head tilted to the side… ")
      print("No features, just a blank face.")
      print("Without shifting, it lifts a finger and rings the doorbell, watching as you stare into its face. ")
      print("Who is this…? ")
      print("What is this…?")
      print("                                        ")
      print("   1) Go to the door")
      print("   2) Close the curtains")
      print("                                        ")
      # Input of numbers
      num3 = int(input("Choose a number (1-2) "))
      while num3 < 1 or num3 > 2:
        print("Invalid")
        num3 = int(input("Choose a number (1-2) "))
      print("                                        ")
      # IF 1 and then 1 and then 2
      if num3 == 2:
        print("You release the curtains, letting them shut. This has to be some sort of lucid dream, a hallucination.")
        print("Exhaustion plays tricks on the mind… right?")
        print("So you make your way back into bed, into the comfort and warmth of your covers. Safety.")
        print("                                        ")
        print("   1) Close your eyes")
        print("   2) Lay in bed awake")
        print("                                        ")
        # Input of numbers
        num678 = int(input("Choose a number (1-2) "))
        while num678 < 1 or num678 > 2:
          print("Invalid")
          num678 = int(input("Choose a number (1-2) "))
        print("                                        ")
        # IF 1 and then 1 and then 2 and then 1
        if num678 == 1:
          print("Just wake up from this nightmare and you’ll be okay. You squeeze your eyes shut.")
          print("The air shifts. A step. It’s inside the room.")
          print("Wake up.")
          print("You don’t see it, but it sees you.")
          print("Wake up.")
          print("Only…")
          print("you’re already awake.")
          print("“I see you…”")
          print("                      GAME OVER          ")
          print("   ENDING 1/3 - The darkness claimed you, and the phantom consumed you.")
        # IF 1 and then 1 and then 2 and then 2
        if num678 == 2:
          print("Don’t close your eyes. It doesn’t feel safe.")
          print("Your gaze drifts to the window hiding behind the curtains. After a while, the exhaustion is gone.")
          print("Your mind is clear and sharp. Steadily sitting yourself up, you take in your surroundings after a noticeable change in the atmosphere.")
          print("What happened?")
          print("                      GAME OVER          ")
          print("   ENDING 3/3 - You survived. You live in this world now. You are alone and safe.")
      # IF 1 and then 1 and then 1
      if num3 == 1:
        print("Some innate urge in your gut tells you to answer the door.")
        print("This could be important, a final explanation for what is going on.")
        print("Hesitantly you force your eyes away from the mysterious stranger and walk cautiously out of your room, toward the front door. Through the long, narrow window on it,  you can make out the blurred but unwavering image of what looks to be the stranger staring through, still watching your every movement.")
        print("You tread softly forward until you reach the door. The lock–a simple illusion of safety, a fragile symbol you know doesn’t exist at this moment. The only thing separating you from the figure.")
        print("Should we welcome it?")
        print("                                        ")
        print("   1) Unlock the door")
        print("   2) Keep the door locked. Move away from it.")
        print("                                        ")
        # Input of numbers
        num4 = int(input("Choose a number (1-2) "))
        while num4 < 1 or num4 > 2:
          print("Invalid")
          num4 = int(input("Choose a number (1-2) "))
        print("                                        ")
        # Unlocking the door ~ IF 2
        if num4 == 2:
          print("You continue to watch the stranger, legs trembling as you begin moving away from the door.")
          print("How can you trust it? This has to be some sort of lucid dream, a hallucination.")
          print("Exhaustion plays tricks on the mind… right?")
          print("So you make your way back into bed, into the comfort and warmth of your covers. Safety.")
          print("                                        ")
          print("   1) Close your eyes")
          print("   2) Lay in bed awake")
          print("                                        ")
          # Input of numbers
          num345 = int(input("Choose a number (1-2) "))
          while num345 < 1 or num345 > 2:
            print("Invalid")
            num345 = int(input("Choose a number (1-2) "))
          print("                                        ")
          # Unlocking the door ~ IF 2 and then 1
          if num345 == 1:
            print("Just wake up from this nightmare and you’ll be okay. You squeeze your eyes shut.")
            print("The air shifts. A step. It’s inside the room.")
            print("Wake up.")
            print("You don’t see it, but it sees you.")
            print("Wake up.")
            print("Only…")
            print("you’re already awake.")
            print("“I see you…”")
            print("                      GAME OVER          ")
            print("   ENDING 1/3 - The darkness claimed you, and the phantom consumed you.")
          # Unlocking the door ~ IF 2 and then 2
          if num345 == 2:
            print("Don’t close your eyes. It doesn’t feel safe.")
            print("Your gaze drifts to the window hiding behind the curtains. After a while, the exhaustion is gone.")
            print("Your mind is clear and sharp. Steadily sitting yourself up, you take in your surroundings after a noticeable change in the atmosphere.")
            print("What happened?")
            print("                      GAME OVER          ")
            print("   ENDING 3/3 - You survived. You live in this world now. You are alone and safe.")
        # Unlocking the door ~ IF 1
        if num4 == 1:
          print("Your hand moves before your brain gets the chance to stop it.")
          print("Click.")
          print("The door hinges make an uncomfortable creaking noise as it slowly opens. It opens, just enough for the figure to slip its head through.")
          print("You can hear the words as it begins to speak. Where is the voice coming from?")
          print("“Hello… I apologise… for disturbing you…”")
          print("“Who are you?” You question.")
          print("“I’m looking…for someone…”")
          print("“You are kind…to open the door…and welcome me…as a guest…”")
          print("“Sometimes…I have to find…another way in…”")
          print("                                        ")
          print("   1) Can you explain what is happening?")
          print("   2) You didn't answer my question.")
          print("   3) ...")
          print("                                        ")
          # Input of numbers
          num38 = int(input("Choose a number (1-3) "))
          while num38 < 1 or num38 > 3:
            print("Invalid")
            num38 = int(input("Choose a number (1-3) "))
          print("                                        ")  
          # Unlocking the door ~ IF 1 and then 2
          if num38 == 2:
            print("It’s unsettling the way it speaks. There is no time to waste, you just need answers. Answers it’s not giving you.")
            print("You respond firmly, “You didn’t answer my question.”")
            print("Everything pauses. The gentle breeze outside halts and the figure stands still.")
            print("“I don’t like…hostility…”")
            print("                      GAME OVER          ")
            print("   ENDING 1/3 - The darkness claimed you, and the phantom consumed you.")
          # Unlocking the door ~ IF 1 and then 1 or 3
          if num38 == 1 or num38 == 3:
            print("“I enjoy…quiet days…”")
            print("“Days like…this…are my favourite…”")
            print("“I want to show you…something special…”")
            print("“I can make it…quiet for you…like this…always…”")
            print("You stare blankly at the guest, trying to understand what it means.")
            print("“I appreciate…a good listener…”")
            print("“You can be…my shadow…”")
            print("“My friend…heh…”")
            print("“Walk with me…and I will…show you… ”")
            print("The guest holds out a hand.")
            print("“How beautiful…silence can be…”")
            print("                                        ")
            print("   1) I also like quiet days...")
            print("   2) Reject the guest")
            print("                                        ")
            # Input of numbers
            num33 = int(input("Choose a number (1-2) "))
            while num33 < 1 or num33 > 2:
              print("Invalid")
              num33 = int(input("Choose a number (1-2) "))
            print("                                        ")
            # Unlocking the door ~ IF 1 and then 1 or 3 and then 1
            if num33 == 1:
              print("Without another word, you gently grab the figure’s cold hand.")
              print("A strange calm washes over you, the quiet settling deep within your bones.")
              print("You want to see the special thing it spoke of. So you let it guide you through the threshold.")
              print("A wave of relief floods you. You walk side by side across the street, the stranger next to you becoming more familiar with each passing step.")
              print("“My friend…I will show you…”")
              print("                      GAME OVER          ")
              print("   ENDING 2/3 - You walked with the phantom. You became its shadow. You found peace and happiness.")
            # Unlocking the door ~ IF 1 and then 1 or 3 and then 2
            if num33 == 2:
              print("The mere thought of following the entity and leaving your home behind compels you to refuse its offer.")
              print("“I cannot go with you… I will not abandon the only sanctuary I have.”")
              print("The guest stands motionless and withdraws its hand. The silence stretches thin before it begins to say something.")
              print("“I see…you don’t require…my companionship…”")
              print("“Very well…”")
              print("“When your walls fall…and the light dies…I will be waiting…”")
              print("“You can’t hide…from the dark…”")
              print("With that, the guest turns around and leaves. Its movements are jagged, as if struggling to walk toward the shadowed street.")
              print("You close and lock the door, peering through the narrow window to catch a final glimpse of the stranger, before swiftly making your way back to bed, seeking refuge beneath the comfort of your covers.")
              print("Don’t close your eyes. It doesn’t feel safe.")
              print("Your gaze drifts to the window hiding behind the curtains. After a while, your mind is clear and sharp.")
              print("Steadily sitting yourself up, you take in your surroundings after a noticeable change in the atmosphere.")
              print("What happened?")
              print("                      GAME OVER          ")
              print("   ENDING 3/3 - You survived. You live in this world now. You are alone and safe.")