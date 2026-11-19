#Setting up the game
player = {"Name": "defaultname", "level": 1}
inventory = []
current_room = "forest entrance"

#Set up player's inputs
def get_choice(prompt):
    return input(prompt).strip().lower()

#GAME OVER message when the player loses or wins
def end_game(message):
    print(message)
    quit()

#Game logic for the different rooms
def enter_cave():
    global current_room
    current_room = "cave"

    answer = get_choice(
        "You reach an underground cavern. "
        "Do you FOLLOW THE WATER or EXPLORE THE CAVERN? "
    )

    if answer == "follow the water":
        end_game(
            "You reach a hidden treasure chamber filled with gold and jewels! "
            "Congratulations!"
        )

    if answer == "explore the cavern":
        answer = get_choice(
            "You find a sleeping dragon! "
            "Do you SNEAK PAST it or ATTACK it? "
        )

        if answer == "sneak past":
            end_game(
                "You sneak past the dragon and find an exit back to the forest. "
                "You survived! Congratulations!"
            )

        if answer == "attack":
            end_game(
                "You attack the dragon, but it breathes fire at you. "
                "You are burned to ashes. Game over."
            )

#Game Logic for choices
def enter_well():
    global current_room
    current_room = "well"

    print(
        "You lose your balance and fall into the well. "
        "A hole leads to a dark crawl space."
    )

    answer = get_choice("Do you enter, YES or NO? ")

    if answer == "yes":
        print("You crawl through the hole.")
        enter_cave()
    elif answer == "no":
        end_game("For some reason, you decided to do nothing but sit in the hole, wallowing in your predicament. Time passes on. And on. Eventually, you succumb to boredom. Game over.")


def enter_hut():
    global current_room
    current_room = "hut"
    print(
        "You enter the hut and find a chest in the corner. "
        "It looks old and dusty."
    )
    answer = get_choice(
        "Do you OPEN THE CHEST or LEAVE IT ALONE? "
    )

    if answer == "open the chest":
        print("You find and equip a magical sword!")
        inventory.append("magical sword")

    answer = get_choice(
        "A wild boar charges at you! "
        "Do you FIGHT or RUN AWAY? "
    )

    if answer == "fight":
        if "magical sword" in inventory:
            end_game(
                "You defeat the wild boar with the magical sword. "
                "You survived! Congratulations!"
            )

        end_game(
            "You fight with your bare hands, but the boar overpowers you. "
            "Game over."
        )

    if answer == "run away":
        end_game(
            "You escape through a hidden path and leave the forest. "
            "You survived! Congratulations!"
        )


def enter_forest():
    answer = get_choice(
        "Do you CHECK INSIDE the well or CONTINUE WALKING? "
    )

    if answer == "check inside":
        enter_well()
    elif answer == "continue walking":
        print(
            "You come across a clearing containing a run-down hut."
        )
        answer = get_choice(
            "Do you ENTER THE HUT or CONTINUE WALKING? "
        )

        if answer == "enter the hut":
            enter_hut()
        elif answer == "continue walking":
            end_game(
                "You become lost in the forest and succumb to the elements. "
                "Game over."
            )


def main():
    print("Welcome to the game! What is your name?")
    player["Name"] = input().strip()

    print(
        f"Hello, {player['Name']}! "
        "You begin at the mouth of a dense forest."
    )

    answer = get_choice("Do you ENTER THE FOREST or TURN BACK? ")

    if answer == "turn back":
        end_game("You decide to turn back and head home. Game over.")
    elif answer == "enter the forest":
        print ("You step into the forest, the trees closing in around you.")
        enter_forest()


if __name__ == "__main__":
    main()