import random
import os  # To check file existence

computer = random.randint(1, 10)
guess = 1
name = input("Enter your name: ")

while True:
    num = int(input("Guess a number between 1 to 10: "))
    if num == computer:
        print("Congratulations!! Correct guess")
        break
    elif num > computer:
        print("Please take a smaller number")
    else:
        print("Please take a larger number")

    guess += 1

print(f"Your Guess score is {guess}")

file_path = r"D:\python\new\proj2\score.txt"

# Read previous best score safely
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data = f.read().strip()

    if data:  
        try:
            prv_name, prv_guess = data.split()  # Extract name and score
            prv_guess = int(prv_guess)
        except ValueError:
            prv_name, prv_guess = "None", float('inf')  # Handle incorrect format
    else:
        prv_name, prv_guess = "None", float('inf')  # Handle empty file
else:
    prv_name, prv_guess = "None", float('inf')  # Assume no previous score if file doesn't exist

print(f"Previous highest score: {prv_name} with {prv_guess} guesses.")

# Update file only if the new score is better (lower)
if guess < prv_guess:
    with open(file_path, "w") as f:
        f.write(f"{name} {guess}")  # Store name and score correctly
    print("Winner, New high score!")


