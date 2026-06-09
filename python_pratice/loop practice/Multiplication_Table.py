#Ask user for a number
#Print its multiplication table from 1 to 10!

#Example for 5:
#5 x 1 = 5
#5 x 2 = 10
#...
#5 x 10 = 50

number = int(input("Enter the number from 1 to 10: "))

for i in range (1,11) :
    print (number,"*",i, "=" , number * i)