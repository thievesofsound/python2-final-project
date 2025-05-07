import random
import time

def sprint(text):
    for c in text:
        print(c, end = "")
        time.sleep(.0)
    print()

class Story:
    def __init__(self,title,text):
        self.title = title
        self.text = text

    def narrate(self):
        sprint(f"\n---{self.title}---\n{self.text}\n")

    def greeting(self):
        sprint(f"{self.text}")

class Choice:
    def __init__(self,description,outcome):
        self.description = description
        self.outcome = outcome

    def make(self):
        sprint(f"{self.outcome} \n")

def present(choices):
        for i, choice in enumerate(choices, 1):
            sprint(f"{i}. {choice.description}")

def choice_input(choices):
    while True:
        try:
            global p_choice
            p_choice = int(input("Choose your decision: "))-1
            assert p_choice >= 0
            return choices[p_choice].make()
            break
        except:
            sprint("Please enter a valid number")
                
class Player:
    def __init__(self,location):
        self.name = ""
        self.location = location
        self.health = 100

    def choose_name(self):
        sprint("Welcome to *PLACEHOLDER*.")
        sprint("\nIn this game you will navigate across cities to reach your desired homeland of California. ")
        sprint("But first, what is name?")
        sprint("You don't have one?")
        sprint("Well... Enter a name then!")
        while True:
            try:
                s_name = input("Name: ")
                assert s_name.isalnum()
                self.name = s_name
                sprint(f"\nWelcome {self.name}! Your game begins below.\n")
                break
            except:
                print("Enter a valid name with no spaces.")
                       
    def move(self,new_place):
        self_location = new_place
        sprint(f"{self.name} has moved to {self.location}")
        time.sleep(1)

    def reduce_health(self,amount):
        self.health -= amount
        sprint(f"Health reduced by {amount}. Current Health: {self.health}")

    def restore_health(self):
        self.health = 100
        sprint("Health restored to 100.")

stories = [Story("Step I: Escaping Astana","\nAstana, Kazakhstan — a gleaming sci-fi city in the heart of Asia, where the skyline screams the future, but the streets whisper unrest. Anti-government militias are tightening their grip, and Astana’s now a lockdown zone. Your only shot at freedom? A train to the U.S. leaves at 9:00 AM. It's 6:32 AM, and the station’s a 2-hour hike away. Rush hour madness starts at 7:30. Time’s ticking, chaos is brewing—what’s your move?"),
           Story("Step II: The Siberian Gauntlet","\nhe train from Astana only takes you so far—it ends at Novosibirsk, deep in Siberia. From here, you’ll need to traverse thousands of kilometers through ice, forests, and secret rail lines to reach the Russian Far East. It’s -12 degrees. Supplies are scarce. A map offers two possible routes forward:"),
           Story("Step III: The Berling Gamble","\nYou’ve reached the edge of Russia. The frozen Bering Strait is your final barrier to American soil. Time is short. Two options lie ahead."),
           Story("Step IV: American Soil, Unfamiliar Land","Alaska is cold and suspicious. You have no ID, no money, no allies. The U.S. may be free—but it’s not easy. Your goal is California. How do you get there?")]

choices1 = [Choice("Sneak past officers", "You barely avoid capture and reach train at 8:52AM."),
            Choice("Create a diversion outside","Diversion fails. You are captured and imprisoned."),
            Choice("Wait for rush hour", "Officers leave. You run to station just in time.")]

choices2 = [Choice("Follow abandoned rail tunnels", "You hide in an abandoned cabin near Russian border."),
            Choice("Travel snowy forests", "A blizzard incapacitates you for weeks. You fail here.")]

choices3 = [Choice("Cross ice at night", "Drones spot you. Captured by Russian soldiers."),
            Choice("Sneak onto cargo ship", "You reach Alaska hidden on the ship.")]

choices4 = [Choice("Hitchhike to US", "You sneak into Washington and find work. (Mid Ending)"),
            Choice("Work on a fishing vessel", "Immigration agents capture you. Detention center ending.")]

def main():
    """Runs main program"""
    i = 0
    while i < 4:
        test = Player("Kazakhstan")
        test.choose_name()
        stories[i].narrate()
        present(choices1)
        choice_input(choices1)
        #2nd indent contains first part
        if p_choice == 0:
            i += 1
            stories[i].narrate()
            present(choices2)
            choice_input(choices2)
            #3rd indent contains 2nd part
            if p_choice == 0:
                i += 1
                stories[i].narrate()
                present(choices2)
                choice_input(choices3)
            #3rd indent contains 2nd part
            if p_choice == 1:
                break
        #2nd indent contains first part    
        if p_choice == 1:
            break
        #2nd indent contains first part
        if p_choice == 2:
            i += 1
            stories[i].narrate()
            present(choices2)
            choice_input(choices2)
            #3rd indent contains 2nd part
            if p_choice == 0:
                i += 1
                stories[i].narrate()
                present(choices2)
                choice_input(choices3)
            #3rd indent contains 2nd part
            if p_choice == 1:
                break
            
                
                
                
        
        
    
main()                 
