import random

#holds the story and will narrate the options 
class Story:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def narrate(self):
        print(f"\n--- {self.title} ---\n{self.text}\n")

#when the user picks a choice, the result is printed out and game moves on or ends based on choice
class Choice:
    def __init__(self, description, outcome):
        self.description = description
        self.outcome = outcome

    def make(self):
        print(f"Outcome: {self.outcome}\n")

#Used as a main character, also used to let user know where they are currently located
class Character:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, new_place):
        self.location = new_place
        print(f"{self.name} moved to {self.location}")

# prints out the choices that the user can pick from
def present_choices(choices):
    for i, c in enumerate(choices, 1):
        print(f"{i}. {c.description}")

#contains the choice that the user picks
def pick_choice(choices, index):
    return choices[index]

def get_choice_input(choices):
    """Gets user input to choose a choice between 0 and the number of choices available"""
    while True:
        try:
            choice_user = int(input("Choose your action: ")) - 1
            if 0 <= choice_user < len(choices):
                return choice_user
            else:
                print("Invalid choice number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#if user picks bad choice, or loses minigame, story ends and prompts them to restart
def ask_retry():
    while True:
        retry = input("Would you like to retry? (yes/no): ").strip().lower()
        if retry == "y":
            print("\n--- Restarting Game ---\n")
            main() 
            return
        elif retry == "n":
            print("\nEnding Game….\n")
            break
        else:
            print("Please enter y for yes or n for no.")

#user must pick random 3 digit number in 3 tries
def puzzle_minigame():
    """User is prompted to enter a three digit number in 3 tries. If they fail, game is over and asked to retry"""
    print("\n--- Checkpoint: Puzzle Minigame ---")
    code = random.randint(100, 131)
    print("You must guess the 3-digit access code between 100 and 130. You have 3 attempts!")

    for attempt in range(3):
        guess = input(f"Attempt {attempt + 1}: Enter a 3-digit code: ")
        if guess.isdigit() and len(guess) == 3:
            if int(guess) == code:
                print("Correct! You bypassed the alarm.\n")
                return True
            else:
                print("Incorrect code.")
        else:
            print("Invalid input. Enter 3 digits.")

    print("\nAlarm triggered! You have been captured.\n--- Game Over ---")
    ask_retry()

#epic pokemon battle
def battle_minigame():
    print("\n--- Checkpoint: Wailord Battle ---")
    player_health = 100
    wailord_health = 300
    special_moves = []

    print("Wailord appears! You must beat him in 3 moves or perish.")

    # move 1
    print("\nYou find two items beneath the cargo ship:")
    print("1. Electric Beam\n2. Bamboo Stick")

    move1 = get_choice_input(["Electric Beam", "Bamboo Stick"])

    if move1 == 0:
        damage = random.randint(90, 110)
        wailord_health -= damage
        player_health -= 40
        special_moves.append(damage)
        print(f"You used Electric Beam! Wailord loses {damage} HP.")
        print("Wailord smashes you with his tail. You lose 40 HP.")
    else:
        damage = random.randint(45, 55)
        wailord_health -= damage
        player_health -= 25
        print(f"You used Bamboo Stick! Wailord loses {damage} HP.")
        print("Wailord splashes you with water. You lose 25 HP.")

    #move 2
    print("\nIn the chaos, you spot more items:")
    print("1. Electroweb\n2. Syrup Bomb")

    move2 = get_choice_input(["Electroweb", "Syrup Bomb"])

    if move2 == 0:
        wailord_health -= 25
        player_health -= 50
        print("You used Electroweb. It was weak. Wailord loses 25 HP.")
        print("Wailord eats and spits you out. You lose 50 HP.")
    else:
        wailord_health -= 150
        special_moves.append(150)
        print("You used Syrup Bomb. Very effective! Wailord loses 150 HP.")

    # move 3
    print("\nFinally, you find two more items:")
    print("1. Mushrooms\n2. Plasma Gloves")

    move3 = get_choice_input(["Mushrooms", "Plasma Gloves"])

    if move3 == 0:
        wailord_health -= 20
        player_health -= 20
        print("You used Mushrooms. Both you and Wailord lose 20 HP.")
    else:
        wailord_health -= 125
        special_moves.append(125)
        print("You used Plasma Gloves. Super effective! Wailord loses 125 HP.")

    # Prints final battle outcome
    print(f"\nFinal Health: You = {player_health} | Wailord = {wailord_health}")

    if player_health <= 0:
        print("\nYou have died. Wailord wins!\n--- Game Over ---")
        ask_retry()
        return

    if wailord_health <= 0:
        print("\nYou defeated Wailord!")
        if any(move >= 100 for move in special_moves):
            print("You achieved the SPECIAL POKEMON ENDING!")
        else:
            print("You move forward to Alaska.")
    else:
        print("\nWailord finishes you off as he still stands!\n--- Game Over ---")
        ask_retry()

#contains the stories
story_parts = [
    Story("Step I - Escape Astana",
              "Astana is under strict rule. It is 6:32 AM. You need to reach the train station by 9:00 AM. What do you do?"),
    Story("Step II - The Siberian Gauntlet",
              "Train ends at Novosibirsk. You must cross Siberia in freezing weather."),
    Story("Step III - The Bering Gamble",
              "You reached Russia's edge. Cross the Bering Strait or sneak on a cargo ship."),
    Story("Step IV - American Soil",
              "Alaska is cold. You must find a way to reach California.")
]

#Has the choices that will print out based on user input
choices_step1 = [
    Choice("Sneak past officers", "You barely avoid capture and reach train at 8:52AM."),
    Choice("Create a diversion", "Diversion fails. You are captured and imprisoned."),
    Choice("Wait for rush hour", "Officers leave. You run to station just in time.")
]

choices_step2 = [
    Choice("Follow abandoned rail tunnels", "You hide in an abandoned cabin near Russian border."),
    Choice("Travel snowy forests", "A blizzard incapacitates you for weeks. You fail here.")
]

choices_step3 = [
    Choice("Cross ice at night", "Drones spot you. Captured by Russian soldiers."),
    Choice("Sneak onto cargo ship", "You reach Alaska hidden on the ship.")
]

choices_step4 = [
    Choice("Hitchhike to US", "You sneak into Washington and find work. (Mid Ending)"),
    Choice("Work on a fishing vessel", "Immigration agents capture you. Detention center ending.")
]


def main():
    """Contains main program and has a counter that is added on to after every decision, thus continuing the story"""
    hero = Character("Guy", "Astana")
    count= 0

    while count< len(story_parts):
        part = story_parts[count]
        part.narrate()

        if count== 0:
            present_choices(choices_step1)
            choice_user = get_choice_input(choices_step1)
            choice = pick_choice(choices_step1, choice_user)
            choice.make()

            if "fail" in choice.outcome.lower() or "captured" in choice.outcome.lower():
                print("\nYou failed. Game Over.\n")
                ask_retry()
                return

            hero.move("Train")

        elif count== 1:
            present_choices(choices_step2)
            choice_user = get_choice_input(choices_step2)
            choice = pick_choice(choices_step2, choice_user)
            choice.make()

            if "fail" in choice.outcome.lower() or "captured" in choice.outcome.lower():
                puzzle_minigame()
            else:
                hero.move("Russian Border")

        elif count== 2:
            present_choices(choices_step3)
            choice_user = get_choice_input(choices_step3)
            choice = pick_choice(choices_step3, choice_user)
            choice.make()

            if "captured" in choice.outcome.lower():
                print("\nYou failed. Game Over.\n")
                ask_retry()
                return

            if choice_user == 1:
                battle_minigame()

            hero.move("Alaska")

        elif count== 3:
            present_choices(choices_step4)
            choice_user = get_choice_input(choices_step4)
            choice = pick_choice(choices_step4, choice_user)
            choice.make()

            if "captured" in choice.outcome.lower():
                print("\nYou failed. Game Over.\n")
                ask_retry()
                return

            hero.move("California" if choice_user == 0 else "Detention Center")

        count+= 1

    print("\n--- The End ---")

if __name__ == "__main__":
    main()


