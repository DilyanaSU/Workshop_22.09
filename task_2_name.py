#Intro to the game
name = input("What is your name?")

print(f"Welcome to dungeon, {name}!")
print("Do you go through door 1 or door 2?")

#Put the > at the first place
door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy your life.")
    print("What dou you do?")
    print("1.Smile and nod.")
    print("2.Scream and run.")

    vampire = input(">" )

    if vampire == "1":
        print(f"Congratulation, {name}! You found a new friend!")
    elif vampire == "2":
        print(f"Sorry {name}, the vampire is faster. You become a dinner.")
    else:
        print("You're not a good with numbers.")


    wolfs = input(">" )

    if wolfs == "yes":
        print()

elif door == "3":
    print("😎😎🤔🤔😫😫!")


