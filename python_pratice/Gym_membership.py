# Gym membership 

#basic:
#1 to 3 months   → Rs 500 per month
#above 3 months  → Rs 400 per month

#premium:
#1 to 3 months   → Rs 1000 per month
#above 3 months  → Rs 800 per month

membership = input ("Enter membership plan you want (Basic/Permium): ")
if membership != "Basic" and membership != "Permium" :
    print (membership,": Invalid plan type !")
else:
    months = int(input("Enter the month's: "))
    if months <= 1 :
        print (months,": Invalid months type !")
    else :
        if membership == "Basic" :
            if months <=3 :
                membership = 500
            else:
                membership = 400
        else:
            if months <=3 :
                membership = 1000
            else :
                membership = 800
        total = months * membership
        print ("Your plan for",months,"membership is:",total)
              
