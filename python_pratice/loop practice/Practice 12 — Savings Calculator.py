#Ask user how much they save per month
#Print their total savings for each month from month 1 to 12!

#Example:
#Month 1: Rs 500
#Month 2: Rs 1000
#Month 3: Rs 1500
#...
#Month 12: Rs 6000

saving = int(input("Enter the amount you save per month :"))

for i in range (1,13):
    total = saving * i 
    print ("Month",i,":",total)


