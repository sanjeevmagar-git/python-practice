#SECTION 1 — While Loop
#Question 2 [7 Marks]
#Create a shopping cart total calculator:
#Keep asking user to enter item prices.
#Add each price to total.
#Stop when user enters 0.
#Print total bill at end.
#Note: entering 0 means user is done shopping!.

price = float(input("Enter item price: "))
total = 0
while price !=0:
    price = float(input("Enter item price: "))
    total += price
    
print(total,":is your total bill.")
???????????????????????????????????????????