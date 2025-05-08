import os
import modules_new
from minigame import puzzle_minigame1,p_dice

class DirectStart(modules_new.Start):
    def __init__(self):
        super().__init__()
    
    def action(self, state_enum):
        print("Story is beginning now.")
        # Premise of the story

path = [
    DirectStart(),
    #beginning of Story III
    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Steal a militia uniform" ),
            modules_new.Option(lambda: None, "2. Use sewer tunnels  "),
            modules_new.Option(lambda: None, "3. Hijack a car")
        ]
    ),
    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Infiltrate black-market cargo train"),
            modules_new.Option(lambda: None, "2.  Build a sled and cross alone"),
            modules_new.Option(lambda: None, "3. Bribe a defecting fuel driver"),
            modules_new.Option(lambda: None, "4. Rob a secret Russian gold convoy")

        ]

    ),
    modules_new.Checkpoint("When stealing the briefcase from the Russians/Or stealing the map, there is a ticking bomb \
         You must enter a 3 digit code to disarm the bomb, or you will explode!" \
        , lambda: modules_new.game_continue.FORWARD if puzzle_minigame1() else modules_new.game_continue.CHECKPOINT
        ),

     modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Blow up drone outpost"),
            modules_new.Option(lambda: None, "2. Sneak onto radioactive cargo ship"),
            modules_new.Option(lambda: None, "3. Paraglide across the strait")
        ]

    ),
    modules_new.Checkpoint("Placeholder", "After blowing up the drone outpost, guards take aim at you \
         You must dodge their shots, unaware of where they come from. \
        ", lambda: modules_new.game_continue.FORWARD if p_dice() else modules_new.game_continue.CHECKPOINT
        ),

    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Hack a U.S. ID"),
            modules_new.Option(lambda: None, "2. Claim asylum as a war reporter"),
            modules_new.Option(lambda: None, "3. Join a survivalist militia")
        ],
    ),

    #End of story III

]
direct = modules_new.Story(path)
while True:
    x = direct.game_state()
    if x == "End":
        print("Thank you for playing. You probably sat here a long time to finish this game. So, i'm shutting down your PC as a good-will. GO WALK OUTSIDE!!!")
        os.system('shutdown /s /t /f 0')