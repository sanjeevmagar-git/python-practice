

#Guess Number       ✅ while + random + counter


#Sometimes you want to count how many times something happens:
#Your Homework 🎯
#Create a Guess the Number game:
#Python picks a random number between 1 and 10
#Ask user to keep guessing until they get it right
#Every wrong guess prints "Too high! 🔺" or "Too low! 🔻"
#When correct print "Correct! 🎉 You got it in [attempts] attempts!"
#1. Generate random number
#2. Ask first guess
#3. Start attempts counter
#4. while guess is wrong → give hint → ask again
#5. Print result with attempts count

import random

secret = random.randint (1,10)
guess = int(input("Enter the number you guess: "))
attempts = 1

while guess != secret:
    if guess > secret:
        print ("Too high! 🔺")
    else:
        print ("Too low! 🔻")
    guess = int(input("Wrong guess! Try again: "))
    attempts + 1  

print (guess,": Is your right guessed number", attempts, ":Is you total attempts.")