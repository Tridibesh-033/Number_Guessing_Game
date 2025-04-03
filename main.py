import random
import os 

computer = random.randint(1, 50)
guess = 1
name = input("Enter your name: ")

while True:
    num = int(input("Guess a number between 1 to 50: "))
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

# Read previous best score
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data = f.read().strip()

    if data:  
        try:
            prv_name, prv_guess = data.split()
            prv_guess = int(prv_guess)
        except ValueError:
            prv_name, prv_guess = "None", float('inf')  # Handle incorrect format
    else:
        prv_name, prv_guess = "None", float('inf')  # Handle empty file
else:
    prv_name, prv_guess = "None", float('inf') 

print(f"Previous highest score: {prv_name} with {prv_guess} guesses.")

# Update file only if the new score is better 
if guess < prv_guess:
    with open(file_path, "w") as f:
        f.write(f"{name} {guess}")
    print("Winner, New high score!")


