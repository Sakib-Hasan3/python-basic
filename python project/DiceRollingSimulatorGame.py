import random

dicerolling = True

while dicerolling:
    print(random.randint(1, 6))  # Corrected function name
    
    playAgain = input("Do you want to roll again [y/n]: ")
    
    if playAgain.lower() == "y":  # Added .lower() to handle case sensitivity
        continue
    else:
        print("Game over")
        break