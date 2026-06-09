

#99 bottles of milk on the wall
#99 bottles of milk
#Take one down, pass it around
#98 bottles of milk on the wall!

#Start from 99 and count down to 1
#Each loop prints the verse with correct number
#When it reaches 0 print "No more bottles of milk on the wall! 
#Solve on paper first then code! 

for i in range(99, 0, -1):   # 99 down to 1
    print(i, "bottles of milk on the wall")
    print(i, "bottles of milk")
    print("Take one down, pass it around")
    print(i-1, "bottles of milk on the wall!")

print("No more bottles! 🍾")