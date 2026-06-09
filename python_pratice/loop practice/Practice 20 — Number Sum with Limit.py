# Keep asking user to enter numbers
# Add each number to total
# Stop when total reaches 100 or above
# Print "Total reached: [total]!"



total = 0
while total < 100 :
    num = int(input("Enter the number: "))
    total += num

print ("Total reached:",total)