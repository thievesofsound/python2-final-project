import random
import time

#Simulates typing on computer(to be fixed)
def slow_print(text):
    for char in text:
        print(char, end='')
        time.sleep(.04)
    print()

#holds the story and will narrate the options 
class Story:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def narrate(self):
        slow_print(f"\n--- {self.title} ---\n{self.text}\n")

#when the user picks a choice, the result is printed out and game moves on or ends based on choice
class Choice:
    def __init__(self, description, outcome):
        self.description = description
        self.outcome = outcome

    def make(self):
        slow_print(f"Outcome: {self.outcome}\n")

#Used as a main character, also used to let user know where they are currently located
class Character:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, new_place):
        self.location = new_place
        slow_print(f"{self.name} moved to {self.location}")
        time.sleep(1)

# New player class to store health, 
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 20

    def reduce_health(self, amount):
        self.health -= amount
        slow_print(f"Health reduced by {amount}. Current health: {self.health}")

    def restore_health(self):
        self.health = 20
        slow_print("Health fully restored to 20.")

# prints out the choices that the user can pick from
def present_choices(choices):
    for i, c in enumerate(choices, 1):
        slow_print(f"{i}. {c.description}")
        time.sleep(0.3)

#contains the choice that the user picks
def pick_choice(choices, index):
    return choices[index]

def get_choice_input(choices):
    while True:
        try:
            choice_user = int(input("Choose your action: ")) - 1
            if 0 <= choice_user < len(choices):
                return choice_user
            else:
                slow_print("Invalid choice number. Try again.")
        except ValueError:
            slow_print("Invalid input. Please enter a number.")

#if user picks bad choice, or loses minigame, story ends and prompts them to restart
def ask_retry():
    while True:
        retry = input("Would you like to retry? (yes/no): ").strip().lower()
        if retry in ["yes", "y"]:
            slow_print("\n--- Restarting Game ---\n")
            time.sleep(1.5)
            main()
            return
        elif retry in ["no", "n"]:
            slow_print("\nEnding Game…\n")
            time.sleep(1)
            return
        else:
            slow_print("Please enter yes or no.")

# New minigame for health regeneration
def health_regen_minigame():
    slow_print("\n--- Regeneration Minigame ---")
    number = random.randint(10, 13)
    slow_print("Guess the secret number between 10 and 13. You have 3 tries!")

    for i in range(3):
        try:
            guess = int(input(f"Attempt {i + 1}: "))
            if guess == number:
                slow_print("Correct! You've regained your strength.")
                return True
            else:
                slow_print("Wrong guess.")
        except ValueError:
            slow_print("Please enter a number.")

    slow_print("You failed to guess the number.")
    return False

# Handles the health 
def health_check(player):
    player.reduce_health(10)
    if player.health <= 0:
        slow_print("\nYou're too weak to continue.")
        if health_regen_minigame():
            player.restore_health()
        else:
            slow_print("You failed to regenerate. Game Over.")
            ask_retry()
            return False
    return True

#user must pick random 3 digit number in 3 tries, only used when user picks bad option
def puzzle_minigame():
    slow_print("\n--- Return Minigame: Puzzle Minigame ---")
    code = random.randint(100, 103)
    slow_print("You must guess the 3-digit access code between 100 and 103. You have 3 attempts!")

    for attempt in range(3):
        guess = input(f"Attempt {attempt + 1}: Enter a 3-digit code: ")
        if guess.isdigit() and len(guess) == 3:
            if int(guess) == code:
                slow_print("Correct! You bypassed the alarm.\n")
                return True
            else:
                slow_print("Incorrect code.")
        else:
            slow_print("Invalid input. Enter 3 digits.")

    slow_print("\nAlarm triggered! You have been captured.\n--- Game Over ---")
    ask_retry()

#epic pokemon battle
def battle_minigame():
    slow_print("\n--- Checkpoint: Wailord Battle ---")
    player_health = 100
    wailord_health = 300
    special_moves = []

    slow_print("Wailord appears! You must beat him in 3 moves or perish.")

    slow_print("\nYou find two items beneath the cargo ship:")
    slow_print("1. Electric Beam\n2. Bamboo Stick")

    move1 = get_choice_input(["Electric Beam", "Bamboo Stick"])

    if move1 == 0:
        damage = random.randint(90, 110)
        wailord_health -= damage
        player_health -= 40
        special_moves.append(damage)
        slow_print(f"You used Electric Beam! Wailord loses {damage} HP.")
        slow_print("Wailord smashes you with his tail. You lose 40 HP.")
    else:
        damage = random.randint(45, 55)
        wailord_health -= damage
        player_health -= 25
        slow_print(f"You used Bamboo Stick! Wailord loses {damage} HP.")
        slow_print("Wailord splashes you with water. You lose 25 HP.")

    slow_print("\nIn the chaos, you spot more items:")
    slow_print("1. Electroweb\n2. Syrup Bomb")

    move2 = get_choice_input(["Electroweb", "Syrup Bomb"])

    if move2 == 0:
        wailord_health -= 25
        player_health -= 50
        slow_print("You used Electroweb. It was weak. Wailord loses 25 HP.")
        slow_print("Wailord eats and spits you out. You lose 50 HP.")
    else:
        wailord_health -= 150
        special_moves.append(150)
        slow_print("You used Syrup Bomb. Very effective! Wailord loses 150 HP.")

    slow_print("\nFinally, you find two more items:")
    slow_print("1. Mushrooms\n2. Plasma Gloves")

    move3 = get_choice_input(["Mushrooms", "Plasma Gloves"])

    if move3 == 0:
        wailord_health -= 20
        player_health -= 20
        slow_print("You used Mushrooms. Both you and Wailord lose 20 HP.")
    else:
        wailord_health -= 125
        special_moves.append(125)
        slow_print("You used Plasma Gloves. Super effective! Wailord loses 125 HP.")

    slow_print(f"\nFinal Health: You = {player_health} | Wailord = {wailord_health}")

    if player_health <= 0:
        slow_print("\nYou have died. Wailord wins!\n--- Game Over ---")
        ask_retry()
        return

    if wailord_health <= 0:
        slow_print("\nYou defeated Wailord!")
        if any(move >= 100 for move in special_moves):
            slow_print("You achieved the SPECIAL POKEMON ENDING!")
        else:
            slow_print("You move forward to Alaska.")
    else:
        slow_print("\nWailord finishes you off as he still stands!\n--- Game Over ---")
        ask_retry()

