

#Balance is Rs 5000
#Keep asking user how much to withdraw
#Each withdrawal reduces balance
#If balance reaches 0 → "Account empty! 🏦"
#If withdrawal > balance → "Insufficient funds!"
#Stop when balance is 0!


balance = 3000
while balance != 0 :
    withdraw = float(input("Enter the amount you want to withdraw: "))
    if withdraw > balance :
        print ("Insufficent balance")
    else :
        balance -= withdraw
        print ("Remining balance: ",round (balance,2))
    
               
print ("Account Empty !")        

           
                      
#   balance = 3000
# while balance != 0 :
#         withdraw = float(input("Enter the amount you want to withdraw: "))
#         if withdraw > balance :
#             print ("Insufficent balance")
#         else:
#             balance -= withdraw
#             print ("Remaining balance: ",balance)
            
# print ("Account empty !")            
            
        
            
            
            
                                                       