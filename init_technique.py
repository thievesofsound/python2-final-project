import os
import modules_new
from FINALPROJECTBETA import puzzle_minigame, battle_minigame, immigration_gaurds

class DirectStart(modules_new.Start):
    def __init__(self):
        super().__init__()
    
    def action(self, state_enum):
        print("Story is beginning now.")
        # Premise of the story

path = [
    DirectStart(),
    #beginning of Story I
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
        Users are given 3 tries. If they fail, the alarm will ‘sound’ and the game is over.", lambda: modules_new.game_continue.FORWARD if puzzle_minigame() else modules_new.game_continue.CHECKPOINT
        ),

     modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Attempt to cross the ice at night"),
            modules_new.Option(lambda: None, "2. Sneak onto a docked cargo ship"),
        ]

    ),
    modules_new.Checkpoint("Placeholder", "On the cargo ship, you spot something underneath the water circling your ship \
         It’s Wailord! The biggest water type Pokemon ever and he is angry. \
        He has 300 health, and in this battle, your health is regenerated to 100. Beat him in 3 moves or perish", lambda: modules_new.game_continue.FORWARD if battle_minigame() else modules_new.game_continue.CHECKPOINT
        ),

    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Hitchhike down through Canada and into the U.S."),
            modules_new.Option(lambda: None, "2. Take a job on a fishing vessel to fund a bus trip south"),
        ],
    ),

    modules_new.Checkpoint("Placeholder", "Due to recent events, every person in the US is subject to ID checks. \
        Conveniently though, there has been a veteran who was buried recently with all of his possessions, including his empty passport. \
        One issue tho, b/c he was a high ranking general, his gravesite is guarded 24/7 and you must make your way across the graveyard. \
        ", lambda: modules_new.game_continue.FORWARD if immigration_gaurds() else modules_new.game_continue.CHECKPOINT )
    #End of story I

]
direct = modules_new.Story(path)
