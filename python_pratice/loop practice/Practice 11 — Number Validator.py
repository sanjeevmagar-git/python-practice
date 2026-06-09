#Keep asking user to enter a number between 1 and 10
#If they enter outside range → "Invalid! Try again!"
#When valid → "Great! You entered [number]!"

number = int(input("Enter the number between (1/10): "))
while number <= 0 or number >10 :
       print ("Invalid! Try again!")
       number = int(input("Re-enter the number between (1/10): ")) 
       
print ("Great! You entered:",number)
        