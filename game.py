import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
    def get_winner(player, computer):
    if player == computer:
        return "tie"
        if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"
def play_game():
    player_score = 0
    computer_score = 0








