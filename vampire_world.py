print("The world is beautiful! Enjoy it!")

regime = input("Do you prefer night or day?")
name = input("What is your name?")
print(f"Your name is {name} and you are awake at {regime}")
print()
print("Welcome to the dungeon!")
print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print(f"Congratulations {name}, you found a new friend!")
    elif vampire == "2":
        print(f"Sorry {name}, the vampire is faster. You become a dinner.")
    else:
        print("You are not so good with numbers, are you?")

if door == "2":
    print("There is a giant spider asking you if you prefer night or day.")
    print("What do you reply?")
    print("1. Night")
    print("2. Day")

    spider = input("> ")

    if spider == "1":
        print(f"Welcome to the darkness, {name}!")
    elif spider == "2":
        print(f"Sorry {name}. You get eaten.")
    else:
        print("You are not so good with numbers, are you?")
