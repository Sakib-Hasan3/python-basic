answer = input("Do you want to play this game? [yes/no]: ").strip().lower()

if answer == "yes":
    print("Welcome to the game!")
    
    answer = input("Do you want to go to the jungle or the cave? [jungle/cave]: ").strip().lower()
    
    if answer == "jungle":
        print("You see a hungry tiger... The tiger eats you. Game Over!")
        
    elif answer == "cave":
        print("You see a bear in front of the cave.")
        answer = input("Do you want to fight with the bear or run away? [fight/run]: ").strip().lower()
        
        if answer == "fight":
            print("The bear is too strong! You lose the game. Game Over!")
        elif answer == "run":
            print("Wow! You're still alive! You win!")
        else:
            print("Invalid choice! The bear attacks you while you hesitate. Game Over!")
    else:
        print("Invalid choice! You lose your way and the game ends.")
else:
    print("The game is closed. Goodbye!")
