# Print multiplication tables for 
# numbers 1 to 5 automatically!

# Expected output:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 1 x 10 = 10
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 5 x 10 = 50


for i in range(1, 6): # Outer loop for the table number
    print (i)# (Hint: Maybe print a header here like "Table of i")
    for j in range(1, 11): # Inner loop for the multiplier
        # Your math and print statement go here!
        print (i,"*",j, "=" , i * j) # (Hint: Adding an empty print here helps separate the tables)