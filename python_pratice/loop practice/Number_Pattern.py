#Print this pattern using for loop:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5



for i in range(1, 6):
    for j in range (1,i+1):
        print (j, end = " ")
    print()           
      
        
     # outer loop → rows 1 to 5
              # inner loop → prints 1 to i
      # end=" " keeps on same line!
           # moves to next line!    