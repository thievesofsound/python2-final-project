import random
import time

def print_delay(text, delay=1):
    print(text)
    time.sleep(delay)

def pharaoh_battle():
    player_health = 200
    pharaoh_health = 500
    pharoah_medallion = ""

    print_delay("PHARAOH: THE EVIL ENFORCER")
    print_delay("After stealing the briefcase and making your way, you believe you are home free...")
    print_delay("But wait! Who is that formulating in that massive sand storm?")
    print_delay("Low and behold, it is THE MIGHTY PHARAOH and he wants to take your money AND your life!")
    print_delay(f"Your Health: {player_health} | PHARAOH'S Health: {pharaoh_health}\n")

    # First move
    print("What move would you like to use first?")
    print("1. Double Kick (-75 boss health, you lose 50)")
    print("2. Vacuum Wave (-50 boss health, you lose 25)")
    choice1 = input("Enter 1 or 2: ")
    if choice1 == "1":
        pharaoh_health -= 75
        player_health -= 50
        print_delay("You used Double Kick! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Supersonic!")
    else:
        pharaoh_health -= 50
        player_health -= 25
        print_delay("You used Vacuum Wave! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Smelling Salts!")

    print(f"Your Health: {player_health} | PHARAOH'S Health: {pharaoh_health}\n")

    # Second move
    print("What move would you like to do second?")
    print("1. Mach Punch (-75 boss health, you lose 25)")
    print("2. Combat Torque (-100 boss health, you lose 75)")
    choice2 = input("Enter 1 or 2: ")
    if choice2 == "1":
        pharaoh_health -= 75
        player_health -= 25
        print_delay("You used Mach Punch! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Egg Bomb!")
    else:
        pharaoh_health -= 100
        player_health -= 75
        print_delay("You used Combat Torque! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Facade!")

    print(f"Your Health: {player_health} | PHARAOH'S Health: {pharaoh_health}\n")

    # Third move
    print("What move would you like to do third?")
    print("3. Jump Kick (-150 boss health, you lose 50)")
    print("4. Flying Press (-75 boss health, you lose 25)")
    choice3 = input("Enter 3 or 4: ")
    if choice3 == "3":
        pharaoh_health -= 150
        player_health -= 50
        print_delay("You used Jump Kick! It was devastating!")
        print_delay("THE MIGHTY PHARAOH used Sand Attack!")
    else:
        pharaoh_health -= 75
        player_health -= 25
        print_delay("You used Flying Press! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Echoed Voice!")

    print(f"Your Health: {player_health} | PHARAOH'S Health: {pharaoh_health}\n")

    # Final move
    print("What move would you like to do last?")
    print("5. Focus (-250 boss health, you lose 25)")
    print("6. Collision Curse (-200 boss health, you lose 25)")
    choice4 = input("Enter 5 or 6: ")
    if choice4 == "5":
        pharaoh_health -= 250
        player_health -= 25
        print_delay("You used Focus! A finishing blow!")
        print_delay("THE MIGHTY PHARAOH used Mega Kick!")
    else:
        pharaoh_health -= 200
        player_health -= 25
        print_delay("You used Collision Curse! Dark energy erupts!")
        print_delay("THE MIGHTY PHARAOH used Smelling Salts!")

    print(f"Your Final Health: {player_health} | PHARAOH'S Final Health: {pharaoh_health}\n")

    # Outcome
    if pharaoh_health <= 0 and player_health > 0:
        print_delay("THE MIGHTY PHARAOH HAS BEEN DEFEATED!")
        chance = random.random()
        if chance < 0.15:
            print_delay("You feel a strange energy surround you...")
            print_delay("You have inherited the PHARAOH'S lifestyle: opulence, power, and respect.")
            print_delay("Your stats increase drastically. You are now a living legend.")
            print("** RICHNESS OPULENCE ENDING UNLOCKED **")
            #**PHAROAH_MEDALLION ADDED INTO INVENTORY 
        else:
            print_delay("Though the PHARAOH is defeated, his curse fades into the wind...")
            print("You walk away victorious, but the sands keep their secrets.")
            print("** STANDARD VICTORY ENDING **")
    elif player_health <= 0:
        print_delay("You collapse before THE MIGHTY PHARAOH.")
        print_delay("Your journey ends here...")
        print("** GAME OVER **")
    else:
        print_delay("Both you and PHARAOH collapse... the storm consumes you.")
        print("** DOUBLE K.O. ENDING **")


def storm_navigation():
    print("\n--- Step III: Storm Navigation ---")
    print("A violent sandstorm howls around you.")
    print("You must choose a direction to navigate through it.")
    print("Only one direction leads to safety. The others will cost you health!")

    health = 100
    directions = ['north', 'south', 'east', 'west']

    for step in range(1, 4):
        correct_path = random.choice(directions)
        print(f"\nStep {step}: Choose a direction (north, south, east, west)")
        choice = input("Your choice: ").lower()

        if choice == correct_path:
            print("You move cautiously and find safe ground.")
        elif choice in directions:
            health -= 25
            print("You stumble through harsh winds and burning sand!")
            print(f"-25 Health | Current Health: {health}")
        else:
            print("Invalid direction! You hesitate and the storm punishes you!")
            health -= 25
            print(f"-25 Health | Current Health: {health}")

        if health <= 0:
            print("\nThe storm overwhelms you. You collapsed under the weight of the desert.")
            print("** GAME OVER **")
            return

    print("\nYou've made it through the storm with your life.")
    print(f"Final Health: {health}")
    print("** STORM SURVIVED **")


import random

def obstacle_navigation():
    print("\n--- Step IV: Obstacle Navigation ---")
    print("You face a series of deadly obstacles in the desert.")
    print("Roll the dice to navigate through them.")
    print("1-2 = Safe | 3-4 = Not Safe | 5-6 = Injured")

    safe_count = 0
    injured = False

    while True:
        input("\nPress Enter to roll the dice...")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}.")

        if roll in [1, 2]:
            safe_count += 1
            print(f"Safe! ({safe_count} safe roll(s))")
        elif roll in [5, 6]:
            injured = True
            print("You were injured!")
        else:
            print("Not safe! Try again.")

        # Check win conditions
        if safe_count >= 3:
            print("\nYou've safely navigated the obstacles!")
            print("*OBSTACLE CLEARED*")
            break
        elif injured and safe_count >= 2:
            print("\nDespite injury, you've managed to get through!")
            print("*OBSTACLE CLEARED*")
            break

