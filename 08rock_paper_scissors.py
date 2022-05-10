plays = {
    "rock": {
        "rock": "It's a tie!",
        "paper": "You win!",
        "scissors": "Computer wins!"
    },
    "paper": {
        "rock": "Computer wins!",
        "paper": "It's a tie!",
        "scissors": "You win!"
    },
    "scissors": {
        "rock": "You win!",
        "paper": "Computer wins!",
        "scissors": "It's a tie!"
    }
}

while True:
    import random
    import secrets

    player = input("Make your move: ")
    if player not in plays:
        print("Invalid input. Try again.")
        continue

    computer = random.choice(list(plays.keys()))
    print(plays[computer][player])
