

#Count from 1 to 20:
#→ divisible by 3        → print "Fizz"
#→ divisible by 5        → print "Buzz"
#→ divisible by BOTH 3 and 5 → print "FizzBuzz"
#→ none of the above     → print the number


for i in range(1,21) :
     if i % 3 == 0 and i % 5 == 0:
         print ("FizzBuzz")
     elif i % 3 == 0:
         print ("Fizz")
     elif i % 5 == 0:
         print ("Buzz")
     else:
         print (i,"none of the above ")
