#Ask user how many temperatures to convert  For each one:
   #Ask temperature in Celsius
   #Convert to Fahrenheit → F = (C × 9/5) + 32
   #Print result!
   
n = int(input("How many temperature you wants to convert: "))
for i in range (1, n+1):
    tc = float(input("Enter the temperature in Celsius: "))
    tf = (tc * 9/5) + 32
    print (round(tf,2),": is the temperature in Fahrenheit.")