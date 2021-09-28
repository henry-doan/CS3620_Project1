import time

def beginning():
  print ("Welcome space cadet! You might be wondering why a monkey is talking to you. Well I am captain Bubbles and I am your partner to guide you on this journey")
  user_name = input("What should I call you cadet?")
  print("Welcome")
  print(user_name)
  print("sit in tight are about to blast off in")
  print (3)
  time.sleep(1)
  print (2)
  time.sleep(1)
  print (1)
  engine_fire()

def engine_fire():
  print("Looks like it is smooth sail... (BOOM!)")
  print("Oh No! our right engine is on fire")
  print("Here are our options:")
  print("1. Abort the mission and take the escape pods")
  print("2. Try to put the fire out")
  print("3. Floor it!")
  try:
    engine_choice = int(input("What should we do?"))
  except ValueError:
    print("You need to do 1, 2, or 3")
    engine_fire()
  # error handle
  if (engine_choice == 1):
    escape_pods()
  elif (engine_choice == 2):
    fire_extinguisher()
  elif (engine_choice == 3):
    floor_it()
  else:
    # loop back to engine_choice
    engine_fire()

def fire_extinguisher():
  print("You go to the fire extinguisher and get stopped by captain Bubbles.")
  print("Are you crazy ?!? What good would that do ? We can't open the door at this high. He slaps you with a banana. Get a grip!")
  escape_pods()

