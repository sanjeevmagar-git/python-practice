# lets make a program which says only 18+ people can vote.

a = input("Enter your name: ")
b = int(input("Enter your age: "))

if b >= 18:
    print(a, "you can vote.")
elif 16 <= b < 18:
    print(a, "you can almost vote in 2 years!")
else:
    print(a, "Oops! you cannot vote.")