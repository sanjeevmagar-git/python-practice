#SECTION 1 — While Loop
#Question 3 [7 Marks]
#Create a password strength enforcer:
#Keep asking user to create a password.
#Password length below 8 → 'Too short! Try again!.
#Password length 8 or above → 'Strong password! Saved! '.
#Count how many attempts it took.
#Print attempts at end.
#Hints : use len() function

attempts = 1
password = input("Enter the length of your password: ")
while len(password) <= 8:
    print ("Too short! Try again!.")
    password = input("Enter the length of your password: ")
    attempts +=1

print ("Strong password! Saved!") 
print ("In",attempts,"attempts.")