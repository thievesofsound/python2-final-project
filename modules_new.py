import random
from enum import Enum
import time
class Option:

    def __init__(self, action, description, enum_type):
        self.action = action
        self.description = description

    def __str__(self):
        return self.description

# Create the Input classes

class Input:
    def __init__(self, validate_input, prompt, text_prompt=""):
        self.validate_input = validate_input
        self.prompt = prompt
        self.value = None
        self.text_prompt = text_prompt

    def display_prompt(self):
        # os.system('clear')
        print(self.prompt, end="")

    def get_input(self):
        while True:
            try:
                self.display_prompt()
                self.value = input(self.text_prompt)
                if not self.validate_input(self.value):
                    raise ValueError("not eligible")
            except ValueError:
                print("Sorry, Invalid Input. Try Again.")  # TODO: Convert to Output
            else:
                return self.value

class Output:
    pass

class OptionPicker(Input):
    def __init__(self, options, question, prompt="Here are your options: "):
        self.options = dict(enumerate(options, 1))
        self.question = question
        super().__init__(
            lambda x: x.isdigit() and int(x) in self.options.keys(), prompt
        )
        self.width = max(map(lambda x: len(x.description), self.options.values()))
    def get_options(self):
        x = ""
        for index, option in self.options.items():
            x += f"{index}. {option}\n"
        return x 
    def display_prompt(self):
        format = f"{self.question}\n{self.prompt:}\n" + self.get_options()
        print(format, end="")
    def get_option(self):
        return self.options[int(self.get_input())]


class Checkpoint:
    # create a checkpoint that can be used to save the game to a file(txt), also contains a minigame
    def __init__(self, name, description, minigame):
        self.name = name
        self.description = description
        self.minigame = minigame
        self.return_to = 0

    def action(self, next, revert):
        self.minigame()
        if self.return_to == 0:
            self.return_to += 1
            return revert
        else:
            return next


class Start:
    # create a start that can be used to start the game(checkpoint without game), and set the seed of the game
    def __init__(self, user_name, description, seed):
        self.user_name = user_name
        self.description = description
        self.seed = seed

    def action(self, state_enum):
        # print a message to the user
        print("Welcome to the game!")
        # set the seed of the game
        random.seed(self.seed)


class End:
    # create a end that can be used to end the game(brings back to main menu(not implemented yet))
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def action(self):
        # print a message to the user
        print("Thank you for playing the game!")
        # end the game

class game_continue(Enum):
    FORWARD = 1
    CHECKPOINT = 2

class Story:
    def __init__(self, path):
        self.path = path
        self.current_state = self.path[0]
        self.current_checkpoint = self.path[0]
        self.next = game_continue

    def game_state(self):
        match self.current_state:
            case Start():
                self.current_state.action(game_continue)
                self.current_state = self.path[1]
            case OptionPicker():
                action_start = self.current_state.get_option().action(self.next)
                match action_start:
                    case game_continue.FORWARD:
                        self.current_state = self.path[
                            self.path.index(self.current_state) + 1
                        ]
                    case game_continue.CHECKPOINT:
                        self.current_state = self.current_checkpoint
            case Checkpoint():
                self.current_checkpoint = self.current_state
                self.current_state = self.current_state.action(
                    self.path[self.path.index(self.current_state) + 1],
                    self.current_checkpoint,
                )
            case End():
                self.current_state.action()