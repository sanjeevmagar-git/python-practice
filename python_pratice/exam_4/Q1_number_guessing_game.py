#SECTION 1 — While Loop
#Question 1 [7 Marks]
#Create a number guessing game:- 
#Ask user to keep guessing a number until they guess correctly.
#Correct number is 42.
#Every wrong guess prints 'Wrong! Try again!'.
#Count total attempts.
#When correct print 'You got it in [attempts] attempts!.


guess = int(input("Guess the number: "))
correct = 42
attempt = 1
while guess != correct:
    print ("Wrong ! Try again!")
    guess = int(input("Guess the number: "))
    attempt += 1
 
print ("You got it in",attempt,"attempts!")
