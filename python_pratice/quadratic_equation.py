# let's clacute the quadratic equation :

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: ")) 
d = ((b ** 2 - 4 * a *c )** 0.5) 
x_1= (- b + d) / (2 * a)
x_2 = (- b - d) / (2 * a)

print ("The value of x", round (x_1,2))
print ("The value of x", round (x_2,2))