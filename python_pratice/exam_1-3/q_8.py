# Here is my code below:

principle =  float(input("Enter the Principle amount : "))
rate = float(input("Enter the Rate : "))
time = float(input("Eenter the Time in year: "))

simple = (principle * rate * time) / 100
total = principle + simple

print (round(simple,2), "Is a Simple Interest.")
print (round(total,2),":Is a Total amount.")
