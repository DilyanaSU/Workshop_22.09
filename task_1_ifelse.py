#Intro to the game
print()
print("Welcome to dungeon!")
print("Do you go through door 1 or door 2?")

#Recognise the input 1
door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy your life.")
    print("What dou you do?")
    print("1.Smile and nod.")
    print("2.Scream and run.")

    vampire = input(">" )

    if vampire == "1":
        print("Congratulation! You found a new friend!")
    elif vampire == "2":
        print("Sorry, the vampire is faster. You become a dinner.")
    else:
        print("You're not a good with numbers.")
elif door == "3":
    print("😎😎🤔🤔😫😫!")


