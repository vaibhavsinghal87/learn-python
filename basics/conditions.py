from random import randint;

age = input("How old are you?\n");
age = int(age);

if age >= 21:
    print("Come on in!");
else:
    print("Go home kid!");

# ***************************************************

color = "blue";
if color == "blue":
    print("Beginner");
elif color == "green":
    print("Intermediate");
elif color == "black":
    print("Advanced");
else:
    print("Please start again");

# ***************************************************

rand = randint(0, 1);
if rand == 0:
    print("HEADS!");
else:
    print("TAILS!");
