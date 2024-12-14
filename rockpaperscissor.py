import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")
    return result

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0

    rounds = int(input("How many rounds would you like to play? "))
    for _ in range(rounds):
        result = play_round()
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print(f"Score: You {user_score} - {computer_score} Computer\n")

    print("Game over!")
    if user_score > computer_score:
        print(f"Congratulations, you won! Final Score: You {user_score} - {computer_score} Computer")
    elif user_score < computer_score:
        print(f"Sorry, you lost! Final Score: You {user_score} - {computer_score} Computer")
    else:
        print(f"It's a tie! Final Score: You {user_score} - {computer_score} Computer")

if __name__ == "__main__":
    main()
