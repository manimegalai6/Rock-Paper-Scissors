import random

def play():
    print("=== Rock-Paper-Scissors ===")
    choices = ["rock", "paper", "scissors"]
    while True:
        user = input("Enter rock/paper/scissors or 'exit' to quit: ").lower()
        if user == 'exit':
            print("Goodbye!")
            break
        if user not in choices:
            print("Invalid choice.")
            continue
        comp = random.choice(choices)
        print("Computer chose:", comp)
        if user == comp:
            print("It's a tie!")
        elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    play()