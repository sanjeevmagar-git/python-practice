#Correct username → "admin"
#Correct password → "1234"
#Only allow 3 attempts total!
#After 3 wrong attempts → "Account locked! 🔒"
#When correct → "Welcome admin! ✅


attempts = 0
while attempts < 3 :
    username = str(input("Enter the username: "))
    password = input("Enter the password: ")
    if username == "admin" and password == "1234":
          print ("Welcom admin")
          break
    else: 
          attempts +=1
          print("Wrong! Tries left:", 3 - attempts)
          
    
if attempts == 3 :
         print ("Account locked !")
         

    