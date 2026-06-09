#Ask user how many kg they lose per week
#Print their total weight loss for each week from week 1 to 8!

#Example (if user loses 0.5 kg per week):
#Week 1: 0.5 kg lost
#Week 2: 1.0 kg lost
#Week 3: 1.5 kg lost
#...
#Week 8: 4.0 kg lost


weight =float(input("Enter the weight you lose per week: "))
for i in range(1,9):
    total = weight * i
    print ("Week",i,":",total,"kg")