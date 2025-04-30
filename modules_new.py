import os
import random

class Option:

  def __init__(self, action, description):
    self.action = action
    self.description = description

  def __str__(self):
    return self.description


# Create the Input classes


class Input:

  def __init__(self, validate_input, prompt):
    self.validate_input = validate_input
    self.prompt = prompt
    self.value = None

  def display_prompt(self):
    # os.system('clear')
    print(self.prompt, end="")

  def get_input(self):
    while True:
      try:
        self.display_prompt()
        self.value = input()
        if not self.validate_input(self.value):
          raise ValueError("not eligible")
      except ValueError:
        print("Sorry, Invalid Input. Try Again.")  #TODO: Convert to Output
      else:
        return self.value


class OptionPicker(Input):

  def __init__(self, options, question, prompt="Please choose an option: "):
    self.options = dict(enumerate(options, 1))
    self.question = question
    super().__init__(lambda x: x.isdigit() and int(x) in self.options.keys(),
                     prompt)

  def get_options(self):
    for index, option in self.options.items():
      print(f"{index}. {option}")

  def display_prompt(self):
    # os.system('clear')
    print(self.question)
    self.get_options()
    print(self.prompt, end=" ")

  def get_option(self):
    return self.options[int(self.get_input())]


class Checkpoint:
    #create a checkpoint that can be used to save the game to a file(txt), also contains a minigame
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
  def action(self):
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

class Story:
  def __init__(self, path):
    self.path = path
    self.current_state = self.path[0]
    self.current_checkpoint = self.path[0]
  def game_state(self):
    while True:
      match self.current_state:
        case Start():
          self.current_state.action()
          self.current_state = self.path[1]
        case OptionPicker():
          self.current_state = self.current_state.get_option().action(self.path[self.path.index(self.current_state) + 1], self.current_checkpoint)
        case Checkpoint():
          self.current_checkpoint = self.current_state
          self.current_state = self.current_state.action(self.path[self.path.index(self.current_state) + 1], self.current_checkpoint)
        case End():
          self.current_state.action()
          break

def option_one(next_option, revert):
  print("Option 1")
  return next_option

def option_two(next_option, revert):
  print("Option 2")
  return revert

story_checker = Story(
  [
  Start("Start", "This is the start of the game", 123),
  OptionPicker([Option(option_one, "Option 1"), Option(option_two, "Option 2")], "What do you want to do?"),
  Checkpoint("Checkpoint 1", "This is a checkpoint", lambda:print("minigame")),
  OptionPicker([Option(option_one, "Option 1"), Option(option_two, "Option 2")], "What do you want to do?"),
  End("End","This is the end of the game")
  ]
)
story_checker.game_state()