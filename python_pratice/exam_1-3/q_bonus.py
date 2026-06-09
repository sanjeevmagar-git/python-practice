# Here is my code below:
    
balance = 5000
c_pin = int(input("Enter the 4 digits pin: "))
if c_pin == 1234 :
    amount = int(input("Enter the amount you want to withdraw:"))
    if amount <= balance and amount > 0 :
          re = balance - amount
          print (amount,"has been withdrawl.")
          print (re,"is remining balance now.")
    elif amount > balance :
          print ("Insufficient Balance !")
    else : 
          print ("Invalid amount entered !")
           
else:
        print ("Incorrect PIN : Access Denied !")

