#Keep asking user for password until they get it right!
#Correct password is "python123"
#Every wrong attempt → "Wrong password! Try again!"
#When correct → "Access granted! Welcome! ✅"

user = input("Enter the Username: ")
attempts = 1
          
while user != "Bahadur":
          user = input("Unverified user ! try again: ")
          attempts + 1
print ("Verified User !", user, " In this much attempts :", attempts)
        


password = input("Enter the Password: ")
attempts = 1
          
while password != "python1234" : 
    password = input("Wrong password ! Try again!: ")
    attempts + 1
          
print ("Access granted! Welcome!", user,". In this much attempts :", attempts)
        