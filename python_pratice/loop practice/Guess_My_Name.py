#Store a secret name "Python"
#Keep asking user to guess the name
#Count attempts
#After correct guess print:
#"You got it in [attempts] tries! 🎉"

secret = "python"
guess = input("Guess the name: ")
attempts = 1
while guess != secret :
          guess = input ("Wrong guess ! Guess Again: ")
          attempts += 1

print (guess,"Yeah, You got correct guess ! Congratulation ! in total attempts:", attempts)
           