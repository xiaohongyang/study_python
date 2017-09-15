# guess number game!
from random import randint

print("guess number game!");
print("You have 10 chance to guess!");

number = randint(1,100)
guessNumber = guestNumberInit = 10;
isWin = False

while(guessNumber > 0):

    guessNumber = guessNumber-1
    numberCurrent = input("Please enter your number!");

    if numberCurrent > number:
        print("Your number is too big!")
    elif numberCurrent < number:
        print("Your number is too small!")
    if numberCurrent == number :
        isWin = True
        break
if(isWin) :
    print("Congratulation ! Your number is right!")
    print("Your guess time is", guestNumberInit - guessNumber)
else :
    print("Sorry You failed!")
    print( number)

