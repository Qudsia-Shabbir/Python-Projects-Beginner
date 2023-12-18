import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']

    while True:
        try:
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if user_choice not in choices:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
                continue

            computer_choice = random.choice(choices)

            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}\n")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (
                (user_choice == 'rock' and computer_choice == 'scissors') or
                (user_choice == 'paper' and computer_choice == 'rock') or
                (user_choice == 'scissors' and computer_choice == 'paper')
            ):
                print("You win!")
            else:
                print("You lose!")

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing. Goodbye!")
                break

        except EOFError:
            print("Error: Unexpected end of input. Exiting the game.")
            break

if __name__ == "__main__":
    rock_paper_scissors()
