import random

print("================================")
print("  STONE PAPER SCISSORS GAME")
print("================================")

# Score initialize karna
player_score = 0
computer_score = 0
draws = 0

# Choices
choices = ["stone", "paper", "scissors"]

while True:

    print("\nChoose your option:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user = input("\nEnter your choice: ").lower()

    # Exit condition
    if user == "4" or user == "exit":
        break

    # Invalid input check
    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    # Computer choice
    computer = random.choice(choices)

    print("\nYou chose:", user)
    print("Computer chose:", computer)

    # Winner decide karna
    if user == computer:
        print("It's a Draw!")
        draws += 1

    elif (
        (user == "stone" and computer == "scissors")
        or (user == "paper" and computer == "stone")
        or (user == "scissors" and computer == "paper")
    ):
        print("Congratulations! You Win!")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Scoreboard
    print("\n========== SCOREBOARD ==========")
    print("Your Score:", player_score)
    print("Computer Score:", computer_score)
    print("Draws:", draws)
    print("================================")

# Final result
print("\n========== FINAL RESULT ==========")
print("Your Score:", player_score)
print("Computer Score:", computer_score)
print("Draws:", draws)

if player_score > computer_score:
    print("🏆 YOU ARE THE CHAMPION!")

elif computer_score > player_score:
    print("COMPUTER IS THE CHAMPION!")

else:
    print("MATCH DRAW!")

print("Thanks for playing!")
