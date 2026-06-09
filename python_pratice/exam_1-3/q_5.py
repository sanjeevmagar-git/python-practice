# Here is my code below:

i_1 = float(input("Enter the price of item 1: "))
i_2 = float(input("Enter the price of item 2: "))
i_3 = float(input("Enter the price of item 3: "))

total = i_1 + i_2 + i_3
discount = total * (10 / 100)
net = total - discount


print (total, ":Is the Price without Discount.")
print (discount, ":Is a Discount amount on it.")
print (net, ":Is a price a Total price after Discount.")