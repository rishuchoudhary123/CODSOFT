import random


options = ["rock", "paper", "scissors"]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    print("Rock, Paper, Scissors Game")
    print("Options: rock, paper, scissors")
    
    player_choice = input("Your choice: ").lower()
    if player_choice not in options:
        print("Invalid choice. Please choose from 'rock', 'paper', or 'scissors'.")
        continue
    
    computer_choice = random.choice(options)
    
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
