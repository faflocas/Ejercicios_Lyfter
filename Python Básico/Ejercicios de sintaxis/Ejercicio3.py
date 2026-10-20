import random
secret_number = random.randint(1,10)
counter = 0
while counter != secret_number:
    counter = int(input("Guess the secret number between 1 & 10: "))
    if counter == secret_number:
        print("You guessed it!")
    else:
        print("Wrong answer :( try again: ")