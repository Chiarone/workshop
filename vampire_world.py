import random
import time

print("The world is beautiful! Enjoy it!")

regime = input("Do you prefer night or day?")
name = input("What is your name?")
print(f"Your name is {name} and you are awake at {regime}")
print()
print("Welcome to the dungeon!")


def wrong_input():
    print("Hey, the input is wrong!")


def death_message():
    print("Oh no! You are falling for...")
    for num in range (1,31):
        print(num)
        time.sleep(1)
    print("meters!")
    print("You are dead.")



friends = ["Kate", "Mike", "Rachel", "Bob"]


print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print(f"Hey! Your friend {friends[random.randint(0,3)]} is here!")

    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print(f"Congratulations {name}, you found a new friend!")
    elif vampire == "2":
        death_message()
    else:
        print("You are not so good with numbers, are you?")

elif door == "2":
    print("There is a giant spider asking you if you prefer night or day.")
    print("What do you reply?")
    print("1. Night")
    print("2. Day")

    spider = input("> ")

    if spider == "1":
        print(f"Welcome to the darkness, {name}!")
    elif spider == "2":
        death_message()
    else:
        print("You are not so good with numbers, are you?")

else:
    wrong_input()
