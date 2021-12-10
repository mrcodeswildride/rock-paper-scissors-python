import os
import random

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def print_game_state():
  cls()
  print()

  print("---------------")
  print(f"You: {player_score}")
  print(f"Computer: {computer_score}")
  print("---------------\n")

def get_choice():
  while True:
    choice = input("Choose [r]ock, [p]aper, or [s]cissors: ").lower()

    if choice in ["r", "rock"]:
      return "rock"
    elif choice in ["p", "paper"]:
      return "paper"
    elif choice in ["s", "scissors"]:
      return "scissors"
    else:
      print("Invalid choice.\n")

player_score = 0
computer_score = 0

while True:
  print_game_state()

  player_choice = get_choice()
  computer_choice = random.choice(["rock", "paper", "scissors"])

  print(f"Computer chose {computer_choice}.\n")

  if player_choice == computer_choice:
    input("Tie game. Press enter to play again. ")
  elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
    player_score += 1
    input("You win. Press enter to play again. ")
  else:
    computer_score += 1
    input("Computer wins. Press enter to play again. ")
