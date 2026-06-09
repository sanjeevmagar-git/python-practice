# Here is my code:
land = str(input("Do you prefer mountains or beach?"))
weather = str(input("Do you prefer hot or cold weather?"))
if land == "mountains" and weather == "cold" :
    print ("Visit Nepal!")
    if weather == "hot" :
        print ("Visit Ethiopia!")
if land == "beach" and weather == "hot" :
    print ("Visit Maldives!")
    if weather == "cold" :
        print ("Visit Norway!")
