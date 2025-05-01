import random
from enum import Enum
from rich.panel import Panel
from rich.console import Console, Group
from rich import print as Print
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align
from rich.live import Live
import time
class Option:

    def __init__(self, action, description):
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

class OptionPicker(Input):
    def __init__(self, options, question, prompt="Please choose an option: "):
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
        return Text(x, justify="left") 
    def display_prompt(self):
        # os.system('clear')
        panel_group = Group(
            Panel(Text(self.question, justify="center"), width=self.width),
            Panel(self.get_options(), title="Options"),
        )
        with Live(panel_group, refresh_per_second=10, screen=True):
            
        Print(Align.center(Panel(Text("Hello World")).fit(panel_group)))

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
    def __init__(self, name, description, seed):
        self.name = name
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


class game_continue extends Enum:
    FORWARD = 1
    CHECKPOINT = 2
class Story:
    def __init__(self, path):
        self.path = path
        self.current_state = self.path[0]
        self.current_checkpoint = self.path[0]
        self.next = game_continue
        )

    def game_state(self):
        while True:
            match self.current_state:
                case Start():
                    self.current_state.action()
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
                    break


def reverse(function, state_enum):
    return state_enum.FORWARD


def forward(function, state_enum):
    print("Option 2")
    return state_enum.CHECKPOINT

story_checker = Story(
    [
        Start("Start", "This is the start of the game", 123),
        OptionPicker(
            [
                Option(
                    reverse(),
                    "Try to sneak around surrounding officers on the block to walk to the train.",
                ),
                Option(option_two, "Create a diversion outside."),
            ],
            """It is 6:32 AM. Walking to a train station will take 2 hours on foot and the last train to the US before hell breaks loose is 9:00AM. People are scrambling to escape, but rush hour is at 7:30AM. You can make time. What do you do?""",
        ),
        Checkpoint("Checkpoint 1", "This is a checkpoint", lambda: print("minigame")),
        OptionPicker(
            [Option(option_one, "Option 1"), Option(option_two, "Option 2")],
            "What do you want to do?",
        ),
        End("End", "This is the end of the game"),
    ]
)

story_checker.game_state()
