#Ask user for a number
#Print multiplication table from 1 to 10
#But skip multiples of 5 using if inside loop!

number = int(input("Enter the number: "))
for i in range (1,11) :
      if i % 5 != 0:    # if i is NOT a multiple of 5 → print!
          print (number,"*",i, "=" , number * i)
          