def escape_pods():
  print("The left engine just went out and the ship is starting to lose power")
  print("Captain Bubbles dragged you in the escape pod and you eject out")
  print("You look outside the escape pod, and see your spaceship ablazed and getting further and further away from you")
  print("As the escape pod slowly descend you get closer to the coast of the drop zone of where you would land if something goes wrong.")
  print("Then you hear a (Boom)!")
  print("Your spaceship expodes, and bits of debris are falling down, one hit the esapce pod off course")
  print("You are spinning uncontrollably")
  print("Captain Bubbles got knock unconscious")
  print("1. Do you open the flaps? or ")
  print("2. Open the parachute?")
  try:
    spin_choice = int(input("What would you choose?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2")
    escape_pods()
  if (spin_choice == 1):
    flaps()
  elif (spin_choice == 2):
    parachute()
  else:
    print("Sorry you need to choose 1 or 2")
    escape_pods()

def floor_it():
  ending(1)

def parachute():
  print("You deploy the parachute and you are still spinning")
  print("So your parachute is tangled and you crashed into the sea")
  print("You open the hatch and see a vast ocean")
  print("1. Do you paddle in a random direction")
  print("2. Wait for help")
  print("3. Help treat and wake up Captain Bubbles")
  try:
    sea_choice = int(input("What would you choose?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2 or 3")
    parachute()
  if (sea_choice == 1):
    paddle()
  elif (sea_choice == 2):
    waiting()
  elif (sea_choice == 3):
    treatment()
  else:
    print("Sorry you need to choose 1 or 2 or 3")
    parachute()

def paddle():
  print("You start to paddle, and ")
  print("You felt a bump on the side of the pod but you don't think too much about it")
  print("You Feel a harder more violent bump and you look on to the sea and see a big fin!")
  print("It's a shark and it smells your fear!")
  print("Do you:")
  print("1. Throw down into the sea your emergency rations or")
  print("2. Improvise")
  try:
    shark_choice = int(input("What would you choose?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2")
    paddle()
  if (shark_choice == 1):
    no_food()
  elif (shark_choice == 2):
    improvise()
  else:
    print("Sorry you need to choose 1 or 2")
    paddle()

def no_food():
  print("You quickly threw your emergency ration into the sea")
  print("The shark thrashes and goes for the food as you quickly paddle away from the shark")
  print("You paddle into the sunset")
  island("spacesuit")

def improvise():
  print("You quickly took off your space suit and Captain Bubbles space suit and fill it with sea water and threw it into the ocean")
  print("The shark thrashes and goes for the dummies you made as you quickly paddle away from the shark")
  print("You paddle into the sunset")
  island("food")

def waiting():
  print("You stayed and start to doze off")
  print("You end off falling asleep and days turned into night")
  print("You suddenly woke up in the middle of the night and you can see the peak of morning comming up")
  print("You see all the stars and constellations and point out the north star")
  print("You recall in your studies that there are some islands to the west that is close to where you launch")
  print("You start to head west as morning and noon comes")
  paddle()

def treatment():
  print("You patched up Captain Bubbles and put a band-aid on his head")
  print("He is still out cold and he need some rest")
  print("You decide to paddle next")
  paddle()

def flaps():
  print("You keep spinning and spining and reached for the button to deploy the flaps, but it's a reach from your fingertips")
  print("Inch by inch, you slowly get closer and closer to the button")
  print("With one final stretch you finally pressed the button")
  print("You managed to stablize the pod and stop it from spinning, then you deploy the parachute and slowly decend")
  island("All Supplies")

def island(supplies):
  print("The sun is setting, and you manage land onto a island")
  print("You then step foot on the island and Captain Bubbles is awake but seems to have amnesia")
  print("Looks like you are the next in command, what do you do? You can only do one and it would be dark soon")
  
  if (supplies == "food"):
    print("Looks like you have some food left and it is getting dark soon")
    print("We need to get other things going if we were to survive the night")
    print("Too bad you don't have a space suit so you don't have to look for a shelter")
    print("But you used it to distract the shark")
    print("1. Would you look for supplies and make a shelter?")
    print("2. Look for water?")
    try:
      next_choice = int(input("What would you choose?"))
    except ValueError:
      print("you need to do 1 or 2")
      island("food")
    if (next_choice == 1):
      shelter()
    elif (next_choice == 2):
      water()
    else: 
      island("food")
  elif (supplies == "spacesuit"):
    print("We need to get other things going if we were to survive the night")
    print("You used all the food to distract the shark but now you don't have food")
    print("You do have your spacesuit and it can be used to survive extreme weather so it would be a good shelter")
    print("1. Would you look for food?")
    print("2. Look for water?")
    try:
      next_choice = int(input("What would you choose?"))
    except ValueError:
      print("You need to do 1 or 2")
      island("spacesuit")
    if (next_choice == 1):
      food()
    elif (next_choice == 2):
      water()
    else: 
      island("spacesuit")
  else:
    print("Looks like you have both some food and a spacesuit so your only thing to take care of is water")
    print("We need to get other things going if we were to survive the night")
    water()

def water():
  print("Looks like you are going to look for water")
  print("You have some options for you for water")
  print("1. Would you drink Sea water")
  print("2. Or look up the tree for some fruits")
  try:
    water_choice = int(input("What would you choose?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2")
    water()
  if (water_choice == 1):
    sea_water()
  elif (water_choice == 2):
    coconuts()
  else: 
    print("Sorry you need to choose 1 or 2")
    water()

def sea_water():
  print("You are surrounded by the ocean")
  print("But it is all sea water")
  print("1. Do you and Captain Bubbles drink the sea water straight up?")
  print("2. Use the sea water and boil it down for fresh water but it will take a while")
  try:
    water_choice = int(input("What would you choose?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2")
    sea_water()
  if (water_choice == 1):
    print("You and Captain Bubbles drank the sea water")
    print("It was really salty but you are really thirsty")
    print("All the sudden you remember that sea water drys you out faster")
    ending(0)
  elif (water_choice == 2):
    fresh_water()
  else: 
    print("Sorry you need to choose 1 or 2")
    sea_water()

def fresh_water():
  print("You end up riging stuff from the escape pod and made a desalination machine")
  print("Where you feed the machine sea water and you produce a fire under it to evaporate the water into a collection bowl")
  print("It has been hours and night comes and you notice how much water you produce")
  print("It bare is over 1 liter of fresh water but it would have to do for now")
  print("You split it into the two cups, one for you and one for Captain Bubbles and you cheers and went to bed")
  island_morning()

def coconuts():
  print("You and Captain Bubbles end of climbing a tree and found some coconuts")
  print("You crack one open and its full of coconut water and fruit")
  print("You gather a lot to last you a while")
  island_morning()

def food():
  print("You are starving and you need to get food in you soon")
  print("1. Do you dig for crabs and shell fish")
  print("2. Try your hand in fishing")
  print("3. Climb some trees")
  try:
    food_choice = int(input("What would you choose?"))
  except ValueError:
    print("You need 1, 2, or 3")
    food()
  if (food_choice == 1):
    ending(6)
  elif (food_choice == 2):
    print("You try your hand into some fishing")
    print("You spend hours trying to fish with no luck")
    print("You decide to do something else")
    water()
  elif (food_choice == 3):
    coconuts()
  else: 
    food()

def shelter():
  print("You decide to build a shelter, and looking at your options and what is left of the ship")
  print("What should you do for your shelter?")
  print("1. Use part of the pod to build a sand pit")
  print("2. Use part of the pod and some wood from trees to make a A frame")
  print("3. Go inland to see if there is something in the jungle")
  try:
    shelter_choice = int(input("What would you do?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2 or 3")
    shelter()
  if (shelter_choice == 1):
    ending(2)
  elif (shelter_choice == 2):
    storm()
  elif (shelter_choice == 3):
    cave()
  else:
    print("Sorry you need to choose 1 or 2 or 3")
    shelter()

def storm():
  print("You assembled some trees and part of the escape pod to make a makeshift A-frame and settled in for the night.")
  print("Suddenly a huge thunderstorm came in and your shelter is not holding up, ")
  print("and eventually the shelter broke into pieces and one of the pieces has been blown into the sea and you notice that Captain Bubbles is hanging on to it.") 
  print("It manages to land in the ocean but the waves are carrying them further and further away,") 
  print("you jumped into the water and swam to get Captain Bubbles and pull him back to shore,") 
  print("The storm has passed and the sun is out again.")
  ending(3)

def island_morning():
  print("It is morning and you live to tell the tale")
  print("Your water supply is slowly but surely keep you not dehydrated")
  print("You see a incomming storm comming for you fast")
  shelter()

def cave():
  print("You run into the jungle and found a cave")
  print("A storm approaches and you and Captain Bubbles take shelter in the cave")
  print("It's cold and dark but it least you got out of the storm")
  print("The storm outside is raging, but you are dry and shelter by the wind")
  print("The storm eventually passes and you slowly fall sleep...")
  print("You eventually wake up cold")
  print("1. Do you build a fire to get warm")
  print("2. Sleep through it ")
  try:
    cave_choice = int(input("What would you do?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2")
    cave()
  if (cave_choice == 1):
    fire()
  elif (cave_choice == 2):
    ending(3)
  else:
    print("Sorry you need to choose 1 or 2")
    cave()

def fire():
  print("You build a fire and it keeps you and Captain Bubbles warm")
  print("It also scares away all the cave creatures and insects out the cave")
  print("You also think this would be perfect for some smores but then quickly realize you are stuck in a dark cave with a monkey")
  print("You manage to fall asleep and morning comes")
  plane()

def plane():
  print("You wake up to a loud sound")
  print("You get out of the cave and see in the distance a plane")
  print("It is too far and seems like it hasn't notice you")
  print("1. Do you build a giant bond fire")
  print("2. Write SOS in the sand")
  print("3. Wave your hands back and forth")
  try:
    plane_choice = int(input("What would you do?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2 or 3")
    plane()
  if (plane_choice == 1):
    ending(4)
  elif (plane_choice == 2):
    print("Your SOS washed away in the sand")
    ending(5)
  elif (plane_choice == 3):
    ending(5)
  else:
    print("Sorry you need to choose 1 or 2 or 3")
    plane()

def ending(ending_index):
  endings = open('endings.txt', 'r')
  lines = endings.readlines()
  print(lines[ending_index])
  if (ending_index == 1):
    beginning()
  elif (ending_index == 4):
    print("You chose the correct choices and manage to beat the game")
  else:
    print("Looks like you and Captain Bubbles are in trouble")
  print("1. Would you like to play again to see if you can make better choices")
  print("2. Quit")
  try:
    end_choice = int(input("What would you choose?"))
  except ValueError:
    print("Sorry you need to choose 1 or 2")
    ending(ending_index)
  if (end_choice == 1):
    beginning()
  elif (end_choice == 2):
    exit()
  else:
    print("Sorry you need to choose 1 or 2")
    ending(ending_index)

beginning()
