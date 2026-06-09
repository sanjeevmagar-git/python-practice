#Keep generating random numbers between 1 and 10
#Count how many tries it takes to get number 7
#Print "Found 7 in [attempts] attempts!"

import random

number = random.randint(1, 10) 
attempts = 1

while number != 7 :
          number = random.randint(1,10)
          attempts += 1
          

print ("Number:",number,": is correct guess. In total:",attempts,":attempts, well done !")