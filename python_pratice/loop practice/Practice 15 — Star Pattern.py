#Ask user for a number
#Print stars that many times like this 
#(if user enters 5):
#*
#* *
#* * *
#* * * *
#* * * * *
number = int(input("Enter the number: "))
for i in range (1,number + 1):
    for j in range (1, i + 1):
        print("*", end= " " )
     
    print()            