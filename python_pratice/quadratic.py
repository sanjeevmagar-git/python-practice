#Let's calcute the following values through qadratic equation.

a = int(input("Enter the value of a :  "))
b = int(input("Enter the value of b :  "))
c = int(input("Enter the value of c :  "))
d = (b ** 2 - 4 * a * c) ** 0.5

x_1 = (- b + d) / (2 * a)
x_2 = (- b  - d) / (2 * a)

print (x_1 , "is value by using +")    
print (x_2 , "is value by using -")