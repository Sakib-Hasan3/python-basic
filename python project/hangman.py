word = "hablu"

chances = 5
GuessAdd = []
done = False

while not done:
    # Display the current state of the guessed word
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    
    print()  # Move to the next line after displaying the word

    # Check if the player has guessed the word
    if all(letter.lower() in GuessAdd for letter in word):
        done = True
        break

    # Get the player's guess
    Myguess = input(f"Chances left: {chances}, Guess the letter: ")

    # Check if the guess is valid
    if Myguess.lower() not in GuessAdd:
        GuessAdd.append(Myguess.lower())

        if Myguess.lower() not in word.lower():
            chances -= 1

            if chances == 0:
                done = True
                break
    else:
        print("You already guessed that letter.")

# Check the result of the game
if done:
    if chances > 0:
        print(f"Yes, you have won the game! The word is '{word}'.")
    else:
        print("You lost the game.")