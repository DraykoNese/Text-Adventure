#Setting up the player
player = {"Name": {"defaultname"}, "level": 1}
#Creating the inventory (it is empty at first)
inventory = []
currentRoom = 'forest entrance'
#Begin by asking the player for their name
print("Welcome to the game! What is your name?")
player["Name"] = input()
print(f"Hello, {player['Name']}! You begin your adventure at the mouth of a dense forest.")
print("Do you ENTER THE FOREST or TURN BACK?")
answer = input().strip().lower() 
if answer == 'turn back': 
    print("You decide to turn back and head home. Game over.")
    quit() 
elif answer == 'enter the forest':
    print("You step into the forest and trek through the thick undergowth. After a while you come across a lone water well. Do you CHECK INSIDE or CONTINUE WALKING?")
    answer = input().strip().lower()
    if answer == 'check inside':
        currentRoom = 'well' #Save which room the player is in
        print("You peer into the dark hole of the well, and in your effort you accidentally lose balance and fall inside!")
        print("You reach the bottom with a thud. When you gather yourself, you discover a small hole leading down a dark crawl space. Do you enter, YES or NO?")
        answer = input().strip().lower()
        if answer == 'yes': 
            print("You crawl through the hole and find yourself in an underground cavern. A channel of deep water runs through the cavern, downstream you can see a faint light. Do you FOLLOW THE WATER or EXPLORE THE CAVERN?")
            answer = input().strip().lower()
            if answer == 'follow the water':
                print("You follow the water and eventually reach a small underground waterfall. Behind the waterfall, you find a hidden passage that leads to a treasure chamber filled with gold and jewels! You have found the treasure! Congratulations!")
                quit()
            elif answer == 'explore the cavern':
                print("You explore the cavern and find a sleeping dragon! Will you try to SNEAK PAST it or ATTACK it?")
                answer = input().strip().lower()
                if answer == 'attack':
                 print("You attack the dragon, but it wakes up and breathes fire at you. You are burned to ashes. Game over.")
                quit()
            elif answer == 'sneak past':
                print("You successfully sneak past the dragon. Following the cavern, you come across a hidden exit that leads you back to the forest. You have survived the adventure! Congratulations!")
                quit()    
    elif answer == 'continue walking':
        print ("you continue walking. The dense forest seems to go forever. But eventually you come across a small clearing where a run-down hut sits. Do you ENTER THE HUT or CONTINUE WALKING?")
        answer = input().strip().lower()
        if answer == 'enter the hut':
            currentRoom = 'hut' 
        elif answer == 'continue walking':
            print("You continue walking. The forest seems to close around you, and eventually you become lost in the dense undergrowth. You wander for days without food or water, and eventually succumb to the elements. Game over.")
            quit()
            print("You enter the hut and find it abandoned, but there is a chest in the corner. Do you OPEN THE CHEST or LEAVE IT ALONE?")
            answer = input().strip().lower()
            if answer == 'open the chest':
                print("You open the chest and find a magical sword! You take the sword and continue your adventure. You have equipped a powerful weapon!")
                inventory.append('magical sword')
            elif answer == 'leave it alone':
                print("You decide to leave the chest alone and continue your adventure.")
            print ("you step outside the hut. Suddenly, you hear a rustling in the bushes. A wild boar charges at you! Do you FIGHT it or RUN AWAY?")
            answer = input().strip().lower()
            if answer == 'fight':
                if 'magical sword' in inventory: #If the player has the magical sword, they can defeat the boar
                    print("You draw your magical sword and fight the wild boar. With your powerful weapon, you defeat the boar and continue your adventure. You have survived the encounter!")
                    quit()
                else:
                    print("You try to fight the wild boar with your bare hands, but it overpowers you. You are injured and cannot continue. Game over.")
                    quit()
            elif answer == 'run away':
                print("You run away from the wild boar deeper into the forest. After a while it seems to have lost interest in you.")
                print("You continue your adventure and eventually find a hidden path that leads you out of the forest. You have survived the adventure! Congratulations!")
                quit()
            