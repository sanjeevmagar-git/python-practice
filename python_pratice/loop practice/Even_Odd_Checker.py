#Print numbers from 1 to 20
#ven numbers → "X is Even 
#Odd numbers  → "X is Odd 🔴"
#Multiples of 10 → "X is a Multiple of 10! 🎯


for i in range (1,21) :
      if i % 10 == 0 :
         print (i, ": Its a multipes of 10.")

      elif i % 2 == 0 : 
          print (i,":Its a odd number")
      else : 
          print ( i,"Its a even number")