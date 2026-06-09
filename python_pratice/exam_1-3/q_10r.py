# Here is my electricity bill calculator:
  
  
  

units = float(input("Enter the units consumed: "))
if units <= 100 and units >= 0 :
    net = units * 3
    print (net, ": Is your net amount to pay.")
elif units <= 300 and units >= 101 :
    net = units * 5
    print (net, ": Is your net amount to pay.")
elif  units > 300: 
    net = units * 7 
    print (net, ": Is your net amount to pay.")
else :
    print ( " Invalid units.")


