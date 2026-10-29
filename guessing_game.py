import random

number = random.randint(1, 20)
attempts = int(1)

attempt = int(input("Guess the number: "))
while attempt != number and attempts < 5:
    if attempt > number:
        print("Too high!")
        print()
        attempts += 1
    else:
        print("Too low!")
        print()
        attempts += 1
    attempt = int(input("Guess the number: "))
if attempt == number:
    print("Correct!")
    print("You needed %d attempts." % attempts)
else:
    print("You lost, correct number was %d." % number)
