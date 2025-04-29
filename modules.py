from enum import Enum
## Templates
class Player:
    """Stores health attributes, and tiredness attributes. And the location in the story, when ending"""
    def __init__(self):
        self.health = 100
        self.tiredness = 100
        self.location = None #TODO: Figure out location
        self.name = ""

class Story:
    def __init__(self):
        pass

class Path:
    def __init__(self, states):
        pass

#when the user picks a choice, the result is printed out and game moves on or ends based on choice

class continuer(Enum):
    CONTINUE = auto()
    REVERT = auto()

class Choice:
    def __init__(self, description, options):
        self.description = description
        self.options = options
        self.input_function = Input(lambda x: x in [options.keys()])
    def run(self, state_continue, state_revert):
        self.input_value = self.input_function.get_input()
        value = options[self.input_value].action()
        match continue:
            case CONTINUE:
                return state_continue
            case REVERT:
                return state_revert

class Option:
    def __init__(self, description, action, continuer):
        self.description = description
        self.action = action
        self.continue = continuer
    def action(self):
        self.action()
        return continuer

class Input:
    def __init__(self, check):
        self.check = check
    def get_input(self, prompt):
        while True:
            try:
                self.value = input(prompt)
                assert self.check(), "not eligible"
            except AssertionError:
                print("Sorry, Invalid Input. Try Again.") #TODO: Convert to Output
            else:
                return self.value()

class Checkpoint:
    pass

class Start:
    pass

class End:
    pass



list_of_choices = [Choice(), Choice(), Choice()]
running_index = 0
match (currentState):
    case Choice():
        currentState = choice.run_based_on_input()
