#Create an Enter PIN program:
#Correct PIN is 1234
#Keep asking user for PIN until they get it right
#Every wrong attempt prints "Wrong PIN! Try again!"
#When correct prints "Access Granted! Welcome! 
#Solve on paper first then code!


#Enter PIN          ✅ while loop
pin =int(input("Enter your PIN: "))

while pin != 1234 :
    pin =int(input("Wrong PIN! Try again!: "))
else:       
    print ("Access Granted! Welcome!")
