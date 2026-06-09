# A cinema has the following ticket prices:
# Age below 5 → Free entry
#Age 5 to 12 → 200 rupees
#Age 13 to 64 → 500 rupees
#Age 65 and above → 150 rupees

#Write a program that asks the user their name and age and prints their ticket price

# Here is my code:
 
a = input("Enter your name : ")
b = int(input("Enter you age : "))
if b < 5 :
    print(a , "Hey ! cute little one you have free entry.")
elif b >= 5 and b <= 12 :
    print ( a, "You have been charged 200 rupees only /- ")
elif b >= 13 and b < 64 :
    print ( a, "You have been charged 500 rupees only /- ")
else :
     print(a, "You have been charged 150 rupees only/- ")