import random


print("**************************************")
print("Welcome to the game! Guess the number:")
print("**************************************")

print("rules: You have to guess a number between 1 and 100.")

number = random.randint(1, 100)
guess = None

difficulty = int(input("Choose a difficulty level (1.easy, 2.medium, 3.hard): "))

if difficulty == 1:
    chances = 10
elif difficulty == 2:
    chances = 5
elif difficulty == 3:
    chances = 1
else:
    print("error")

while chances > 0 : 
    guess = int(input("Enter your guess: "))
    chances -= 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number!, the number was {number}.")
        break

if chances == 0:
    print(f"Sorry, you ran out of chances. The number was {number}.")