"""Example of if-thenelse statements"""

THE_ANSWER_TO_LIFE: int = 42

print("Guess a number...")

guess: int = int(input("Your Guess: "))

if guess == THE_ANSWER_TO_LIFE:
    print("Correct!")
    print("Great work")
else:
    if guess > 42:
        print("Too high!")
    else:
        print("Too low!")
    
print("Game over")



