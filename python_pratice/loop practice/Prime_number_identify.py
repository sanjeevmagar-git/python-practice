
for i in range(2, 31):      # outer loop → each number
    for j in range(2, i):   # inner loop → check divisors
        if i % j == 0:  # not prime!
            print (i, ":Its not a prime number.")
        else :
            print (i,":Its  a prime number.")
