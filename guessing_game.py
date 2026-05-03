number = int(input("Guess the secret number:"))
while number != 18:
    print("Wrong, try again!")
    number = int(input("Guess the secret number:"))
else:
    print("Correct! You got it!")
