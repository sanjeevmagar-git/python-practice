# Here is my code below:
import random

guess = int(input("Enter the number: "))
number = random.randint (1,3)
if guess == number:
   print (number,"Correct! You guessed it!")
else :
   print ("Wrong! The number was",number)