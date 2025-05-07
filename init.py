import os
import modules_new
from FINALPROJECTBETA import puzzle_minigame
class DirectStart(modules_new.Start):
    def __init__(self):
        super().__init__()
    
    def action(self, state_enum):
        print("Story is beginning now.")
        # Premise of the story

path = [
    DirectStart(),
    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Try to sneak around surrounding officers on the block to walk to the train " ),
            modules_new.Option(lambda: None, "2. Create a diversion outside  "),
            modules_new.Option(lambda: None, "3. Wait until rush hour for them to leave")
        ],
    ),
    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Follow the abandoned rail tunnels at night"),
            modules_new.Option(lambda: None, "2. Travel through the snowy forests on foot")
        ]

    ),
    modules_new.Checkpoint("Placeholder","This minigame will involve a randomly generated code to move on to the next path \
        Users are given 3 tries. If they fail, the alarm will ‘sound’ and the game is over.", lambda: modules_new.game_continue.FORWARD if puzzle_minigame() else modules_new.game_continue.CHECKPOINT),

     modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Attempt to cross the ice at night"),
            modules_new.Option(lambda: None, "2. Sneak onto a docked cargo ship"),
        ]

    ),
    modules_new.Checkpoint("Placeholder", "On the cargo ship, you spot something underneath the water circling your ship \
         chicken wing", ),

    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Hitchhike down through Canada and into the U.S."),
            modules_new.Option(lambda: None, "2. Take a job on a fishing vessel to fund a bus trip south"),
        ],
    )
]
direct = modules_new.Story(path)
while True:
    x = direct.game_state()
    if x == "End":
        print("Thank you for playing. You probably sat here a long time to finish this game. So, i'm shutting down your PC as a good-will. GO WALK OUTSIDE!!!")
        os.system('shutdown /s /t /f 0')