#Immigration checkpoint for final
def immigration_gaurds():
    print("\n--- Checkpoint: immigration ---")
    print("Due to recent events, every person in the US is subject to ID checks.")
    print("Conveniently though, there has been a veteran who was buried recently with all of his possessions, including his passport.")
    print("One issue though; becuase he was a high ranking gneral , his gravesite is gaurded 24/7")

    row1 = [4,5]
    row1_choice = random.choice(row1)
    while True:
        try:
            guess1 = int(input("\nEnter a number 1-7 to move up: "))
            if guess1 > row1_choice and guess1 > 0 and guess1 < 8:
                slow_print("Congrats, You have moved up to row 2")
            else:
                slow_print("You have been captured and beaten to death.")
                slow_print("Prompt to retry")
                break
            row2_choice = random.choice(row1)
            guess1 = int(input("\nEnter a number 1-7 to move up: "))
            if guess1 < row2_choice and guess1 > 0 and guess1 < 8:
                slow_print("Congrats, You have moved up to row 3")
            else:
                slow_print("You have been captured and beaten to death.")
                slow_print("Prompt to retry")
                break
            row3_choice = random.choice(row1)
            guess1 = int(input("\nEnter a number 1-7 to move up: "))
            if guess1 < row3_choice and guess1 > 0 and guess1 < 8:
                slow_print("Congrats, You have moved up to row 4")
            else:
                slow_print("You have been captured and beaten to death.")
                slow_print("Prompt to retry")
                break
            row4_choice = random.choice(row1)
            guess1 = int(input("\nEnter a number 1-7 to move up: "))
            if guess1 < row4_choice and guess1 > 0 and guess1 < 8:
                slow_print("Congrats, You have moved up to row 5")
            else:
                slow_print("You have been captured and beaten to death.")
                slow_print("Prompt to retry")
                break
            row5_choice = random.choice(row1)
            guess1 = int(input("\nEnter a number 1-7 to move up: "))
            if guess1 > row5_choice and guess1 > 0 and guess1 < 8:
                slow_print("Congrats, You have escaped the gaurds!")
            else:
                slow_print("You have been captured and beaten to death.")
                slow_print("Prompt to retry")
                break
        except Exception:
            slow_print("Enter a number please.")

        

#contains the stories
story_parts = [
    Story("Step I - Escape Astana", "Welcome User. You are currently located in Astana, Kazakhstan. Astana is under strict rule. It is 6:32 AM. You need to reach the train station by 9:00 AM to begin your journey. What do you do?"),
    Story("Step II - The Siberian Gauntlet", "The train ends at Novosibirsk, Russia. You must cross Siberia in its freezing weather. What do you do?"),
    Story("Step III - The Bering Gamble", "You reached Russia's edge. You see some ice you can walk on. You also see a cargo ship. What do you do?"),
    Story("Step IV - American Soil", "Alaska is very cold. You must find a way to reach California.")
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
    hero = Character("Guy", "Astana")
    player = Player("Guy")
    count = 0

    while count < len(story_parts):
        if not health_check(player):
            return

        part = story_parts[count]
        part.narrate()

        if count == 0:
            present_choices(choices_step1)
            choice_user = get_choice_input(choices_step1)
            choice = pick_choice(choices_step1, choice_user)
            choice.make()

            if "fail" in choice.outcome.lower() or "captured" in choice.outcome.lower():
                puzzle_minigame()
            else:
                hero.move("Train")

        elif count == 1:
            present_choices(choices_step2)
            choice_user = get_choice_input(choices_step2)
            choice = pick_choice(choices_step2, choice_user)
            choice.make()

            if "fail" in choice.outcome.lower() or "captured" in choice.outcome.lower():
                puzzle_minigame()
            else:
                hero.move("Russian Border")

        elif count == 2:
            present_choices(choices_step3)
            choice_user = get_choice_input(choices_step3)
            choice = pick_choice(choices_step3, choice_user)
            choice.make()

            if "captured" in choice.outcome.lower():
                puzzle_minigame()
            else:
                hero.move("Train")

            if choice_user == 1:
                battle_minigame()

            hero.move("Alaska")

        elif count == 3:
            present_choices(choices_step4)
            choice_user = get_choice_input(choices_step4)
            choice = pick_choice(choices_step4, choice_user)
            choice.make()

            if "capture" in choice.outcome.lower():
                puzzle_minigame()
            else:
                hero.move("Train")

            if choice_user ==1:
                immigration_gaurds()

            hero.move("California" if choice_user == 0 else "Detention Center")

        # Print current health after each story step
        slow_print(f"Current Health: {player.health}\n")

        count += 1

    slow_print("\n--- The End ---")

if __name__ == "__main__":
    main()



