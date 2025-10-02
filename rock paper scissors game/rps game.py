import random

choices = ("rock", "paper", "scissors")
score = 0
is_running = True

while is_running:
    rng_choice = random.choice(choices)
    user_choice = input("Rock paper scissors, shoot: ").lower().strip()
    if user_choice not in choices:
        print("Invalid input please, try again")
    elif user_choice == rng_choice:
        print(f"Draw! Score stays {score}")
    elif user_choice == "rock" and rng_choice == "paper" or \
            user_choice == "scissors" and rng_choice == "rock" or \
            user_choice == "paper" and rng_choice == "scissors":
        print("Computer won!")
        print(f"Computer chose {rng_choice}")
        score -= 1
        print(f"Your score is now {score}")
    else:
        print("You won!")
        print(f"Computer chose {rng_choice}")
        score += 1
        print(f"Your score is now {score}")

    play_again = input("Do you want to play again? (y/n): ").lower().strip()
    if play_again == "n":
        is_running = False
