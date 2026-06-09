# here let's find out a hypotenuse of any user given data:

a = int(input("enter base: "))
b = int(input("enter perpendicular: "))
c = (a ** 2 + b ** 2) ** 0.5

print("Your hypotenuse is:", round (c,2))