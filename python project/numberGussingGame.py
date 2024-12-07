import random 

# Generate a random number between 1 and 200
randomnumber = random.randrange(1, 201)  # 201 is exclusive

# Prompt the user to guess the number
userInput = int(input("Guess the number (between 1 and 200): "))
print(f"The random number is: {randomnumber}")  # Optional: Show the number for testing

# Check the user's guess
if userInput > randomnumber:
    print("The number is too high.")
elif userInput < randomnumber:
    print("The number is too low.")
else:
    print("Yes, you matched the number!")