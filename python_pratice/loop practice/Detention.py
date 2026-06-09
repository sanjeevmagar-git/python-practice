

#Create a Detention program:
#Ask the user for their name
#Ask them how many times they must write their sentence
#Print "I [name] will not talk in class!" that many times!

name = input("Enter Your name:" )
times = int(input("Enter how many times you want to write:" ))

for i in range(times):
    print("i", name,"will not talk in class!")